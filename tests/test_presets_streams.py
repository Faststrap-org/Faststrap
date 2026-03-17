"""Tests for SSE stream helpers."""

import pytest

from faststrap.presets import SSEStream, sse_comment, sse_event


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


def test_sse_stream_headers() -> None:
    response = SSEStream([sse_event("ping")])

    assert response.media_type == "text/event-stream"
    assert response.headers.get("Cache-Control") == "no-cache"
    assert response.headers.get("Connection") == "keep-alive"
    assert response.headers.get("X-Accel-Buffering") == "no"


@pytest.mark.anyio
async def test_sse_stream_formats_events() -> None:
    response = SSEStream(
        [
            sse_event("hello"),
            sse_event({"ok": True}, event="update", event_id="1", retry=5000),
            sse_comment("keepalive"),
        ]
    )

    chunks: list[str] = []
    async for chunk in response.body_iterator:
        if isinstance(chunk, (bytes, bytearray)):
            chunks.append(chunk.decode())
        else:
            chunks.append(str(chunk))

    body = "".join(chunks)
    assert "data: hello" in body
    assert "event: update" in body
    assert "id: 1" in body
    assert "retry: 5000" in body
    assert ": keepalive" in body
