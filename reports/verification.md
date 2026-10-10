# Acceptance and review record

Date: 2026-10-10 (Europe/Berlin). This record describes the implemented project
and the checks performed in the initial implementation. The subsequent
[factual audit](experiment-04-factual-audit.md) records the latest validation.

## Verified results

- `uv run pytest -q`: 37 tests passed in 15.84 seconds after the mathematical,
  rendering, configuration, report, and browser changes. The suite generates
  complete artifacts independently for b=-1,0,1.
- `uv run gauge-fields`: successful default generation at 12:05:05 UTC. The
  generator's 15 gauge/strength cases use 289 grid points each; maximum absolute
  curl, gradient, and circulation residuals were all zero at tolerance 1e-10.
- Twenty timestamped generation/browser logs inspected at this checkpoint
  contained no WARNING, ERROR, or browser error entries. Earlier expected
  test-development failures are documented in the experiment records.
- Scientific PNG and vector PDF inspected; the figure PDF has one page and
  no raster images. The companion's five initial pages contain selectable
  experiment text and a figure appendix. This acceptance record adds a sixth
  page when the companion is regenerated.
- Browser behavior checked through native Home, End, and ArrowRight keys.
  B geometry remains unchanged at the endpoints and midpoint. The zero-field
  case correctly has no arrows. Layouts at 736, 360, and 320 pixels retain
  square plotting frames and have no horizontal overflow. Desktop and phone
  browser captures were inspected, as was the PDF's first rendered page.

## One-pass code and documentation review

Correctness: checked the signs in A′−A, coordinate/derivative ordering, contour
behavior at the scalar saddle, and the difference between a gauge parameter
and physical time. Reference passages are clearly distinguished from added prose.

Security: numeric-only serialized data is embedded in the visualization; no
credentials or user-provided executable markup enter it. The repository is
private, and .env, .venv, raw logs, and local browser captures are ignored.
External browser loading is limited to the version-pinned D3 script.

Maintainability and design: the thin pipeline delegates to configuration,
model, verification, two renderers, and a report exporter. The browser reuses
the same endpoint samples; the PDF reads existing Markdown instead of a second
copy of report prose. The architecture, setup, settings, and outputs in README
were checked against code and observed runs.

Reliability: configuration rejects nonfinite and unusable values, the zero
field avoids normalization errors, failures preserve nonzero exit status and
logged tracebacks, and a missing CDN yields a visible error state. Exact
derivation and independent finite differences/line integrals provide different
forms of evidence; they are not presented as interchangeable proofs.

## Review corrections and limits

Git initially treated the ReportLab file as text because its initial bytes did
not trigger binary detection, producing irrelevant PDF whitespace diagnostics.
Explicit PDF/PNG binary attributes fix review and line-ending handling. PDF
links to individual experiments now resolve to the private repository, so they
remain meaningful when the PDF is downloaded separately. These are small
review corrections; the prior physics and browser results still apply.

The interactive view was verified in a separate Chromium instance, not in the
unavailable in-app browser connection. Other browser engines and the host's
optional saved-state integration were not separately exercised. The default
layout is manually inspected; parameter boundary checks do not claim exhaustive
visual review of every possible configuration. Runtime dependencies, supported
configuration ranges, and the CDN requirement are documented in README.
