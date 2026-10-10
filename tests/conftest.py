"""Global: exercise the real command as a user would; local: share isolated artifacts across checks.

Sources: https://docs.pytest.org/en/stable/how-to/fixtures.html and
https://docs.python.org/3/library/subprocess.html .
"""

import os  # Supply explicit plotting settings without altering the user's .env.
import subprocess  # Verify the real entry point instead of calling renderer internals.
from pathlib import Path  # Locate the checkout regardless of the invoking directory.

import pytest  # Share the complete generated artifacts across dependent tests.


@pytest.fixture(scope="session", params=[-1, 0, 1])  # Generate once for each important field orientation.
def generated(request, tmp_path_factory):
    """Global: validate the whole pipeline; local: run each field sign in an isolated output directory."""
    output = tmp_path_factory.mktemp(f"field-{request.param}")  # Never replace the committed default figures while testing.
    root = Path(__file__).resolve().parents[1]  # The CLI reads repository documentation from its normal working directory.
    environment = {**os.environ, "GAUGE_B": str(request.param), "GAUGE_EXTENT": "2", "GAUGE_POINTS": "13", "GAUGE_OUTPUT": str(output)}  # Keep test results independent of personal plotting overrides.
    run = subprocess.run(["uv", "run", "--no-sync", "gauge-fields"], cwd=root, env=environment, text=True, capture_output=True, timeout=90)  # Use the documented command and inspect all diagnostics.
    assert run.returncode == 0, run.stdout+run.stderr  # Surface the complete failure evidence if generation fails.
    assert "Generation completed successfully" in run.stdout  # Require the last pipeline phase, not just an early file.
    assert " WARNING " not in run.stdout and " ERROR " not in run.stdout, run.stdout  # Unexpected library diagnostics are part of the result.
    return output, request.param  # Consumers inspect actual generated files and the configured field strength.
