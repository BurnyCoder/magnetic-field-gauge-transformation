"""Global: keep plotting configuration out of the mathematics.

Local: merge the working directory's .env with process settings and validate them.
Sources: https://bbc2.github.io/python-dotenv/ and
https://docs.python.org/3/library/dataclasses.html .
"""

import os  # Explicit environment settings override the optional local file.
from dataclasses import dataclass  # A small immutable record replaces a configuration framework.
from math import isfinite  # Reject NaN and infinity before creating invalid figures or JSON.
from pathlib import Path  # Resolve output locations portably.

from dotenv import dotenv_values  # Reuse the library's .env parser without changing process state.


@dataclass(frozen=True)  # Settings remain consistent across every generation phase.
class Settings:
    """Global: shared rendering contract; local: store validated plot parameters."""

    b: float = 1.0  # Magnetic field strength in illustrative units.
    extent: float = 2.0  # Sample both coordinates from -extent to +extent.
    points: int = 13  # An odd grid includes the zero-potential axes and origin.
    output: Path = Path("outputs")  # Export inside the user's working directory by default.

    def __post_init__(self):
        """Global: fail clearly on unsupported settings; local: bound the visualization's numeric range."""
        if not isfinite(self.b) or abs(self.b) > 100:  # Keep generated magnitudes and labels within a useful teaching range.
            raise ValueError("GAUGE_B must be finite and between -100 and 100.")  # Explain the supported configuration.
        if not isfinite(self.extent) or not 0.1 <= self.extent <= 10:  # Avoid degenerate axes and unreadable extremes.
            raise ValueError("GAUGE_EXTENT must be between 0.1 and 10.")  # Fail before sampling or file export.
        if not isinstance(self.points, int) or self.points < 5 or self.points > 25 or self.points % 2 == 0:  # Bound density and include zero.
            raise ValueError("GAUGE_POINTS must be an odd integer from 5 to 25.")  # Tell the user how to repair the setting.


def load_settings() -> Settings:
    """Global: one configuration entry point; local: apply environment-over-file precedence."""
    values = {**dotenv_values(Path.cwd()/".env"), **os.environ}  # Read only this repository's local configuration.
    return Settings(  # Dataclass construction also performs the shared validation.
        b=float(values.get("GAUGE_B", "1")),  # Retain the algebra's b parameter.
        extent=float(values.get("GAUGE_EXTENT", "2")),  # Use symmetric axes for comparison.
        points=int(values.get("GAUGE_POINTS", "13")),  # Control display density independently of the mathematics.
        output=Path(values.get("GAUGE_OUTPUT", "outputs")),  # Allow a separate directory for trial runs.
    )
