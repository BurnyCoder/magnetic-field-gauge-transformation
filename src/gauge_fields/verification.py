"""Global: attach independent numerical evidence to generated figures.

Local: verify derivatives and oriented circulation, rather than trusting a label.
Sources: https://numpy.org/doc/stable/reference/generated/numpy.gradient.html
and https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf, p. 6.
"""

import json  # Save machine-readable residuals alongside the plots.
import logging  # Report residuals immediately to both configured handlers.

import numpy as np  # Grid derivatives provide an independent check on the closed-form expressions.

from gauge_fields.fields import gauge_scalar, potential  # Verify the same functions used to produce plot samples.


def verify_fields(output):
    """Global: reject incorrect physics before delivery; local: compare curl, gradient, and loop integrals."""
    axis = np.linspace(-2, 2, 17)  # These validation coordinates are independent of plot settings.
    x, y = np.meshgrid(axis, axis)  # Finite differences act along rows and columns.
    corners = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]])  # Unit-area CCW square.
    steps, middle = np.diff(corners, axis=0), (corners[:-1]+corners[1:])/2  # Midpoint quadrature is exact on each linear edge.
    residuals = {"curl": 0.0, "gradient": 0.0, "circulation": 0.0}  # Accumulate the worst errors across all gauges.
    for b in (-2.0, 0.0, 1.0):  # Include reversal and a truly empty field.
        dy, dx = np.gradient(gauge_scalar(x, y, b), axis, axis, edge_order=2)  # Differentiate s independently of A'-A.
        gradient = np.stack((dx, dy, np.zeros_like(x)), axis=-1)  # Restore Cartesian component order.
        residuals["gradient"] = max(residuals["gradient"], float(np.max(np.abs(potential(x, y, b, 1)-potential(x, y, b, 0)-gradient))))  # Check the gauge's sign.
        for gauge in (0, 0.25, 0.5, 0.75, 1):  # Verify intermediate gauges as well as both endpoints.
            field = potential(x, y, b, gauge)  # Evaluate the implemented potential family.
            curl = np.gradient(field[..., 1], axis, axis=1)-np.gradient(field[..., 0], axis, axis=0)  # Compute curl z from sampled derivatives.
            residuals["curl"] = max(residuals["curl"], float(np.max(np.abs(curl-b))))  # The expected magnetic field is exactly b.
            integral = np.sum(potential(middle[:, 0], middle[:, 1], b, gauge)[:, :2]*steps)  # Sum A dot dl around the unit square.
            residuals["circulation"] = max(residuals["circulation"], float(abs(integral-b)))  # Flux through a unit square is b.
    if max(residuals.values()) > 1e-10:  # Stop on a material disagreement rather than exporting a success claim.
        raise ValueError(f"Gauge identity validation failed: {residuals}")  # The shared exception handler preserves the evidence.
    result = {"cases": 15, "grid_points_per_case": 289, "tolerance": 1e-10, "maximum_absolute_errors": residuals}  # Define what was actually tested.
    (output/"validation.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")  # Keep inspectable validation results with the deliverables.
    logging.info("Validated 15 gauges/strengths on 289 points each; errors: %s", residuals)  # Summarize actual numerical evidence.
    return result  # Let later phases include the evidence without rerunning the experiment.
