# Exercise 3: reproducible gauge-transformation experiments

## Abstract

The question is whether two visibly different vector potentials represent the
same uniform magnetic field. The supplied exercise gives A=(0,bx,0) and
A′=(-by,0,0). Their difference is the gradient of s=-bxy+C; both curls equal
(0,0,b). An interpolating family Aλ=A+λ∇s preserves this curl and all closed-loop
circulation. Exact differentiation establishes the result; numerical experiments
and browser checks test whether the implementation represents it faithfully.

## Methodology and evidence

We transcribed the screenshot, derived the connecting scalar, tested the
mathematics before implementation, and reused one sampled grid in both
renderers. The experiments below document the hypothesis, evidence, problems,
and corrections without treating finite numerical samples as a proof.

- [Experiment 1](experiment-01-mathematics.md): exploratory central-difference check.
- [Experiment 2](experiment-02-static.md): test-driven physics and scientific exports.
- [Experiment 3](experiment-03-browser.md): native slider interaction and responsive rendering.

The PDF companion assembles this summary, the individual experiment records,
and the generated four-panel figure from their existing sources. It is a local
reproducibility report, not a claim of new experimental physics.

## Conclusion and limitations

Gauge freedom changes the vector potential while preserving the magnetic field.
Here b is constant and the gauge function is time-independent and smooth over
all space. Coordinates and magnitudes use illustrative units. The plotted slice
contains all spatial dependence because the fields have no z dependence. The
browser checks cover Chromium; the interactive renderer needs access to its
pinned D3 CDN. The scientific PNG/PDF and the algebra can be read offline.

The primary source is the supplied screenshot. Independent corroboration is
[MIT's electromagnetism gauge and circulation derivation, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf).
