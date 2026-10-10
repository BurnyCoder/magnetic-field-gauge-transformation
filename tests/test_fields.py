"""Global: protect the gauge transformation physics before plotting is implemented.

Local: check explicit endpoints and independent derivatives/integrals.
Sources: https://numpy.org/doc/stable/reference/generated/numpy.gradient.html
and https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf, p. 6.
"""

import numpy as np  # Array operations let every test cover a spatial grid.
import pytest  # Parameterization repeats physical checks for field reversals.

from gauge_fields.fields import gauge_scalar, potential  # These are the public mathematical functions.


@pytest.mark.parametrize("b", [-2.0, 0.0, 1.0])  # Reverse, remove, and restore the field.
def test_endpoints_and_midpoint(b):
    """Global: anchor the slider to both potentials; local: compare exact components."""
    x, y = np.array([-2.0, 0.0, 1.0]), np.array([1.0, 0.0, -2.0])  # Include both signs and the origin.
    zero = np.zeros_like(x)  # All three gauges have zero z component.
    np.testing.assert_allclose(potential(x, y, b, 0), np.stack((zero, b*x, zero), axis=-1))  # The first potential.
    np.testing.assert_allclose(potential(x, y, b, 1), np.stack((-b*y, zero, zero), axis=-1))  # The second potential.
    np.testing.assert_allclose(potential(x, y, b, 0.5), np.stack((-b*y/2, b*x/2, zero), axis=-1))  # Symmetric gauge.


@pytest.mark.parametrize("b", [-2.0, 0.0, 1.0])  # The gradient identity must preserve the sign of b.
def test_difference_is_scalar_gradient(b):
    """Global: establish the gauge transformation; local: differentiate the scalar independently."""
    axis = np.linspace(-2, 2, 17)  # Uniform spacing makes finite differences exact for bilinear s.
    x, y = np.meshgrid(axis, axis)  # Rows vary in y and columns vary in x.
    ds_dy, ds_dx = np.gradient(gauge_scalar(x, y, b), axis, axis, edge_order=2)  # Respect meshgrid axis order.
    gradient = np.stack((ds_dx, ds_dy, np.zeros_like(x)), axis=-1)  # Reassemble Cartesian gradient components.
    np.testing.assert_allclose(potential(x, y, b, 1)-potential(x, y, b, 0), gradient, atol=1e-12)  # Check A' = A + grad s.


@pytest.mark.parametrize("b", [-2.0, 0.0, 1.0])  # Include the physically degenerate zero-field case.
@pytest.mark.parametrize("gauge", [0, 0.25, 0.5, 0.75, 1])  # Check intermediate gauges, not just endpoints.
def test_curl_and_closed_loop_flux(b, gauge):
    """Global: protect gauge invariance; local: use independent grid and line-integral formulas."""
    axis = np.linspace(-2, 2, 17)  # Use more points than the display requires.
    x, y = np.meshgrid(axis, axis)  # Evaluate the full plane slice.
    field = potential(x, y, b, gauge)  # Only the field evaluation comes from production code.
    curl = np.gradient(field[..., 1], axis, axis=1)-np.gradient(field[..., 0], axis, axis=0)  # Curl z = dAy/dx - dAx/dy.
    np.testing.assert_allclose(curl, b, atol=1e-12)  # Every point must have the same magnetic field.
    corners = np.array([[-0.7, -0.4], [1.3, -0.4], [1.3, 0.6], [-0.7, 0.6], [-0.7, -0.4]])  # CCW rectangle, area 2.
    steps = np.diff(corners, axis=0)  # Each directed side contributes A dot dl.
    midpoints = (corners[:-1]+corners[1:])/2  # Midpoint quadrature is exact for these affine vector fields.
    values = potential(midpoints[:, 0], midpoints[:, 1], b, gauge)[:, :2]  # Discard the identically zero z component.
    assert np.sum(values*steps) == pytest.approx(2*b, abs=1e-12)  # Stokes' theorem predicts b times the area.


def test_scalar_value_and_broadcasting():
    """Global: keep the model reusable; local: check point inputs and a gauge constant."""
    assert gauge_scalar(2, 3, 4, constant=5) == -19  # -bxy+C fixes the sign and allows the irrelevant constant.
    np.testing.assert_array_equal(potential(2, 3, 4, 0), [0, 8, 0])  # A single point yields one three-vector.
    assert potential(np.array([0, 1]), 2, 1, 0.5).shape == (2, 3)  # Scalars broadcast over coordinate arrays.
