"""Global: the single generation entry point; local: orchestrate clearly named phases.

Source: https://docs.python.org/3/library/logging.html .
"""

import logging  # Keep failures in the same timestamped run evidence as successful phases.

from gauge_fields.config import load_settings  # Resolve one shared configuration.
from gauge_fields.fields import sample_fields  # Calculate each field once.
from gauge_fields.interactive import export_interactive  # Keep browser rendering details out of the orchestrator.
from gauge_fields.logging_setup import start_logging  # Initialize evidence before configuration can fail.
from gauge_fields.report import export_report  # Assemble experiment prose without duplicating it in the entry point.
from gauge_fields.static_plot import export_static  # Delegate plot details to the renderer.
from gauge_fields.verification import verify_fields  # Verify physics independently before rendering.


def main() -> None:
    """Global: regenerate the deliverables; local: configure, verify, sample, and export in order."""
    start_logging()  # Capture all subsequent progress, warnings, and errors.
    try:  # Preserve useful diagnostics if any generation phase fails.
        settings = load_settings()  # Validate optional .env and environment settings.
        settings.output.mkdir(parents=True, exist_ok=True)  # Create only the configured artifact destination.
        logging.info("Configuration: b=%g extent=%g points=%d output=%s", settings.b, settings.extent, settings.points, settings.output)  # Record only nonsecret plotting parameters.
        verify_fields(settings.output)  # Prevent misleading exports if the implemented identities are wrong.
        samples = sample_fields(settings)  # Share a single coordinate grid and common arrow scale.
        export_static(samples, settings.output)  # Produce the PNG and vector PDF.
        export_interactive(samples, settings.output)  # Reuse exactly those samples for the slider.
        export_report(settings.output)  # Attach the documented experiment methodology and results as a PDF.
        logging.info("Generation completed successfully")  # A final marker makes complete runs distinguishable from interrupted runs.
    except Exception:  # Include the real traceback without silently claiming success.
        logging.exception("Generation failed")  # File and console handlers receive the same diagnostic.
        raise  # Preserve a nonzero process exit status for callers and tests.
