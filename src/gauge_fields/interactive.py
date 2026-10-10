"""Global: render the same samples in a small browser visualization.

Local: embed numeric data in a hand-authored fragment and its portable wrapper.
Sources: https://docs.python.org/3/library/importlib.resources.html and
https://docs.python.org/3/library/json.html .
"""

import json  # Serialize finite numeric samples, never arbitrary executable code.
import logging  # Keep export progress in the pipeline's timestamped evidence.
from importlib.resources import files  # Resolve packaged templates without relying on an absolute checkout path.


def export_interactive(samples, output):
    """Global: synchronize the static and interactive views; local: inject one compact sample payload."""
    count = samples.x.shape[0]  # Infer grid dimensions from the shared calculation output.
    points = [  # Include only the endpoint components the browser needs to interpolate.
        {"x": float(samples.x[row, column]), "y": float(samples.y[row, column]), "first": samples.first[row, column, :2].tolist(), "second": samples.second[row, column, :2].tolist(), "magnetic": row % 2 == 0 and column % 2 == 0}  # Preserve coordinates and the static renderer's B-marker subsampling.
        for row in range(count) for column in range(count)  # Flatten in deterministic row-major order.
    ]
    payload = {"b": samples.b, "limit": samples.limit, "extent": float(abs(samples.x).max()), "scale": samples.scale, "points": points}  # Reuse the exact static arrow scale and padded bounds.
    assets = files("gauge_fields")/"assets"  # Locate package resources portably in a clone or installed wheel.
    fragment = (assets/"view.html").read_text(encoding="utf-8").replace("__SAMPLED_FIELDS__", json.dumps(payload, separators=(",", ":"), allow_nan=False))  # Only numbers enter the JSON script element.
    (output/"exercise-3-gauge.html").write_text(fragment, encoding="utf-8")  # Save the conversation-ready fragment.
    page = (assets/"page.html").read_text(encoding="utf-8").replace("__FRAGMENT__", fragment)  # Reuse the fragment for an ordinary browser.
    (output/"exercise-3-interactive.html").write_text(page, encoding="utf-8")  # A clone can open this file directly, without a server.
    logging.info("Exported interactive view and inline fragment to %s", output)  # Identify both completed presentations.
