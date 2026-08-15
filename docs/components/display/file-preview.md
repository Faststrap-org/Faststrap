# FilePreview

`@experimental`

Generic file preview shell with safe fallback behavior.

---

## Quick Start

```python
from faststrap import FilePreview

FilePreview("/files/report.pdf", title="Annual Report")
FilePreview("/files/photo.jpg", title="Team Photo")
FilePreview("/files/notes.md", title="Meeting Notes")
```

---

## Features

- Automatic file type inference from extension
- Image preview via `<img>`
- PDF preview via `<iframe>`
- Text/code preview with safe fallback message
- Custom fallback for unsupported types

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `src` | `str` | required | File URL or path. |
| `kind` | `str \| None` | `None` | Explicit file kind: `"image"`, `"pdf"`, `"text"`, `"code"`, `"unknown"`. |
| `title` | `str \| None` | `None` | Optional title shown above the preview. |
| `height` | `str \| int \| None` | `None` | Preview height (px or CSS string). |
| `width` | `str \| int \| None` | `None` | Preview width (px or CSS string). |
| `fallback` | `str \| None` | `None` | Custom fallback message for unsupported types. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

---

## Usage Examples

### Image Preview

```python
FilePreview("/assets/diagram.png", title="Circuit Diagram")
```

### PDF Document

```python
FilePreview("/docs/manual.pdf", title="User Manual", height="600px")
```

### Code File

```python
FilePreview("/src/main.py", title="Main Script")
```

### Custom Fallback

```python
FilePreview(
    "/files/data.bin",
    title="Binary Data",
    fallback="Binary preview not supported. Download to view.",
)
```

---

## Supported File Types

| Extension(s) | Inferred Kind |
| --- | --- |
| `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp` | `image` |
| `.pdf` | `pdf` |
| `.txt`, `.md`, `.csv`, `.json`, `.xml`, `.html` | `text` |
| `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.rs`, `.go` | `code` |
| Other | `unknown` |

---

## Notes

- For production use, consider server-side content-type validation.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.display.file_preview.FilePreview
    options:
        show_source: true
        heading_level: 4
