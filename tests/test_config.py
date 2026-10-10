"""Global: protect reproducible configuration; local: check precedence and unsupported numeric inputs.

Sources: https://bbc2.github.io/python-dotenv/ and
https://docs.pytest.org/en/stable/how-to/monkeypatch.html .
"""

import pytest  # Parameterize invalid cases without repeating test logic.

from gauge_fields.config import Settings, load_settings  # Exercise the real configuration boundary.


@pytest.mark.parametrize("values", [{"b": float("nan")}, {"b": float("inf")}, {"b": 101}, {"extent": 0}, {"extent": 11}, {"points": 4}, {"points": 12}, {"points": 27}])  # Cover degenerate, nonfinite, and unreadable settings.
def test_invalid_settings(values):
    """Global: reject unusable plots; local: require a clear configuration error."""
    with pytest.raises(ValueError, match="GAUGE_"):  # Errors should identify the setting the user can fix.
        Settings(**values)  # All configuration paths share the dataclass's validation.


def test_environment_overrides_only_current_directory_file(tmp_path, monkeypatch):
    """Global: make cloned runs predictable; local: verify environment-over-.env precedence."""
    monkeypatch.chdir(tmp_path)  # Avoid reading or altering the user's actual .env file.
    for key in ("GAUGE_B", "GAUGE_EXTENT", "GAUGE_POINTS", "GAUGE_OUTPUT"):  # Clear only this project's configuration namespace.
        monkeypatch.delenv(key, raising=False)  # Defaults should not depend on the developer's shell settings.
    (tmp_path/".env").write_text("GAUGE_B=-2\nGAUGE_EXTENT=3\n", encoding="utf-8")  # Model a user's local plotting preferences.
    monkeypatch.setenv("GAUGE_B", "1")  # An explicit command-line environment override must win.
    settings = load_settings()  # Exercise the actual parser and validation path together.
    assert settings.b == 1 and settings.extent == 3 and settings.points == 13  # Combine environment, file, and default values.
