"""Global: verify usable exports; local: inspect artifact content and their shared numeric contract.

Sources: https://pypdf.readthedocs.io/en/stable/user/extract-text.html and
https://docs.python.org/3/library/json.html .
"""

import json  # Read the exact data embedded in the browser artifact.
import re  # Isolate the explicitly identified JSON element, not arbitrary JavaScript.

import numpy as np  # Compare sampled endpoints with the physics model.
from PIL import Image  # Check image integrity through the same established library Matplotlib uses.
from pypdf import PdfReader  # Inspect the scientific PDF without relying only on a filename.

from gauge_fields.fields import potential  # Establish agreement between the public model and interactive samples.


def test_generated_artifacts(generated):
    """Global: deliver genuine files; local: validate image, vector PDF, JSON, and endpoint samples."""
    output, b = generated  # Inspect one complete user-style generation run.
    with Image.open(output/"gauge-transformation-fields.png") as image:  # Decode the exported image to catch corruption.
        assert image.size == (1980, 1800)  # The intended four-panel figure has sufficient resolution.
        image.verify()  # Ask Pillow to verify the entire encoded stream.
    document = PdfReader(output/"gauge-transformation-fields.pdf")  # Verify the static export is a real PDF.
    assert len(document.pages) == 1 and len(document.pages[0].images) == 0  # The requested scientific PDF stays vector-based.
    validation = json.loads((output/"validation.json").read_text())  # Read actual residuals rather than a success flag.
    assert max(validation["maximum_absolute_errors"].values()) <= validation["tolerance"]  # Enforce the documented numeric standard.
    fragment = (output/"gauge-transformation.html").read_text()  # Inspect the inline artifact produced by the same command.
    match = re.search(r'<script type="application/json" id="gauge-samples">(.*?)</script>', fragment, re.S)  # Select only numeric embedded samples.
    assert match, "Missing shared sample data"  # A view without data cannot reproduce the model.
    data = json.loads(match.group(1))  # JSON parsing rejects malformed payloads before browser interaction.
    assert data["b"] == b and len(data["points"]) == 169  # Match the full 13 by 13 grid and configured field strength.
    for point in data["points"]:  # Compare every endpoint, not a single hand-picked arrow.
        np.testing.assert_allclose(point["first"], potential(point["x"], point["y"], b, 0)[:2])  # The first potential remains the slider origin.
        np.testing.assert_allclose(point["second"], potential(point["x"], point["y"], b, 1)[:2])  # The second potential remains the slider destination.
    assert "__SAMPLED_FIELDS__" not in fragment and len(fragment.encode()) < 1_000_000  # Ensure substitution and the inline size contract.
    report = PdfReader(output/"gauge-transformation-report.pdf")  # The companion remains usable without optional local experiment records.
    text = "\n".join(page.extract_text() for page in report.pages)  # Inspect every page, including the figure appendix.
    assert "Generated field comparison" in text  # Every clone can generate the figure; separate report tests cover optional Markdown.
