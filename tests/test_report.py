"""Global: keep PDF generation usable when experiment records stay local.

Local: exercise absent, empty, partial, and complete report directories independently.
Sources: https://docs.pytest.org/en/stable/how-to/monkeypatch.html and
https://pypdf.readthedocs.io/en/stable/user/extract-text.html .
"""

import pytest  # Run the same observable PDF contract for each local report layout.
from PIL import Image  # Supply a real image without repeating the field-generation pipeline.
from pypdf import PdfReader  # Inspect actual pages and selectable text in the generated companion.

from gauge_fields.report import export_report  # Exercise the existing report phase directly.


@pytest.mark.parametrize("records", [None, (), ("experiment-01",), ("summary", "experiment-01", "experiment-02", "verification")])  # Cover a clone, an empty folder, a missing summary, and a complete record set.
def test_optional_local_reports(tmp_path, monkeypatch, records):
    """Global: avoid a dependency on ignored files; local: verify inclusion, ordering, and no blank pages."""
    monkeypatch.chdir(tmp_path)  # Resolve reports in an isolated working directory, never the user's evidence.
    if records is not None:  # None specifically models a fresh clone without a reports directory.
        directory = tmp_path/"reports"  # Keep synthetic evidence beside the isolated generation destination.
        directory.mkdir()  # An empty tuple exercises an existing folder with no Markdown records.
        for name in reversed(records):  # Create records in reverse order to check the PDF's stable reading order.
            (directory/f"{name}.md").write_text(f"# {name}\n\nLocal evidence.\n", encoding="utf-8")  # Give each source a unique, extractable heading.
    Image.new("RGB", (100, 100), "white").save(tmp_path/"gauge-transformation-fields.png")  # Supply the same image path the static phase produces.
    export_report(tmp_path)  # Generate the real PDF with whichever optional records exist.
    document = PdfReader(tmp_path/"gauge-transformation-report.pdf")  # Read the complete output rather than checking file existence.
    headings = [page.extract_text().strip().split("\n")[0] for page in document.pages]  # An unwanted blank page remains visible as an empty heading.
    assert headings == [*(records or ()), "Generated field comparison"]  # Include every available record before exactly one figure page.
