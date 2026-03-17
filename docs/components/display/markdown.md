# Markdown

Render markdown content into safe HTML with optional sanitization.

## Installation

```bash
pip install "faststrap[markdown]"
```

## Usage

```python
from faststrap import Markdown

Markdown(
    "# Hello\n\nThis is **safe** markdown.",
    cls="prose",
)
```

## Behavior

- Uses Python `markdown` for conversion.
- Sanitizes output with `bleach` by default.
- Raises a clear `ImportError` if optional dependencies are missing.

## Advanced Control

```python
Markdown(
    text,
    sanitize=True,
    extensions=["extra", "tables", "fenced_code"],
)
```

## Security Notes

If you disable sanitization, only render trusted content.

## API Reference

::: faststrap.components.display.markdown.Markdown
    options:
        show_source: true
        heading_level: 4
