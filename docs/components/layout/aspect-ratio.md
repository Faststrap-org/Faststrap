# AspectRatio

`AspectRatio` renders content in a responsive container that maintains a consistent width-to-height ratio. It uses the CSS `aspect-ratio` property, so it works without any JavaScript.

Common use cases: video embeds, image galleries, map containers, and responsive media cards.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Ratios](https://getbootstrap.com/docs/5.3/helpers/ratio/)

---

## Quick Start

```python
from faststrap import AspectRatio, Image

AspectRatio(
    Image(src="https://placehold.co/600x400", cls="card-img-top"),
    ratio="16/9",
)
```

---

## Visual Examples & Use Cases

### 1. 16:9 Video Embed

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="overflow-hidden" style="aspect-ratio: 16/9;">
      <div style="width: 100%; height: 100%; background: #e9ecef; display: flex; align-items: center; justify-content: center;">
        <span class="text-muted">16:9 Video Placeholder</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
AspectRatio(
    Div("16:9 Video Placeholder", cls="d-flex align-items-center justify-content-center bg-light"),
    ratio="16/9",
)
```
  </div>
</div>

### 2. 1:1 Square (Profile Picture)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="overflow-hidden" style="aspect-ratio: 1/1; max-width: 200px;">
      <div style="width: 100%; height: 100%; background: #e9ecef; display: flex; align-items: center; justify-content: center;">
        <span class="text-muted">1:1 Avatar</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
AspectRatio(
    Image(src="/avatar.jpg", cls="img-fluid"),
    ratio="1/1",
)
```
  </div>
</div>

### 3. 4:3 Image

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="overflow-hidden" style="aspect-ratio: 4/3;">
      <div style="width: 100%; height: 100%; background: #e9ecef; display: flex; align-items: center; justify-content: center;">
        <span class="text-muted">4:3 Image</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
AspectRatio(
    Image(src="/photo.jpg", cls="img-fluid"),
    ratio="4/3",
)
```
  </div>
</div>

### 4. Custom Ratio

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="overflow-hidden" style="aspect-ratio: 21/9;">
      <div style="width: 100%; height: 100%; background: #e9ecef; display: flex; align-items: center; justify-content: center;">
        <span class="text-muted">21:9 Ultra-wide</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
AspectRatio(
    Div("21:9 Ultra-wide", cls="d-flex align-items-center justify-content-center bg-light"),
    ratio="21/9",
)
```
  </div>
</div>

---

## Practical Functionality

### 1. Embedding a YouTube Video

```python
AspectRatio(
    Iframe(
        src="https://www.youtube.com/embed/dQw4w9WgXcQ",
        frameborder="0",
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
        allowfullscreen=True,
        cls="w-100 h-100",
    ),
    ratio="16/9",
)
```

### 2. Inside a Card

```python
Card(
    AspectRatio(
        Image(src="/hero.jpg", cls="card-img-top"),
        ratio="16/9",
    ),
    Card.Body(
        H4("Video Thumbnail"),
        P("Click to play the full video."),
    ),
)
```

### 3. Responsive Image Gallery

```python
Row(
    Col(
        AspectRatio(Image(src="/img1.jpg", cls="img-fluid"), ratio="1/1"),
        cols=4,
    ),
    Col(
        AspectRatio(Image(src="/img2.jpg", cls="img-fluid"), ratio="1/1"),
        cols=4,
    ),
    Col(
        AspectRatio(Image(src="/img3.jpg", cls="img-fluid"), ratio="1/1"),
        cols=4,
    ),
)
```

---

## Common Ratios

| Ratio | Use Case |
|-------|----------|
| `16/9` | Video, YouTube embeds, wide images |
| `4/3` | Classic photos, documents |
| `1/1` | Profile pictures, avatars, Instagram-style |
| `21/9` | Ultra-wide monitors, cinematic |
| `3/2` | Standard photography |
| `9/16` | Vertical video, TikTok/Reels |

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `children` | `Any` | required | Content to display inside the ratio box. |
| `ratio` | `str` | `"16/9"` | Aspect ratio as `"width/height"` string. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes (cls, id, style, etc.). |

---

## Accessibility

- The container uses `overflow: hidden` to clip content that exceeds the aspect ratio.
- Child media elements should use `object-fit: cover` or `object-fit: contain` for best results.

---

## API Reference

::: faststrap.components.layout.aspect_ratio.AspectRatio
    options:
        show_source: true
        heading_level: 4
