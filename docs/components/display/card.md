# Card

Cards are flexible and extensible content containers. They include options for headers and footers, a wide variety of content, contextual background colors, and powerful display options.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Card Documentation](https://getbootstrap.com/docs/5.3/components/card/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card" style="width: 18rem;">
      <div class="card-header">Featured</div>
      <div class="card-body">A simple card with some content.</div>
      <div class="card-footer text-end">
        <button class="btn btn-primary">Go somewhere</button>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Card(
    "A simple card with some content.",
    header="Featured",
    footer=Button("Go somewhere")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Images & Structure
Cards commonly contain images at the top (`img_top`) or bottom (`img_bottom`).

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card" style="width: 18rem;">
      <img src="https://placehold.co/600x400" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card Image Cap</h5>
        <p class="card-text">Some quick example text to build on the card title.</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">Last updated 3 mins ago</small>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Card(
    "Some quick example text to build on the card title.",
    title="Card Image Cap",
    img_top="https://placehold.co/600x400",
    footer="Last updated 3 mins ago"
)
```
  </div>
</div>

Card images are decorative by default (`alt=""`). Add accessible alternative
text and reserve image dimensions when the card represents meaningful content:

```python
Card(
    "Portable performance for demanding workflows.",
    title="Developer laptop",
    img_top="/assets/laptop.jpg",
    img_alt="Silver laptop on a desk",
    img_loading="lazy",
    img_width=640,
    img_height=360,
    img_cls="object-fit-cover",
)
```

Use `img_attrs={...}` for additional attributes such as `data-testid`,
`decoding`, or application-specific hooks.

### 2. Semantic Variants
Apply background colors with `text-bg-{variant}` classes by using the `variant` argument.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2 justify-content-center">
      <div class="card text-bg-success" style="width: 10rem;">
        <div class="card-body">
          <h5 class="card-title">Success</h5>
          <p class="card-text">Success Card</p>
        </div>
      </div>
      <div class="card text-bg-danger" style="width: 10rem;">
        <div class="card-body">
          <h5 class="card-title">Error</h5>
          <p class="card-text">Danger Card</p>
        </div>
      </div>
      <div class="card text-bg-dark" style="width: 10rem;">
        <div class="card-body">
          <h5 class="card-title">Dark</h5>
          <p class="card-text">Dark Card</p>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Card("Success Card", title="Success", variant="success")
Card("Danger Card", title="Error", variant="danger")
Card("Dark Card", title="Dark", variant="dark")
```
  </div>
</div>

### 3. Slot Class Customization 🛠️
FastStrap Cards have specialized "slots" for customization. You don't have to overwrite the base classes; just inject your own into specific parts.

| Slot Param | Targeting | Description |
| :--- | :--- | :--- |
| `header_cls` | `.card-header` | Styles the header container. |
| `body_cls` | `.card-body` | Styles the main content area. |
| `footer_cls` | `.card-footer` | Styles the footer. |
| `title_cls` | `.card-title` | Styles the H5 title. |

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card w-100">
      <div class="card-header bg-primary text-white text-center">My Title</div>
      <div class="card-body p-5 fs-4">Content...</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# A card with a blue header and padded body
Card(
    "Content...",
    header="My Title",
    header_cls="bg-primary text-white text-center",
    body_cls="p-5 fs-4"
)
```
  </div>
</div>

---

## Parameter Reference

::: faststrap.components.display.card.Card
    options:
        show_source: true
        heading_level: 4
