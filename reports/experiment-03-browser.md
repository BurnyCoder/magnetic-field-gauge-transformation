# Experiment 3 — verify interaction and responsive presentation

Date: 2026-10-10 (Europe/Berlin).

## Question and hypothesis

Does moving the gauge slider visibly change A while leaving B unchanged, and
does the presentation remain readable on narrow screens? A native range input
and fixed sampled endpoints should support this without a backend.

## Method

The generator embeds its existing endpoint samples in the browser view.
Chromium opens the generated local file, uses End and Home keys to reach the
exercise endpoints, and applies 50 ArrowRight presses to reach λ=0.50.
The check compares all potential arrow paths and the complete B-symbol group.
It then inspects equal aspect and horizontal overflow at widths 736, 360,
and 320 pixels. Runs cover b=-1,0,1; zero field is expected to remain empty.
Browser screenshots and timestamped console logs are kept locally in ignored
evidence directories.

## Issues and corrections

The in-app browser connection rejected the Linux workspace before opening a
page, so verification uses a separate local Playwright Chromium session. It
does not attach to a personal browser. The first integrated run passed 25 tests
but failed three responsive checks because SVGRect's width/height getters were
not serialized by the test harness. All slider and B-invariance assertions had
already passed. Explicitly returning plain width/height properties repairs the
measurement, following [MDN's SVGRect documentation](https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getBBox)
and [Playwright's evaluation contract](https://playwright.dev/python/docs/evaluating).

## Result and learning

The browser-only rerun passed all three field-sign cases in 12.53 seconds;
the subsequent full run passed 37 tests. The [acceptance record](verification.md)
lists the inspected evidence. The failure showed why a test harness needs inspection as
well as the product. Independent endpoint data checks and native keyboard
interaction complement the geometric measurements. We keep the browser's field
formulas out of the renderer: interpolation reuses the Python-generated samples.

The only runtime network dependency is the pinned D3 script. If it cannot load,
the page presents an accessible error and disables its slider instead of
silently displaying an empty successful-looking chart.
