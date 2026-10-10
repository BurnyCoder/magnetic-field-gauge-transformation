# Experiment 1 — independently check the proposed gauge family

Date: 2026-10-10 (Europe/Berlin).

## Question and hypothesis

Does Aλ=(-λby,(1-λ)bx,0) have curl (0,0,b) for every selected gauge?
Differentiation predicts (1-λ)b+λb=b. The corresponding gauge function is
s=-bxy, and its constant offset is irrelevant.

## Method

During planning, an in-memory Python calculation evaluated central differences
with step 0.0001 at (-2,1), (0,0), and (1,-2). It combined b=-1,0,1 with
λ=0,0.25,0.5,0.75,1, giving 45 point/gauge/strength cases. The test compared
the measured z curl with b using absolute tolerance 1e-9. The implementation
session's tool output is the evidence for this exploratory run; it did not
create a raw log file or alter the repository.

## Result and interpretation

All 45 cases passed. The maximum absolute error was approximately 1.56e-12.
This small residual is floating-point subtraction error in the finite
difference, not a physical change in the magnetic field. The analytic result
remains exact. Subsequent grid tests use exactly representable sample spacing
and are documented separately rather than retroactively replacing this result.

## Learning and choice

The continuous family gives the slider a direct mathematical interpretation.
Its midpoint is the symmetric gauge, making rotational symmetry visible.
We chose this family because it connects the two potentials directly without
adding another physical model.

The mathematical convention and invariant closed-loop integral were checked
against [MIT's solution, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf).
