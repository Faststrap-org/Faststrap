# HTMX Compatibility & Migration Guide

Faststrap is designed around HTMX as its primary engine for reactive, zero-JavaScript user interfaces. Starting with Faststrap v0.8.2 and FastHTML 0.14.x, Faststrap provides a dual-engine architecture supporting both **HTMX 2.x** and **HTMX 4.0.0**.

---

## The Dual-Engine Strategy

| Engine | Status | Default | Notes |
| --- | --- | --- | --- |
| **HTMX 2.0.7** | Certified Stable | **Yes** | 100% backwards-compatible, production certified across all Faststrap components. |
| **HTMX 4.0.0** | Forward Support (Opt-In) | No | Next-generation runtime featuring security isolation, native morphing, and modernized events. |

Faststrap guarantees that your existing apps will continue running smoothly on HTMX 2.0.7 without breaking changes. At the same time, you can opt into HTMX 4 today with a single parameter.

---

## Configuring HTMX in Faststrap

You configure HTMX behavior when calling `add_bootstrap()` on your FastHTML app:

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()

# Standard setup (uses certified HTMX 2.0.7 default)
add_bootstrap(app)
```

### Opting into HTMX 4

To enable HTMX 4, pass `htmx4=True`:

```python
add_bootstrap(
    app,
    htmx4=True,
    htmx_compat=True,                          # Optional: load HTMX 2.x compatibility extension
    allow_extensions=["response-targets", "sse"], # Whitelist allowed extensions (HTMX 4 security model)
)
```

### Configuration Options

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `htmx4` | `bool | None` | `None` | Explicitly enable or disable HTMX 4. When `None`, auto-detects if FastHTML app is configured with `htmx4=True`. |
| `htmx_compat` | `bool` | `False` | When `htmx4=True`, loads the official HTMX 4 2.x compatibility extension (`hx-compat`) to preserve legacy 2.x event and attribute naming. |
| `allow_extensions` | `list[str] | None` | `None` | Whitelist of extension names allowed to execute under HTMX 4's strict extension isolation policy. Configures `htmx.config.allowExtensions`. |
| `hx_config` | `dict[str, Any] | None` | `None` | Arbitrary key-value dictionary serialized into `htmx.config` via a `<meta name="htmx-config">` tag. |
| `hx_version` | `str | None` | `None` | Override the HTMX CDN version string directly (e.g. `"2.0.7"` or `"4.0.0"`). |

---

## The Cross-Version JavaScript Bridge (`FaststrapHtmx`)

HTMX 4 introduces modernized event lifecycles (such as `htmx:swap` replacing certain behaviors of `htmx:afterSwap`, and strict node processing).

Faststrap ships a lightweight client-side bridge (`faststrap-htmx.js`) that automatically loads ahead of component scripts. This bridge abstracts version differences:

```javascript
// Register a callback that runs whenever new content is swapped into the DOM,
// regardless of whether HTMX 2 or HTMX 4 is running:
FaststrapHtmx.onSwap(function(targetElement) {
    console.log("DOM updated:", targetElement);
});

// Check which engine is active:
if (FaststrapHtmx.isV4()) {
    console.log("Running HTMX 4.x runtime");
}

// Process newly added dynamic nodes:
FaststrapHtmx.process(myContainer);
```

All Faststrap internal components (Bootstrap Toasts, ModernToast, Chart.js, GSAP animations, SplitPane, and OTP inputs) use this bridge, guaranteeing identical behavior across both engines.

---

## Server-Side Patterns & Presets

Faststrap provides specialized presets designed to take advantage of multi-element updates and modern swap behaviors.

### 1. Multi-Target Updates (`multi_response`)

Under HTMX 4, multi-target swaps and OOB (out-of-band) patterns require explicit element boundaries. Faststrap provides `multi_response` to bundle a primary response with one or more out-of-band updates and an optional toast:

```python
from faststrap.presets import multi_response
from faststrap import Card, StatCard, Badge

@app.post("/items/update")
def update_item():
    primary = Card("Item updated successfully!")
    stat_oob = StatCard(title="Active Items", value=42, id="sidebar-stat", hx_swap_oob="true")
    badge_oob = Badge("Updated", id="header-status", hx_swap_oob="outerHTML:#header-status")

    return multi_response(
        primary,
        stat_oob,
        badge_oob,
        toast=("Item status updated", "success"),
    )
```

### 2. Native Morph Polling in `DataTable`

HTMX 4 supports native DOM morphing, while HTMX 2 uses the `idiomorph` extension. Faststrap's `DataTable` component abstracts this:

```python
from faststrap import DataTable

DataTable(
    data=my_live_records,
    columns=["id", "name", "status"],
    poll_interval=5,      # Poll every 5 seconds
    poll_morph=True,      # Smoothly morph DOM changes without losing input focus or scroll position
    poll_endpoint="/api/table-feed",
)
```

When `poll_morph=True`, the component sets `hx_swap="morph"` (or `morph:outerHTML`), preserving cell focus, expanded details, and scroll state across refreshes.

### 3. SSE Engines in `SSETarget`

`SSETarget` allows choosing between standard browser EventSource or HTMX SSE extensions:

```python
from faststrap import SSETarget

# Default: lightweight native EventSource
SSETarget("/live-feed", sse_swap="notification", engine="eventsource")

# HTMX SSE extension engine
SSETarget("/live-feed", sse_swap="notification", engine="htmx")
```

### 4. Optimistic Pending State in `LoadingButton`

HTMX 4 provides optimistic UI updates with `hx-pending`. Faststrap's `LoadingButton` supports this via the `pending` parameter:

```python
from faststrap.presets import LoadingButton

LoadingButton(
    "Submit Application",
    hx_post="/submit",
    pending="Submitting your application...",
    spinner=True,
)
```

---

## Roadmap Note: `LiveBind` (P3)

HTMX 4 introduces experimental two-way bindings via `hx-live`. Faststrap's architectural review evaluated a `LiveBind` abstraction and determined that the specification is actively evolving across early 4.0 releases.

To ensure stability for production applications, **`LiveBind` is deferred to HTMX 4.1+**. Faststrap will introduce a dedicated reactive binding helper once the underlying HTMX 4.1 contract stabilizes.
