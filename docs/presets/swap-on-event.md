# SwapOnEvent

`SwapOnEvent` renders a container that listens for a custom DOM event and triggers an HTMX swap. This is useful for coordinating UI updates from non-HTMX JavaScript code without coupling directly to HTMX internals.

!!! tip "Use Case"
    Use `SwapOnEvent` when you need to trigger an HTMX swap from a custom event dispatched by another script, a WebSocket message, or a browser API.

---

## Quick Start

```python
from faststrap import SwapOnEvent

SwapOnEvent(
    "Loading...",
    event_name="data:updated",
    target="#results",
    swap="innerHTML",
)
```

---

## Visual Examples & Use Cases

### 1. Basic Swap on Custom Event

```python
SwapOnEvent(
    "Initial content",
    event_name="my:update",
    target="#results",
    swap="innerHTML",
)
```

Trigger with JavaScript:
```javascript
document.dispatchEvent(new CustomEvent("my:update"));
```

### 2. Custom Swap Strategy

```python
SwapOnEvent(
    "<p>Replacement content</p>",
    event_name="refresh",
    target="this",
    swap="outerHTML",
)
```

### 3. With HTMX Endpoint

Set a data attribute to specify the endpoint:
```python
SwapOnEvent(
    "Loading...",
    event_name="refresh",
    target="#content",
    swap="innerHTML",
    data_fs_swap_endpoint="/api/content",
)
```

Then the JS runtime will call `htmx.ajax('GET', '/api/content', { target: '#content', swap: 'innerHTML' })`.

---

## Practical Functionality

### 1. WebSocket-Driven Updates

```python
from faststrap import SwapOnEvent

SwapOnEvent(
    "Waiting for updates...",
    event_name="ws:message",
    target="#live-feed",
    swap="beforeend",
)
```

```javascript
// In your WebSocket handler:
ws.onmessage = (event) => {
    document.dispatchEvent(new CustomEvent("ws:message", {
        detail: { data: event.data }
    }));
};
```

### 2. Browser API Integration

```python
SwapOnEvent(
    "Geolocation not set",
    event_name="faststrap:location:success",
    target="#location-display",
    swap="innerHTML",
    data_fs_swap_endpoint="/update-location",
)
```

### 3. Event-Driven Refresh

```python
SwapOnEvent(
    "Click refresh to update",
    event_name="manual-refresh",
    target="this",
    swap="innerHTML",
)
```

```javascript
// Trigger from console or another script:
document.dispatchEvent(new CustomEvent("manual-refresh"));
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Initial content to show before the swap. |
| `event_name` | `str` | `"faststrap:swap"` | Custom event name to listen for. |
| `target` | `str` | `"this"` | HTMX swap target selector. |
| `swap` | `str` | `"innerHTML"` | HTMX swap strategy (`innerHTML`, `outerHTML`, `beforeend`, etc.). |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

---

## API Reference

::: faststrap.presets.interactions.SwapOnEvent
    options:
        show_source: true
        heading_level: 4
