# Exercise 3: different potentials, the same magnetic field

This project reproduces the supplied exercise as scientific figures. An interactive
gauge transformation is being added. The method is to calculate the
two vector potentials on a shared grid, verify their common curl, and render the
same samples in both presentations.

Development uses Python 3.12 and uv with a project-local virtual environment.
Run `uv sync --locked`, then `uv run gauge-fields` to generate the PNG, vector PDF,
and numerical validation in `outputs/`. Run `uv run pytest` to verify the model.
Copy `.env.example` to `.env` to change plotting parameters. Full documentation
will accompany the interactive implementation.
