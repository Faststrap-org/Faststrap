# Accessibility Helpers

Faststrap now includes built-in accessibility primitives in `faststrap.accessibility`.

## Why this exists

- Reduce repeated a11y boilerplate in every app.
- Make keyboard and screen-reader support default.
- Keep APIs simple and composable with existing FastHTML/Faststrap components.

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

