"""Server-Sent Events (SSE) helpers."""

from __future__ import annotations

import json
from collections.abc import AsyncIterable, AsyncIterator, Iterable, Iterator
from typing import Any

from starlette.responses import StreamingResponse


def sse_event(
    data: Any,
    *,
    event: str | None = None,
    event_id: str | None = None,
    retry: int | None = None,
) -> dict[str, Any]:
    """Build a normalized SSE event payload dict."""
    return {
        "data": data,
        "event": event,
        "id": event_id,
        "retry": retry,
    }


def sse_comment(text: str = "keep-alive") -> dict[str, Any]:
    """Build a comment-only SSE payload (used as a keep-alive ping)."""
    return {"comment": text}


def _format_sse_event(payload: dict[str, Any]) -> str:
    if "comment" in payload:
        comment = payload.get("comment", "")
        lines = str(comment).splitlines() or [""]
        return "\n".join(f": {line}" for line in lines) + "\n\n"

    data = payload.get("data", "")
    event = payload.get("event")
    event_id = payload.get("id")
    retry = payload.get("retry")

    if isinstance(data, (dict, list, tuple)):
        data_str = json.dumps(data, default=str)
    else:
        data_str = "" if data is None else str(data)

    lines = data_str.splitlines() or [""]
    parts: list[str] = []
    if event:
        parts.append(f"event: {event}")
    if event_id:
        parts.append(f"id: {event_id}")
    if retry is not None:
        parts.append(f"retry: {int(retry)}")
    parts.extend(f"data: {line}" for line in lines)
    return "\n".join(parts) + "\n\n"


def _iter_sse(events: Iterable[Any]) -> Iterator[str]:
    for item in events:
        payload = item if isinstance(item, dict) else {"data": item}
        yield _format_sse_event(payload)


async def _aiter_sse(events: AsyncIterable[Any]) -> AsyncIterator[str]:
    async for item in events:
        payload = item if isinstance(item, dict) else {"data": item}
        yield _format_sse_event(payload)


def SSEStream(
    events: Iterable[Any] | AsyncIterable[Any],
    *,
    headers: dict[str, str] | None = None,
) -> StreamingResponse:
    """Create a StreamingResponse for Server-Sent Events (SSE).

    Args:
        events: Iterable or async iterable of SSE payloads.
        headers: Optional extra headers.

    Returns:
        StreamingResponse configured for text/event-stream.
    """
    base_headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "X-Accel-Buffering": "no",
    }
    if headers:
        base_headers.update(headers)

    body_iter: Iterable[str] | AsyncIterator[str]
    if isinstance(events, AsyncIterable):
        body_iter = _aiter_sse(events)
    else:
        body_iter = _iter_sse(events)

    return StreamingResponse(body_iter, media_type="text/event-stream", headers=base_headers)
