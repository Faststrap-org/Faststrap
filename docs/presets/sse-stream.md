# SSEStream

`SSEStream` builds a `text/event-stream` response for Server-Sent Events.

---

## Quick Start

```python
from faststrap.presets import SSEStream, sse_event

@app.get("/api/stream")
async def stream():
    async def gen():
        yield sse_event("Hello")
    return SSEStream(gen())
```

---

## Keep Alive Comments

```python
from faststrap.presets import sse_comment

yield sse_comment("keepalive")
```

---

## Pair With SSETarget

```python
from faststrap import SSETarget

SSETarget("Waiting...", endpoint="/api/stream")
```

---

## Security Notes

Use authentication and avoid streaming sensitive data to unauthenticated users. For production, disable proxy buffering.

---

## API Reference

::: faststrap.presets.streams.SSEStream
    options:
        show_source: true
        heading_level: 4
