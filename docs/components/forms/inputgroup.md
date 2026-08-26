# InputGroup

The `InputGroup` component extends form controls by adding text, buttons, or icons before or after inputs.

## Quick Start

```python
InputGroup(InputGroupText("@"), Input("username", placeholder="Username"))
```

## Usage Scenarios

### Text Addons

```python
InputGroup(InputGroupText("$"), Input("amount", input_type="number", placeholder="0.00"), InputGroupText(".00"))
InputGroup(Input("domain", placeholder="Your website"), InputGroupText(".com"))
InputGroup(InputGroupText("https://"), Input("url", placeholder="example.com"))
```

### Button Addons

```python
InputGroup(Input("search", placeholder="Search..."), Button("Go", variant="primary"))
InputGroup(Button("Copy", variant="outline-secondary"), Input("share_link", value="https://example.com/share/abc123", readonly=True))
```

### Sizes

```python
InputGroup(InputGroupText("@"), Input("username", placeholder="Large"), size="lg")
InputGroup(InputGroupText("@"), Input("username", placeholder="Default"))
InputGroup(InputGroupText("@"), Input("username", placeholder="Small"), size="sm")
```

## Parameter Reference

### InputGroup

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Form controls and addons |
| `size` | `"sm" \| "lg" \| None` | `None` | Group size |
| `nowrap` | `bool` | `False` | Prevent wrapping on smaller screens |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### InputGroupText

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Text or icon content |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Proper form control structure is maintained.
- Label associations work when used with labels.

## API Reference

::: faststrap.components.forms.inputgroup.InputGroup
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.inputgroup.InputGroupText
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.inputgroup.FloatingLabel
    options:
        show_source: true
        heading_level: 4
