# Accessibility Guide

Faststrap includes built-in accessibility components and follows Bootstrap's accessibility patterns. This guide covers how to build accessible FastHTML apps.

---

## Built-in Accessibility Components

### SkipLink

`SkipLink` renders a hidden "Skip to main content" link that appears on focus:

```python
from faststrap import SkipLink

SkipLink(target="#main-content")
```

### LiveRegion

`LiveRegion` creates an ARIA live region for dynamic content updates:

```python
from faststrap import LiveRegion

LiveRegion(
    "3 new messages",
    aria_live="polite",
    aria_atomic="true",
)
```

Aria live values:
- `"polite"` — announces when the user is idle
- `"assertive"` — announces immediately
- `"off"` — disables announcements

### VisuallyHidden

`VisuallyHidden` renders content that is visible to screen readers but hidden visually:

```python
from faststrap import VisuallyHidden

Button(
    "Close",
    aria_label="Close dialog",
)
VisuallyHidden("Dialog closed")
```

### FocusTrap

`FocusTrap` constrains keyboard focus within a modal or dialog:

```python
from faststrap import FocusTrap

FocusTrap(
    Modal(
        Modal.Header("Confirm Action"),
        Modal.Body("Are you sure?"),
        Modal.Footer(
            Button("Cancel", variant="secondary"),
            Button("Confirm", variant="primary"),
        ),
    ),
)
```

---

## ARIA Patterns with Faststrap

### Modals

```python
from faststrap import Modal, ModalHeader, ModalBody, ModalFooter

Modal(
    ModalHeader("Delete Item", close_button=True),
    ModalBody("Are you sure you want to delete this item?"),
    ModalFooter(
        Button("Cancel", variant="secondary", data_bs_dismiss="modal"),
        Button("Delete", variant="danger", hx_delete="/items/1", hx_target="#item-list"),
    ),
    id="delete-modal",
    aria_labelledby="delete-modal-label",
)
```

### Alerts

```python
from faststrap import Alert, VisuallyHidden

Alert(
    "Form submitted successfully!",
    variant="success",
    role="status",
    VisuallyHidden("Success"),
)
```

### Navigation

```python
from faststrap import Navbar, NavbarBrand, NavbarNav, NavbarItem

Navbar(
    NavbarBrand("My App", href="/"),
    NavbarNav(
        NavbarItem("Home", href="/", active=True),
        NavbarItem("About", href="/about"),
        NavbarItem("Contact", href="/contact"),
    ),
    aria_label="Main navigation",
)
```

---

## Keyboard Navigation

Faststrap components support keyboard interaction:

| Component | Keys | Action |
| --- | --- | --- |
| `Modal` | `Escape` | Close modal |
| `Dropdown` | `Escape`, `Arrow keys` | Close / navigate items |
| `CommandPalette` | `Escape`, `Arrow keys`, `Enter` | Close / navigate / select |
| `Tabs` | `Arrow keys` | Switch tabs |
| `Accordion` | `Enter`, `Space` | Toggle panel |

---

## Color Contrast

Faststrap components use Bootstrap's built-in color contrast ratios. When creating custom themes:

- Ensure text meets WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text)
- Use `text-bg-{variant}` classes for semantic backgrounds
- Test with browser dev tools Accessibility panel

---

## Screen Reader Testing

1. **Enable a screen reader** (NVDA on Windows, VoiceOver on macOS)
2. **Navigate with keyboard only** — Tab through interactive elements
3. **Check landmarks** — Ensure regions are properly labeled
4. **Verify live regions** — Dynamic updates should be announced

---

## Form Accessibility

```python
from faststrap import FormGroup, Input, Button

FormGroup(
    "Email Address",
    Input(
        name="email",
        type="email",
        required=True,
        aria_describedby="email-help",
    ),
    help_text="We'll never share your email.",
    help_id="email-help",
)
```

Best practices:
- Always provide labels via `FormGroup`
- Use `help_text` for additional context
- Use `aria-describedby` to link inputs to help text
- Use `required` attribute for mandatory fields

---

## See Also

- [Custom Components Guide](../guides/custom-components.md)
- [Validation Guide](../guides/validation.md)
- [Error Handling Guide](../guides/error-handling.md)
