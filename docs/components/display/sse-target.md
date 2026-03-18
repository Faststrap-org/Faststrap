# SSETarget

`SSETarget` connects a DOM container to an SSE endpoint and updates it as events arrive.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="border rounded p-3 text-muted">Waiting for updates...</div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import SSETarget

SSETarget(
    "Waiting for updates...",
    endpoint="/api/stream",
    swap="inner",
)
```
  </div>
</div>

---

## Swap Modes

Valid values:

- `inner`
- `outer`
- `before`
- `after`
- `append`
- `prepend`
- `replace`
- `text`

Use `text` if you want to update plain text only.

---

## Targeting Another Element

```python
SSETarget(
    "",
    endpoint="/api/stream",
    target="#status",
    swap="text",
)
```

---

## Connection Options

```python
SSETarget(
    "Live",
    endpoint="/api/stream",
    event="message",
    with_credentials=True,
    reconnect=True,
    retry=3000,
)
```

Use `retry` to suggest a reconnection delay (milliseconds).
For `swap="outer"` or `swap="replace"`, stream a single root element so the target can be rebound safely after replacement.

---

## Pair With SSEStream

```python
from faststrap.presets import SSEStream, sse_event

@app.get("/api/stream")
async def stream():
    async def gen():
        yield sse_event("Hello")
    return SSEStream(gen())
```

---

## Accessibility

`SSETarget` sets `aria-live="polite"` by default. Set `aria_live=None` to disable the live region.

---

## Security Notes

Protect your SSE endpoints with auth and rate limits. Do not stream sensitive data to unauthenticated clients. If you stream HTML fragments, treat them as trusted server-rendered content.

---

## API Reference

::: faststrap.components.display.sse_target.SSETarget
    options:
        show_source: true
        heading_level: 4
