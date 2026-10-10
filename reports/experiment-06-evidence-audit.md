# Experiment 6 — verify the explanation and its evidence

Date: 2026-10-10 (Europe/Berlin).

## Question and method

Does the current gauge transformation explanation contain an incorrect equation,
an unsupported physical claim, or an invented quotation or attribution? We
rechecked the [derivation](../docs/explanation.md) against the field implementation,
the supplied reference text, the original implementation conversation, and Git
history through `c54931b`. We inspected the plotted directions, common arrow
scale, scalar contours, and circulation-loop orientation. Existing mathematical
and full-pipeline tests were run before changing the documentation.

Direct differentiation and the oriented square integral provide the mathematical
check. [MIT's solution, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf)
was retrieved and corroborates the gauge transformation, electric-potential
rule, and invariant loop integral. The official-domain indexed passage from
[David Tong's notes, section 1.2.2, equation (1.18)](https://www.damtp.cam.ac.uk/user/tong/aqm/solid1.pdf)
corroborates the symmetric-gauge formula. Direct retrieval of that Cambridge PDF
again failed, so this audit does not claim to have read its full contents.

## Findings and corrections

No new physics error was found. The curls, gradient sign, midpoint, circulation,
units, and positive/zero/negative-field descriptions are correct under the
stated assumptions. The explanation already distinguishes the gauge function
from electric scalar potential, holds the latter fixed, and uses smooth,
single-valued functions and spatially constant slider values. No mathematical
or rendering implementation change was warranted.

The three quoted passages match the supplied reference wording. Their publication
metadata was not independently established; no author, book title, edition, or
page number should be inferred from the corroborating MIT citation. The reference
page now makes this distinction explicit without changing the quotations.

A separate documentation claim was incorrect at the time of this audit:
`gh repo view --json nameWithOwner,isPrivate,url` reported `isPrivate: false`
for `BurnyCoder/magnetic-field-gauge-transformation`, while README and the
acceptance record described it as private. Those descriptions were corrected.
The standing private-visibility instruction remains an intended policy, not
proof of a live setting. This audit did not change repository access or determine
when or why the visibility changed. The acceptance record now links the experiment
index instead of calling an older audit the latest validation.

## Experiments and measured results

- `uv run pytest tests/test_fields.py -q`: 22 tests passed in 0.20 seconds.
- `uv run pytest -q`: 37 tests passed in 16.51 seconds. This includes complete
  generation for b=-1,0,1 and Chromium slider checks at 736, 360, and 320 pixels.
- All six generation/browser logs from the full run, between 12:43:46 and
  12:44:01 UTC, were inspected and contained no warnings or errors.
- The committed scientific figure and the newly captured 320-pixel browser
  view were visually inspected. Their field directions agree with the algebra.
- `uv run gauge-fields` completed at 12:45:50 UTC without warnings or errors;
  its 15 gauge/strength cases had zero measured residuals. The updated PDF
  contains this audit. The PNG, both HTML exports, and validation JSON remained
  byte-for-byte unchanged; the figure PDF has one page and no raster images.

## Learning and review

An explanation can be mathematically correct while adjacent claims about its
sources or repository state need qualification. Source fidelity, publication
attribution, mathematical proof, and finite numerical tests establish different
things. Existing checks were sufficient for this prose-only audit; adding new
physics code or tests that repeat the formulas would not strengthen the result.

One review pass checked correctness, source support, security, reliability,
maintainability, and scope. No credentials were added, no dependencies changed,
and the shared-sample architecture remains intact. Browser evidence is limited
to Chromium; publication provenance and the Cambridge full-document retrieval
remain explicit limits.
