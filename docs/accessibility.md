# Accessibility Helpers

Faststrap now includes built-in accessibility primitives in `faststrap.accessibility`.

## Why this exists

- Reduce repeated a11y boilerplate in every app.
- Make keyboard and screen-reader support default.
- Keep APIs simple and composable with existing FastHTML/Faststrap components.

## When to use these helpers

1. Any page with keyboard users in mind.
2. Dynamic pages that update content after interactions.
3. Dialog-like UI that must keep tab focus contained.
4. Icon-only controls that need screen-reader labels.

## Components

### `SkipLink`

```python
from faststrap import SkipLink

SkipLink(target="#main-content", text="Skip to content")
```

Use it near the top of your page so keyboard users can jump to main content immediately.

### `VisuallyHidden`

```python
from faststrap import VisuallyHidden

Button(
    Icon("x"),
    VisuallyHidden("Close dialog"),
)
```

Hides content visually while keeping it available to assistive technologies.

### `LiveRegion`

```python
from faststrap import LiveRegion

LiveRegion("Profile saved", politeness="polite")
```

Use for dynamic status updates that should be announced by screen readers.

### `FocusTrap`

```python
from faststrap import FocusTrap

FocusTrap(
    Input(name="email"),
    Button("Save"),
)
```

Wrap dialog-like content to constrain tab focus inside the container.

## Practical pattern for dynamic updates

```python
Div(
    Button("Save", hx_post="/save", hx_target="#status"),
    Div(id="status"),
    LiveRegion(id="a11y-status"),
)
```

Use route responses to update both visible status and the live region where appropriate.

## Recommended pattern

```python
from faststrap import *

app = FastHTML()
add_bootstrap(app)

@app.get("/")
def home():
    return Container(
        SkipLink("#main-content"),
        Div(
            H1("Dashboard"),
            id="main-content",
        ),
    )
```

## Accessibility notes

- `SkipLink` should appear early in the DOM.
- `LiveRegion` should be used for meaningful state changes (avoid noisy updates).
- `FocusTrap` is best for overlays, dialogs, and modal-like content.
