# TextClamp

`TextClamp` renders long content with optional expandable behavior.

Use it when pages need cleaner previews without overwhelming users.

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

## Why this is useful

- Keeps cards/lists visually balanced when text length varies.
- Improves scanability in feeds, blog indexes, and catalog pages.
- Gives users control to expand full content only when needed.

## Common use cases

1. Blog/news feed previews.
2. Product descriptions on cards.
3. Testimonial excerpts.
4. Comment/thread summaries.

## Without show more button

```python
TextClamp(
    "Very long article preview text ...",
    max_chars=120,
    show_more=False,
)
```

This is useful for strict preview layouts where expansion is not needed.

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

## Full card example

```python
Card(
    H5(post.title),
    TextClamp(
        post.body,
        max_chars=220,
        expand_label="Read full post",
        collapse_label="Collapse",
        button_cls="btn btn-sm btn-link p-0 mt-2",
    ),
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

## Notes

- If text length is below `max_chars`, no toggle button is rendered.
- `show_more=False` keeps preview-only output.
