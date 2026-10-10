# Experiment 5 — independently recheck the explanation

Date: 2026-10-10 (Europe/Berlin).

## Question and method

Does the current explanation contain incorrect equations, unsupported physical
claims, or invented source attributions? We checked each mathematical step
against the implemented field functions and independently differentiated the
potentials and connecting scalar. We inspected the square's directed edge
contributions, parameter assumptions, dimensional units, and the relation
between the stated arrow scale and both renderers.

[MIT's derivation, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf)
confirms the electromagnetic gauge transformation and invariant closed-loop
integral. The official-domain indexed excerpt of [David Tong's Cambridge notes,
section 1.2.2, equation (1.18)](https://www.damtp.cam.ac.uk/user/tong/aqm/solid1.pdf)
independently identifies the midpoint potential as the symmetric gauge. Direct
PDF retrieval was unavailable during this check; the excerpt, not a full reading
of that document, is the corroborating evidence. Only that mathematical
definition is used; the showcase remains classical.

## Findings and changes

The core derivation was already correct. No field formula or visualization
needed to change. Three statements were made more precise:

- The zero-field scalar retains its arbitrary additive constant; zero everywhere
  specifically refers to the displayed choice of that constant.
- Translating a circulation square can change individual side contributions,
  but does not necessarily change each of them. The total remains invariant.
- Matching magnetic fields alone does not establish matching electric fields,
  even for static potentials. The showcase holds the electric scalar potential
  fixed, which makes its static gauge choices electromagnetically equivalent.

We also defined the position vector used in the midpoint formula and specified
the axis of rotational symmetry. Reference quotations remain unchanged; no
new book attribution or unsupported physical claim was found in the explanation.

## Verification and limits

`uv run pytest tests/test_fields.py -q` passed all 22 mathematical tests in
0.20 seconds. They cover both field signs and zero, intermediate gauges,
independent finite differences, an off-center circulation loop, and the
additive scalar constant. These checks support the implementation; direct
differentiation establishes the exact identities. This follow-up changes prose
and references only, so the prior browser results remain the relevant interface
evidence rather than a newly claimed browser run.

The complete generation command succeeded at 12:37:52 UTC with no warnings or
errors in its log. Its 15 gauge/strength cases again had zero measured residuals.
The updated eight-page PDF includes this audit; the plot and interactive file
contents were checked to be unchanged.
