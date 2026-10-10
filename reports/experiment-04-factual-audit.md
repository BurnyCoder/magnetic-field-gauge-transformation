# Experiment 4 — factual audit of the gauge transformation showcase

Date: 2026-10-10 (Europe/Berlin).

## Question and method

Does the explanation accurately connect changing vector-potential arrows to
an invariant magnetic field? We compared the reference passages with the
written derivation, differentiated the potentials and connecting scalar, and
checked the circulation argument. [MIT's electromagnetic derivation, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf)
independently supports gradient gauge changes, invariant fields, and unchanged
closed-loop circulation. Existing export and browser checks were updated before
renaming the generated files. The first export run failed at the expected new
PNG path, confirming that the tests required the new deliverable names.

## Findings and corrections

The core mathematics was correct: both curls are (0,0,b), their difference is
the gradient of s=-bxy+C, and the slider midpoint is one half of B cross r.
No field formula needed to change. We clarified the explanation in four places:

- Curl's z component is oriented circulation per unit area in the shrinking-loop
  limit. Each nonzero square-side contribution is bL²/2 for the displayed square
  centered at the origin; an off-center square preserves the total bL².
- The zero contour is the two axes only when b is nonzero and C=0. At b=0,
  s=0 everywhere for C=0. The signed component b has field magnitude |b|.
- The slider selects spatially constant, static gauges. It does not represent
  physical time. The electric-potential transformation uses an explicitly
  stated SI convention; the gauge function is distinct from electric potential.
- The gradient identity uses smooth, single-valued functions. Their explicit
  connecting scalar establishes the relation globally for this example.

## Presentation and reasoning

Gauge transformation is now the primary subject in titles, plot labels, browser
metadata, package metadata, and artifact names. Selected reference passages
retain their wording and remain separate from the added explanation. Broad
historical and formalism claims are outside this static classical demonstration
and are omitted. No unverified book attribution is introduced.

We retained the existing NumPy, Matplotlib, and sampled-data browser design:
the review found an explanation and presentation issue, not a new mathematical
model or rendering requirement. The PNG and vector PDF use the same shared
arrow scale as before. The report is still generated from these Markdown records.

## Validation and review

`uv run gauge-fields` completed at 12:30:27 UTC. All 15 gauge/strength cases
had zero measured curl, gradient, and circulation residuals at tolerance 1e-10.
`uv run pytest -q` passed all 37 tests in 16.41 seconds, including complete
generation for b=-1,0,1 and native keyboard/browser checks at 736, 360, and 320
pixels. Seven new generation/browser logs contained no warning or error entries.
The figure, desktop/phone views, and report page were visually inspected; the
one-page figure PDF contains no raster images.

One review pass checked factual scope, reference fidelity, artifact paths,
documentation, and unchanged numeric-only browser data. GitHub reported the
repository's current canonical name as magnetic-field-gauge-transformation;
clone instructions and PDF links now use it. No dependencies or mathematical
formulas changed. Browser-engine and host-integration limits remain documented
in the [initial acceptance record](verification.md).
