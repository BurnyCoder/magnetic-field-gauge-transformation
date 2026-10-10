"""Global: verify the actual user interaction in a separate local Chromium browser.

Local: inspect keyboard changes, fixed B symbols, responsive geometry, and console errors.
Sources: https://playwright.dev/python/docs/library and
https://playwright.dev/python/docs/emulation .
"""

from datetime import UTC, datetime  # Name browser evidence by its real verification time.
from pathlib import Path  # Keep browser captures and console logs in ignored local evidence directories.

import pytest  # Keep browser checks selectable for users running only the math tests.
from playwright.sync_api import sync_playwright  # Use the documented browser automation library.


@pytest.fixture(scope="session")  # Launch one test browser for all generated field signs.
def browser():
    """Global: isolate testing from personal browser state; local: manage a headless Chromium lifecycle."""
    with sync_playwright() as playwright:  # Ensure Playwright's driver is cleaned up on success and failure.
        browser = playwright.chromium.launch()  # Use the explicitly installed Chromium headless shell.
        yield browser  # Share only the browser process, never page state.
        browser.close()  # Release the temporary test process after verification.


@pytest.mark.browser  # Allow fast physics-only runs without downloading a browser.
def test_slider_and_responsive_layout(generated, browser):
    """Global: protect the visual explanation; local: use native keys and compare the unchanged B drawing."""
    output, b = generated  # Open artifacts made by the real generation command.
    page = browser.new_page(viewport={"width": 1000, "height": 900})  # Begin with a desktop-sized presentation.
    failures, messages = [], []  # Collect both fatal JavaScript and ordinary console evidence.
    page.on("pageerror", lambda error: failures.append(str(error)))  # A visually plausible page can still have runtime failures.
    page.on("console", lambda message: messages.append(f"{datetime.now(UTC).isoformat()} {message.type}: {message.text}"))  # Capture real-time browser records with timestamps.
    page.goto((output/"gauge-transformation-interactive.html").as_uri())  # Test the portable file without a development server.
    slider = page.get_by_role("slider", name="Gauge position λ:")  # Use the control's accessible label as a user would.
    page.locator(".vector-mark").first.wait_for(state="attached")  # Wait for real chart marks instead of sleeping.
    magnetic = page.locator("[data-magnetic-field]").inner_html()  # Record the physical field before changing the gauge.
    initial = page.locator(".vector-mark").evaluate_all("nodes => nodes.map(n => n.getAttribute('d'))")  # Save the complete starting potential geometry.
    slider.focus()  # Native range key handling requires keyboard focus.
    slider.press("End")  # Select the second potential through actual keyboard interaction.
    assert page.locator("#gauge-value").text_content() == "1.00"  # Confirm the visible value, not only an internal variable.
    assert "Second potential" in page.locator("#gauge-state").inner_text()  # The endpoint label must follow the same state.
    ending = page.locator(".vector-mark").evaluate_all("nodes => nodes.map(n => n.getAttribute('d'))")  # Read what was actually drawn after the transformation.
    assert (ending != initial) if b else (ending == initial)  # Nonzero fields change gauge; all zero-field arrows remain absent.
    assert page.locator("[data-magnetic-field]").inner_html() == magnetic  # The physical field drawing must remain byte-for-byte unchanged.
    slider.press("Home")  # Return to the first potential.
    for _ in range(50):  # The step size is 0.01, so 50 native increments reach the midpoint.
        slider.press("ArrowRight")  # Exercise keyboard accessibility rather than injecting slider state.
    assert page.locator("#gauge-value").text_content() == "0.50"  # Verify the visible midpoint value.
    assert "Symmetric gauge" in page.locator("#gauge-state").inner_text()  # Expose the rotationally symmetric representation.
    assert page.locator("[data-magnetic-field]").inner_html() == magnetic  # Intermediate gauges must also preserve B.
    evidence = Path("test-results")  # Keep machine-specific browser captures out of version control.
    evidence.mkdir(exist_ok=True)  # Make the first verification run self-contained.
    for width in (736, 360, 320):  # Test the conversation width and two phone-sized layouts.
        page.set_viewport_size({"width": width, "height": 1100})  # Trigger the actual ResizeObserver and CSS breakpoint.
        page.wait_for_function("document.querySelector('.gauge-svg').viewBox.baseVal.width === document.querySelector('#potential-panel').getBoundingClientRect().width")  # Wait for geometry to match the resized panel.
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), "Horizontal overflow"  # Reject off-screen controls or panels.
        for geometry in page.locator("rect[data-chart-frame]").evaluate_all("nodes => nodes.map(n => ({width: n.getBBox().width, height: n.getBBox().height}))"):  # Explicitly serialize SVGRect getters as documented scalar dimensions.
            assert abs(geometry["width"]-geometry["height"]) < 1e-6  # Equal aspect must survive responsive resizing.
        if b == 1:  # One representative set is enough for manual visual inspection.
            page.screenshot(path=str(evidence/f"gauge-{width}.png"), full_page=True)  # Preserve what a user would see, including stacked panels.
    assert not failures, failures  # No uncaught JavaScript errors are acceptable.
    assert not any(" error:" in message for message in messages), messages  # Console errors must be investigated, not ignored.
    Path("logs").mkdir(exist_ok=True)  # Browser tests can also run independently of the generator.
    Path(f"logs/browser-{datetime.now(UTC):%Y%m%dT%H%M%S.%fZ}.log").write_text("\n".join(messages)+"\n", encoding="utf-8")  # Retain timestamped interaction evidence.
    page.close()  # Do not leak page state into the next field sign.
