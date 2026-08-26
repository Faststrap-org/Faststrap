# Aspect Ratio

The `AspectRatio` component renders content in a responsive container constrained to a specific aspect ratio.

## Quick Start

```python
AspectRatio(
    Img(src="/hero.jpg", cls="img-fluid"),
    ratio="16/9",
)
```

## Usage Scenarios

### Video Embed

```python
AspectRatio(
    Iframe(src="https://www.youtube.com/embed/dQw4w9WgXcQ", cls="border-0"),
    ratio="16/9",
)
```

### Square Image

```python
AspectRatio(
    Img(src="/avatar.jpg", cls="img-fluid"),
    ratio="1/1",
)
```

### Ultra-Wide Banner

```python
AspectRatio(
    Img(src="/banner.jpg", cls="img-fluid"),
    ratio="21/9",
)
```

### Classic 4:3

```python
AspectRatio(
    Img(src="/presentation.jpg", cls="img-fluid"),
    ratio="4/3",
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `children` | `Any` | Required | Content to display (images, videos, iframes, etc.) |
| `ratio` | `str` | `"16/9"` | Aspect ratio as `width/height` string (e.g. `"16/9"`, `"4/3"`, `"1/1"`, `"21/9"`) |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, id, hx-*, data-*, etc.) |

## Accessibility

- Ensure child media elements (images, iframes) have appropriate `alt` text or titles.
- Use `object-fit: cover` on images for best visual results within the constrained container.

## API Reference

::: faststrap.components.layout.aspect_ratio.AspectRatio
    options:
        show_source: true
        heading_level: 4
