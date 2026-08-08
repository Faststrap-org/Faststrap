# Debounce

`Debounce` returns a formatted HTMX trigger string that adds a delay to an event. It is a convenience helper that ensures consistent `delay:Xms changed` trigger strings across your application.

Use `Debounce` with `hx-trigger` to debounce input events, preventing excessive server requests while the user is typing.

---

## Quick Start

```python
from faststrap import Debounce, Input

Input(
    placeholder="Search...",
    name="q",
    hx_get="/search",
    hx_target="#results",
    hx_trigger=Debounce(300),
)
```

---

## Visual Examples & Use Cases

### 1. Default Debounce (300ms)

```python
Debounce()
# Returns: "input changed delay:300ms"
```

### 2. Custom Delay

```python
Debounce(delay=500)
# Returns: "input changed delay:500ms"
```

### 3. Custom Trigger Event

```python
Debounce(trigger="keyup", event="keyup")
# Returns: "keyup changed delay:300ms"
```

### 4. Used with ActiveSearch

```python
from faststrap import ActiveSearch

ActiveSearch(
    endpoint="/api/search",
    target="#results",
    debounce=500,
)
# Internally uses: hx-trigger="keyup changed delay:500ms"
```

---

## Practical Functionality

### 1. Search Input with Debounce

```python
from faststrap import Input

Input(
    type="search",
    placeholder="Search users...",
    name="q",
    hx_get="/api/users/search",
    hx_target="#user-list",
    hx_trigger=Debounce(300),
    cls="form-control",
)
```

### 2. Custom Debounce for Slow Endpoints

```python
Input(
    placeholder="Type to search...",
    name="q",
    hx_get="/api/slow-search",
    hx_target="#results",
    hx_trigger=Debounce(800),
)
```

### 3. Debounce with Keyup Trigger

```python
Input(
    placeholder="Filter...",
    name="filter",
    hx_get="/api/filter",
    hx_target="#results",
    hx_trigger=Debounce(200, trigger="keyup"),
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `delay` | `int` | `300` | Milliseconds to wait after the event before sending the request. |
| `trigger` | `str` | `"changed"` | Base HTMX trigger event (e.g. `"changed"`, `"keyup"`). |
| `event` | `str` | `"input"` | Event to listen for (e.g. `"input"`, `"keyup"`). |
| `**kwargs` | `Any` | `{}` | Reserved for future extension. |

---

## Return Value

`Debounce` returns a string suitable for use with `hx-trigger`:

```
"{event} {trigger} delay:{delay}ms"
```

For example, `Debounce(300)` returns `"input changed delay:300ms"`.

---

## API Reference

::: faststrap.presets.interactions.Debounce
    options:
        show_source: true
        heading_level: 4
