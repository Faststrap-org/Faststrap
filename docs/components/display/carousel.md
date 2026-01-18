# Carousel

Responsive slideshow component for cycling through images or content.

## Basic Usage

```python
from faststrap import Carousel, CarouselItem

Carousel(
    CarouselItem(Img(src="/img/slide1.jpg"), caption="First slide"),
    CarouselItem(Img(src="/img/slide2.jpg"), caption="Second slide"),
    CarouselItem(Img(src="/img/slide3.jpg"), caption="Third slide"),
    id="myCarousel"
)
```

## API Reference

### Carousel

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | CarouselItem | - | Carousel items |
| `id` | str | Required | Unique carousel ID |
| `controls` | bool | True | Show prev/next controls |
| `indicators` | bool | True | Show slide indicators |
| `fade` | bool | False | Use fade transition |
| `interval` | int | 5000 | Auto-play interval (ms), 0 to disable |
| `**kwargs` | Any | - | Additional HTML attributes |

### CarouselItem

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | Any | - | Slide content |
| `caption` | str\|None | None | Slide caption |
| `active` | bool | False | Set as active slide |
| `**kwargs` | Any | - | Additional HTML attributes |

## Examples

### Auto-playing Carousel

```python
Carousel(
    CarouselItem(Img(src="/img/1.jpg"), active=True),
    CarouselItem(Img(src="/img/2.jpg")),
    CarouselItem(Img(src="/img/3.jpg")),
    id="autoCarousel",
    interval=3000  # 3 seconds
)
```

### Fade Transition

```python
Carousel(
    CarouselItem(Img(src="/img/1.jpg"), active=True),
    CarouselItem(Img(src="/img/2.jpg")),
    id="fadeCarousel",
    fade=True
)
```

### With Captions

```python
Carousel(
    CarouselItem(
        Img(src="/products/laptop.jpg"),
        caption="Premium Laptop - $999",
        active=True
    ),
    CarouselItem(
        Img(src="/products/phone.jpg"),
        caption="Smartphone - $699"
    ),
    id="productCarousel"
)
```

## Accessibility

- Uses proper ARIA attributes
- Keyboard navigation supported
- Screen reader announcements for slide changes

## See Also

- [Image](image.md) - For single images
- [Card](card.md) - For content cards
