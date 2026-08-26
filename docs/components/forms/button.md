# Button

The `Button` component wraps standard HTML `<button>` or `<a>` elements with Bootstrap styling, loading states, and icon support.

## Quick Start

<iframe
  src="https://preview.faststrap.dev/embed/Button?variant=primary&size=lg&pill=true&text=Get+Started"
  width="100%"
  height="140"
  frameborder="0"
  data-faststrap-preview
></iframe>

<div class="mb-3 text-end">
  <a href="https://preview.faststrap.dev/studio/Button" target="_blank" class="btn btn-sm btn-outline-primary">
    ⚡ Open in FastStrap Studio →
  </a>
</div>

```python
Button("Get Started", variant="primary", size="lg", pill=True)
```


## Usage Scenarios

### Variants

```python
Button("Primary", variant="primary")
Button("Secondary", variant="secondary")
Button("Success", variant="success")
Button("Danger", variant="danger")
Button("Warning", variant="warning")
Button("Info", variant="info")
Button("Light", variant="light")
Button("Dark", variant="dark")
Button("Link", variant="link")
```

### Outline Style

```python
Button("Delete", variant="danger", outline=True)
Button("Save Draft", variant="primary", outline=True)
```

### Sizes

```python
Button("Join Now!", size="lg", variant="primary")
Button("Default", variant="secondary")
Button("Details", size="sm", variant="info")
```

### Full Width

```python
Button("Sign In", variant="primary", full_width=True)
```

### Anchor Tag

```python
Button("Go to Login", as_="a", href="/login", variant="primary")
```

### Icons

```python
Button("Save", icon="check-circle", variant="success")
Button("Next Step", icon="arrow-right", icon_pos="end", variant="primary")
```

### Loading State

```python
Button("Save Profile", hx_post="/profile/save", loading_text="Saving...", loading=True)
```

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class / Attribute | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.btn-{variant}` | Color theme. Options: `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `link`. |
| `outline` | `bool` | `.btn-outline-{variant}` | If `True`, renders outline style instead of solid fill. |
| `size` | `str` | `.btn-{size}` | Size of button. Options: `sm` (Small), `lg` (Large). Default is Medium. |
| `full_width` | `bool` | `.w-100` | Makes button span full width of parent. |
| `pill` | `bool` | `.rounded-pill` | Gives button fully rounded corners. |
| `as_` | `str` | `<tag>` | Tag to render. Default `button`. Use `a` for links. |
| `href` | `str` | `href="..."` | URL destination (requires `as_="a"`). |
| `disabled` | `bool` | `disabled` / `.disabled` | Disables interactivity and applies disabled styling. |
| `active` | `bool` | `.active` | Forces the button to appear in a "pressed" state. |
| `icon` | `str` | `<i class="bi bi-{icon}">` | Adds a Bootstrap Icon (e.g., "check", "house"). |
| `icon_pos` | `str` | - | Position of icon: `start` (default) or `end`. |
| `spinner` | `bool` | `.spinner-border` | Controls whether `loading=True` renders a spinner. |
| `loading` | `bool` | - | Helper that enables `spinner` and `disabled` state together. |
| `loading_text` | `str` | - | Text to display when `loading=True`. |
| `css_vars` | `dict` | `style="--var: val"` | Dict of CSS variables to apply inline. |

## Accessibility

- Buttons default to `type="button"` to prevent accidental form submission.
- When rendered as an anchor (`as_="a"`), `role="button"` is added automatically.
- Loading state sets `aria-busy="true"`.
- Active state sets `aria-pressed="true"`.
- Icons and spinners use `aria-hidden="true"`.

## API Reference

::: faststrap.components.forms.button.Button
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.button.CloseButton
    options:
        show_source: true
        heading_level: 4
