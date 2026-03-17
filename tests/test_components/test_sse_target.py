"""Tests for SSETarget component."""

from fasthtml.common import to_xml

from faststrap import SSETarget


def test_sse_target_default_attrs() -> None:
    target = SSETarget("Waiting...", endpoint="/api/stream")
    html = to_xml(target)

    assert 'data-fs-sse="true"' in html
    assert 'data-fs-sse-endpoint="/api/stream"' in html
    assert 'data-fs-sse-event="message"' in html
    assert 'data-fs-sse-swap="inner"' in html
    assert 'class="faststrap-sse-target"' in html
    assert 'aria-live="polite"' in html


def test_sse_target_customization() -> None:
    target = SSETarget(
        endpoint="/stream",
        event="stats",
        swap="append",
        target="#live",
        with_credentials=True,
        reconnect=False,
        retry=5000,
        cls="custom",
    )
    html = to_xml(target)

    assert 'data-fs-sse-endpoint="/stream"' in html
    assert 'data-fs-sse-event="stats"' in html
    assert 'data-fs-sse-swap="append"' in html
    assert 'data-fs-sse-target="#live"' in html
    assert 'data-fs-sse-credentials="true"' in html
    assert 'data-fs-sse-reconnect="false"' in html
    assert 'data-fs-sse-retry="5000"' in html
    assert "custom" in html
