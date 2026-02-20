# TextClamp

`TextClamp` renders long content with optional expandable behavior.

## Import

```python
from faststrap import TextClamp
```

## Basic usage

```python
TextClamp(
    "Very long article preview text ...",
    max_chars=120,
)
```

## Without show more button

```python
TextClamp(
    "Very long article preview text ...",
    max_chars=120,
    show_more=False,
)
```

## Custom button labels and style

```python
TextClamp(
    article_body,
    max_chars=180,
    expand_label="Read full post",
    collapse_label="Show less",
    button_cls="btn btn-sm btn-outline-primary mt-2",
)
```

## API

- `text`: Full text content.
- `max_chars`: Number of characters before truncation.
- `show_more`: Toggle expandable mode.
- `expand_label`: Expand button text.
- `collapse_label`: Collapse button text.
- `button_cls`: Button classes.
- `ellipsis`: Trailing truncation string.

