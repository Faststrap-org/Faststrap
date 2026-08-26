# Inline Editor

The `InlineEditor` component renders a compact inline display/edit surface for server-driven edit flows.

## Quick Start

```python
InlineEditor("username", value="jdoe", editing=False)
```

## Usage Scenarios

### Read Mode

```python
InlineEditor("title", value="My Document", display="My Document", editing=False)
```

### Edit Mode

```python
InlineEditor("title", value="My Document", editing=True, endpoint="/update/title")
```

### With Custom Endpoints

```python
InlineEditor(
    "email",
    value="user@example.com",
    editing=False,
    edit_endpoint="/edit/email",
    endpoint="/save/email",
    method="post",
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `value` | `str` | `""` | Current value |
| `display` | `Any \| None` | `None` | Custom display content (falls back to `value`) |
| `editing` | `bool` | `False` | Whether to show the edit form |
| `endpoint` | `str \| None` | `None` | Save endpoint |
| `edit_endpoint` | `str \| None` | `None` | Endpoint to request edit mode |
| `method` | `"get" \| "post" \| "put" \| "patch"` | `"post"` | Save method |
| `input_type` | `str` | `"text"` | HTML input type |
| `save_label` | `str` | `"Save"` | Save button label |
| `cancel_label` | `str` | `"Cancel"` | Cancel button label |
| `edit_label` | `str` | `"Edit"` | Edit button label |
| `hx_target` | `str \| None` | `None` | HTMX target selector |
| `hx_swap` | `str` | `"outerHTML"` | HTMX swap style |
| `input_cls` | `str \| None` | `None` | Additional classes for input |
| `actions_cls` | `str \| None` | `None` | Additional classes for action buttons |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Edit button uses `variant="link"` and `size="sm"` for unobtrusive styling.
- Input gets `aria-label` derived from the field name.
- Proper focus management is handled by HTMX swaps.

## API Reference

::: faststrap.components.forms.inline_editor.InlineEditor
    options:
        show_source: true
        heading_level: 4
