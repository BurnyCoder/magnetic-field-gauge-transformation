"""Global: export four scientifically comparable panels as PNG and vector PDF.

Local: reuse Samples and Matplotlib's quiver, contour, and scatter primitives.
Sources: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html
and https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html .
"""

import logging  # Record successful exports in the shared run log.
from pathlib import Path  # Accept any configured output directory.

import matplotlib  # Select a noninteractive renderer before importing pyplot.
matplotlib.use("Agg")  # Generation works on servers without a desktop display.
import matplotlib.pyplot as plt  # Reuse the plotting library rather than drawing scientific plots by hand.
import numpy as np  # Mask zero-length arrows and subsample the magnetic markers.

from gauge_fields.fields import Samples  # Both presentations share this rendering contract.


def format_axes(axis, samples):
    """Global: preserve comparisons; local: use identical limits, units, and equal aspect."""
    axis.set(xlim=(-samples.limit, samples.limit), ylim=(-samples.limit, samples.limit), xlabel="x (illustrative units)", ylabel="y (illustrative units)")  # Match every panel's coordinate frame.
    axis.set_aspect("equal", adjustable="box")  # A diagonal vector has its physical direction on screen.
    axis.grid(color="#dce3eb", linewidth=0.6, zorder=0)  # A quiet grid supports comparison without obscuring arrows.
    axis.axhline(0, color="#aab7c4", linewidth=0.8, zorder=0)  # Make sign changes at the axes easy to identify.
    axis.axvline(0, color="#aab7c4", linewidth=0.8, zorder=0)  # Mark the zero-potential line in the first gauge.
    axis.tick_params(labelsize=9)  # Maintain readable, secondary numeric tick labels.


def draw_potential(axis, samples, field, title):
    """Global: compare arrow direction and magnitude honestly; local: disable per-panel autoscaling."""
    nonzero = np.linalg.norm(field, axis=-1) > 0  # A zero vector has no arrowhead or misleading dot.
    arrows = axis.quiver(samples.x[nonzero], samples.y[nonzero], field[..., 0][nonzero], field[..., 1][nonzero], angles="xy", scale_units="xy", scale=samples.scale, pivot="middle", color="#175da8", width=0.005, minlength=0, zorder=3)  # Match Cartesian direction and the shared magnitude scale.
    axis.set_title(title, fontsize=13, pad=15)  # Label the actual mathematical field, not a generic panel number.
    if samples.b:  # An arrow legend is meaningful only for a nonzero field.
        key = abs(samples.b)*float(np.max(np.abs(samples.x)))  # Choose a useful reference magnitude from the sampled range.
        axis.quiverkey(arrows, 0.78, 1.02, key, f"{key:g} A-units", labelpos="E", fontproperties={"size": 8})  # Make the common scale explicit.


def export_static(samples: Samples, output: Path) -> None:
    """Global: create the downloadable deliverable; local: compose and save all four panels."""
    figure, axes = plt.subplots(2, 2, figsize=(11, 10), layout="constrained")  # Give each vector field enough room to read.
    figure.suptitle("Exercise 3 · Different potentials, the same magnetic field", fontsize=17)  # State the physical comparison.
    for axis in axes.flat:  # All fields use the same spatial coordinate convention.
        format_axes(axis, samples)  # Reuse one formatting routine to prevent aspect or limit drift.
    draw_potential(axes[0, 0], samples, samples.first, r"$\mathbf{A}=(0,bx,0)$")  # Vertical shear in Equation (8).
    draw_potential(axes[0, 1], samples, samples.second, r"$\mathbf{A}'=(-by,0,0)$")  # Horizontal shear in Equation (9).
    draw_potential(axes[1, 0], samples, samples.difference, r"$\nabla s=\mathbf{A}'-\mathbf{A}$,  $s=-bxy$")  # Plot the gradient which changes the gauge.
    if samples.b:  # A constant zero scalar has no meaningful contour family.
        levels = np.linspace(-0.75*np.max(np.abs(samples.scalar)), 0.75*np.max(np.abs(samples.scalar)), 7)  # Choose symmetric contour values for either sign of b.
        contours = axes[1, 0].contour(samples.x, samples.y, samples.scalar, levels=levels[levels != 0], colors="#8695a7", linewidths=0.8)  # The axes already represent s=0 exactly; omit its ambiguous marching-squares saddle.
        axes[1, 0].clabel(contours, fontsize=8, inline=True, fmt="%g")  # Label contour values instead of adding an unrelated color scale.
    loop = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]])*min(1, np.max(np.abs(samples.x)))  # Fit the same CCW test square in every configured domain.
    for axis in axes[0]:  # The identical loop makes the two circulation calculations comparable.
        axis.plot(loop[:, 0], loop[:, 1], color="#d07623", linewidth=1.3, zorder=4)  # Mark the integration boundary without implying a field line.
        axis.annotate("", xy=loop[1], xytext=(loop[0]+loop[1])/2, arrowprops={"arrowstyle": "->", "color": "#d07623"})  # Indicate counterclockwise orientation along the lower edge.
    magnetic = axes[1, 1]  # The last panel represents the perpendicular physical field.
    magnetic.set_title(r"$\mathbf{B}=\nabla\times\mathbf{A}=\nabla\times\mathbf{A}'=(0,0,b)$", fontsize=13, pad=15)  # Identify both curls with one field.
    mx, my = samples.x[::2, ::2], samples.y[::2, ::2]  # Magnetic symbols need fewer samples than planar arrows.
    if samples.b:  # Avoid depicting a magnetic field when its magnitude is zero.
        magnetic.scatter(mx, my, s=105, facecolors="none", edgecolors="#175da8", linewidths=1.0)  # Circles denote the shaft's view along z.
        magnetic.scatter(mx, my, s=12 if samples.b > 0 else 30, marker="." if samples.b > 0 else "x", color="#175da8", linewidths=1.0)  # Dots point out of the page; crosses point into it.
    direction = "out of page (+z)" if samples.b > 0 else "into page (-z)" if samples.b < 0 else "zero magnetic field"  # State the sign independently of color.
    magnetic.text(0.5, 0.025, f"b = {samples.b:g} · {direction}", transform=magnetic.transAxes, ha="center", fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})  # Explain symbols without comparing B's units to A's.
    figure.supxlabel("z = 0 · shared arrow scale for A, A′ and ∇s · orange squares: circulation loops", fontsize=10)  # Clarify the slice and the scale convention.
    for extension in ("png", "pdf"):  # Keep a screen-friendly image and a publication-friendly vector file.
        path = output/f"exercise-3-fields.{extension}"  # Deterministic names make README links stable.
        figure.savefig(path, dpi=180, facecolor="white")  # Matplotlib keeps the PDF geometry vector-based.
        logging.info("Exported static figure: %s", path)  # Record each completed artifact.
    plt.close(figure)  # Release resources during tests and repeated generation.
