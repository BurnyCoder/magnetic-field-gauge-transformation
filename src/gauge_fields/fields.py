"""Global: one source of field samples for static and interactive presentations.

Local: implement two vector potentials and their scalar gauge function.
Sources: docs/reference-text.md; https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf;
https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html .
"""

from dataclasses import dataclass  # Keep arrays together without a mutable global cache.

import numpy as np  # Broadcasting supports both point evaluations and full grids.

from gauge_fields.config import Settings  # Sampling consumes the shared validated configuration.


def potential(x, y, b=1.0, gauge=0.0):
    """Global: connect both showcase potentials; local: return A + gauge*grad(-bxy)."""
    x, y = np.broadcast_arrays(np.asarray(x, dtype=float), np.asarray(y, dtype=float))  # Align scalar and array coordinates.
    return np.stack((-gauge*b*y, (1-gauge)*b*x, np.zeros_like(x)), axis=-1)  # The final dimension holds (Ax, Ay, Az).


def gauge_scalar(x, y, b=1.0, constant=0.0):
    """Global: identify the gauge freedom; local: evaluate s=-bxy+C, not electric potential."""
    return -b*np.asarray(x)*np.asarray(y)+constant  # Differentiation gives (-by, -bx, 0) independently of C.


@dataclass(frozen=True)  # Each export receives the same sampled arrays and arrow scale.
class Samples:
    """Global: rendering data contract; local: retain fields on one shared xy mesh."""

    x: np.ndarray  # Horizontal sample positions.
    y: np.ndarray  # Vertical sample positions.
    first: np.ndarray  # The slider's starting potential, (0,bx,0).
    second: np.ndarray  # The slider's ending potential, (-by,0,0).
    difference: np.ndarray  # The connecting gradient, computed from those endpoints.
    scalar: np.ndarray  # Scalar samples for contours beneath the gradient.
    b: float  # The invariant perpendicular magnetic field.
    limit: float  # Padded display boundary prevents edge arrows from clipping.
    scale: float  # One inverse arrow-length scale is used for all potentials.


def sample_fields(settings: Settings) -> Samples:
    """Global: synchronize both renderers; local: sample once and derive a common geometric scale."""
    axis = np.linspace(-settings.extent, settings.extent, settings.points)  # Include both boundaries and the origin.
    x, y = np.meshgrid(axis, axis)  # Columns correspond to x, rows to y.
    first, second = potential(x, y, settings.b, 0), potential(x, y, settings.b, 1)  # Evaluate the two exact gauge endpoints.
    difference = second-first  # Reuse endpoints instead of duplicating the gradient formula.
    spacing = float(axis[1]-axis[0])  # Grid spacing controls a readable maximum arrow length.
    maximum = float(np.max(np.linalg.norm(difference, axis=-1)))  # This field bounds both endpoints and their interpolation.
    scale = maximum/(1.2*spacing) if maximum else 1.0  # Keep small-screen arrows readable while each Cartesian component stays inside the half-spacing padding.
    return Samples(x, y, first, second, difference, gauge_scalar(x, y, settings.b), settings.b, settings.extent+spacing/2, scale)  # Share arrays without resampling.
