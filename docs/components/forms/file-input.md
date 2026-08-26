# File Input

The `FileInput` component provides a styled file upload control with optional image preview support.

## Quick Start

```python
FileInput("upload", label="Upload file")
```

## Usage Scenarios

### With Image Preview

```python
FileInput("avatar", label="Avatar", accept="image/*", preview_id="auto")
```

### Multiple Files

```python
FileInput("docs", label="Documents", multiple=True)
```

### With Accept Filter

```python
FileInput("resume", label="Resume", accept=".pdf,.doc,.docx", required=True)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `label` | `str \| None` | `None` | Label text |
| `multiple` | `bool` | `False` | Allow selecting multiple files |
| `disabled` | `bool` | `False` | Disable the input |
| `required` | `bool` | `False` | Mark as required |
| `accept` | `str \| None` | `None` | File types to accept (e.g. "image/*", ".pdf") |
| `size` | `str \| None` | `None` | Control size (`sm`, `lg`) |
| `file_id` | `str \| None` | `None` | ID for the input |
| `input_cls` | `str` | `""` | Additional classes for input element |
| `label_cls` | `str` | `""` | Additional classes for label element |
| `helper_text` | `str \| None` | `None` | Help text displayed below input |
| `preview_id` | `str \| None` | `None` | ID of an img element for preview. Use `"auto"` to create one automatically. |
| `preview_img_cls` | `str` | `"img-thumbnail mt-2"` | Classes for the preview image |
| `preview_max_height` | `str` | `"200px"` | Max height for preview image |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Labels are associated with inputs via `for` and `id` attributes.
- Required fields use the `required` attribute.
- Preview images include `alt="File preview"`.

## API Reference

::: faststrap.components.forms.file.FileInput
    options:
        show_source: true
        heading_level: 4
