# Image

Responsive image component with Bootstrap utilities.

## Basic Usage

```python
from faststrap import Image

# Responsive image
Image(src="/photos/landscape.jpg", alt="Beautiful landscape")

# Thumbnail
Image(src="/profile.jpg", alt="Profile", thumbnail=True)

# Rounded
Image(src="/avatar.jpg", alt="Avatar", rounded=True)
```

## API Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | str | Required | Image source URL |
| `alt` | str | "" | Alternative text |
| `fluid` | bool | True | Make image responsive |
| `thumbnail` | bool | False | Add thumbnail border |
| `rounded` | bool | False | Round corners |
| `circle` | bool | False | Make image circular |
| `align` | str\|None | None | Alignment: "start", "center", "end" |
| `**kwargs` | Any | - | Additional HTML attributes |

## Examples

### Responsive Fluid Image

```python
Image(
    src="/hero-image.jpg",
    alt="Hero banner",
    fluid=True
)
```

### Profile Avatar

```python
Image(
    src="/users/john.jpg",
    alt="John Doe",
    circle=True,
    style={"width": "100px", "height": "100px"}
)
```

### Thumbnail Gallery

```python
Row(
    Col(Image(src="/gallery/1.jpg", thumbnail=True), md=3),
    Col(Image(src="/gallery/2.jpg", thumbnail=True), md=3),
    Col(Image(src="/gallery/3.jpg", thumbnail=True), md=3),
    Col(Image(src="/gallery/4.jpg", thumbnail=True), md=3)
)
```

### Centered Image

```python
Image(
    src="/logo.png",
    alt="Company Logo",
    align="center"
)
```

## Accessibility

- Always provide meaningful `alt` text
- Use empty `alt=""` for decorative images
- Ensure sufficient color contrast for overlaid text

## See Also

- [Figure](figure.md) - Image with caption
- [Carousel](carousel.md) - Image slideshow
- [Card](card.md) - Image in card layout
