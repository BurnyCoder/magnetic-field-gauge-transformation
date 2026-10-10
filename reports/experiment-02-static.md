# Experiment 2 — test the field model and inspect scientific figures

Date: 2026-10-10 (Europe/Berlin).

## Question and hypothesis

Can one small implementation produce comparable plots without losing the
exercise's field signs, gradient relation, or circulation? Shared coordinates,
equal aspect, and a fixed arrow scale should preserve meaningful comparisons.

## Method and evidence

We wrote endpoint, midpoint, scalar-gradient, curl, and circulation tests before
implementing the model. The first test run failed during collection because
the field module did not yet exist. After implementation, 22 tests passed.
The production validation evaluates 15 gauge/strength combinations on a
17-by-17 grid and checks a counterclockwise unit square independently.

The first complete command finished at 11:55:41 UTC. Its timestamped generation
log recorded zero maximum residuals for the grid curl, gradient identity, and
unit-square circulation, with a tolerance of 1e-10. These affine/bilinear fields
and dyadic sample spacing yield exact results in those particular floating-point
calculations; this does not imply arbitrary numerical derivatives are exact.
Each run saves current residuals in `outputs/validation.json`.

## Issue, correction, and result

Visual inspection found small diagonal artifacts in the zero scalar contour
near the saddle at the origin. The exact zero contour is the pair of coordinate
axes. We therefore retained the exact axes and plotted only nonzero contour
levels. This removes an ambiguous contour interpolation at a degenerate crossing
without changing field data. The corrected pipeline completed at 11:56:14 UTC.

The PNG was inspected for arrows, sign changes, labels, contour geometry, and
uniform perpendicular B symbols. The PDF is checked for one page and no raster
images. The working mathematical core and its outputs were pushed in commit
`84f11f8` before the interactive feature and final review.

## Learning and choice

Matplotlib was sufficient; a custom scientific renderer would add unnecessary
work. Its [quiver documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html)
guided Cartesian arrow directions, explicit scale, and common pivot. Zero
vectors are omitted. The separate B panel avoids projecting the entire magnetic
field to zero in the xy plane.
