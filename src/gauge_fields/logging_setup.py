"""Global: make each generation observable; local: stream identical UTC records to file and console.

Source: https://docs.python.org/3/howto/logging.html .
"""

import logging  # Standard handlers flush records as they are emitted.
import sys  # Send console progress to the caller's terminal.
import time  # Format record timestamps consistently in UTC.
from datetime import UTC, datetime  # Use timezone-aware run identifiers.
from pathlib import Path  # Keep log files under the current workspace.


def start_logging() -> Path:
    """Global: establish run evidence; local: install two handlers with identical formatting."""
    directory = Path("logs")  # Raw run logs stay local and are ignored by Git.
    directory.mkdir(exist_ok=True)  # The first run needs no manual directory setup.
    path = directory/f"generate-{datetime.now(UTC):%Y%m%dT%H%M%S.%fZ}.log"  # Microseconds distinguish immediate reruns.
    formatter = logging.Formatter("%(asctime)sZ %(levelname)s %(name)s: %(message)s", "%Y-%m-%dT%H:%M:%S")  # Readable sortable UTC timestamps.
    formatter.converter = time.gmtime  # The suffix Z must actually describe UTC.
    handlers = [logging.FileHandler(path, encoding="utf-8"), logging.StreamHandler(sys.stdout)]  # Write evidence and real-time progress together.
    for handler in handlers:  # Apply exactly the same formatting on both destinations.
        handler.setFormatter(formatter)  # Avoid silent differences between the terminal and saved evidence.
    logging.basicConfig(level=logging.INFO, handlers=handlers, force=True)  # Replace prior handlers during repeat invocations.
    logging.captureWarnings(True)  # Library warnings belong in the same run log.
    logging.info("Logging started: %s", path)  # Make the run's evidence location discoverable.
    return path  # Allow a caller to link the complete log if needed.
