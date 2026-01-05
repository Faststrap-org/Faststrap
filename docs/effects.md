# Effects (Fx)

The `Fx` effects module provides zero-JavaScript visual effects using pure CSS. Add animations, transitions, and micro-interactions to your components without writing a single line of JavaScript.

!!! success "Goal"
    Master using Faststrap's built-in effects system to create smooth, professional animations and interactions that enhance user experience.

---

## Quick Start

```python
from faststrap import Card, Fx

# Card with fade-in animation and hover lift effect
Card(
    "Content here",
    cls=f"{Fx.fade_in} {Fx.hover_lift}"
)
```

---

## Effect Categories

### 1. Entrance Animations

Appear on page load or HTMX swap.

```python
# Fade in
Card("Content", cls=Fx.fade_in)

# Slide up
Card("Content", cls=Fx.slide_up)

# Slide down
Card("Content", cls=Fx.slide_down)

# Slide from left
Card("Content", cls=Fx.slide_left)

# Slide from right
Card("Content", cls=Fx.slide_right)

# Zoom in
Card("Content", cls=Fx.zoom_in)

# Bounce in
Card("Content", cls=Fx.bounce_in)
```

---

### 2. Hover Interactions

Trigger on mouseover.

```python
# Lift on hover (subtle elevation)
Card("Hover me", cls=Fx.hover_lift)

# Scale on hover (slight zoom)
Button("Click me", cls=Fx.hover_scale)

# Glow effect
Card("Glowing", cls=Fx.hover_glow)

# Tilt effect
Card("Tilt", cls=Fx.hover_tilt)

# Color shift
Button("Colorize", cls=Fx.hover_colorize)
```

---

### 3. Loading States

For HTMX indicators.

```python
# Spinning animation
Div(Icon("arrow-repeat"), cls=Fx.spin)

# Pulsing animation
Div("Loading...", cls=Fx.pulse)

# Shimmer effect (skeleton loading)
Div(cls=Fx.shimmer, style={"width": "200px", "height": "20px"})
```

---

### 4. Visual Effects

Glass morphism and shadows.

```python
# Glass effect (frosted glass)
Card("Glass card", cls=Fx.glass)

# Soft shadow
Card("Soft shadow", cls=Fx.shadow_soft)

# Sharp shadow
Card("Sharp shadow", cls=Fx.shadow_sharp)

# Gradient shift
Div("Gradient", cls=Fx.gradient_shift)
```

---

### 5. Modifiers

Control speed and delay.

```python
# Speed modifiers
Card("Fast", cls=f"{Fx.fade_in} {Fx.fast}")  # 150ms
Card("Slow", cls=f"{Fx.fade_in} {Fx.slow}")  # 500ms
Card("Slower", cls=f"{Fx.fade_in} {Fx.slower}")  # 1000ms

# Delay modifiers
Card("Delayed", cls=f"{Fx.fade_in} {Fx.delay_sm}")  # 200ms delay
Card("More delay", cls=f"{Fx.fade_in} {Fx.delay_lg}")  # 500ms delay
```

---

## Combining Effects

```python
from faststrap import Card, Fx

# Fade in with hover lift and soft shadow
Card(
    "Beautiful card",
    cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.shadow_soft}"
)

# Slide up fast with delay and hover scale
Card(
    "Animated card",
    cls=f"{Fx.slide_up} {Fx.fast} {Fx.delay_sm} {Fx.hover_scale}"
)

# Glass card with glow on hover
Card(
    "Glass effect",
    cls=f"{Fx.glass} {Fx.hover_glow}"
)
```

---

## Common Recipes

### Product Card with Effects

```python
Card(
    Img(src="product.jpg", cls="card-img-top"),
    Div(
        H5("Product Name", cls="card-title"),
        P("$99.99", cls="card-text"),
        Button("Add to Cart", variant="primary"),
        cls="card-body"
    ),
    cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.shadow_soft}"
)
```

---

### Hero Section with Staggered Animations

```python
from faststrap import Hero, Fx

Hero(
    H1("Welcome", cls=f"{Fx.fade_in}"),
    P("Subtitle", cls=f"{Fx.fade_in} {Fx.delay_sm}"),
    Button("Get Started", cls=f"{Fx.fade_in} {Fx.delay_md}")
)
```

---

### Loading Indicator

```python
Div(
    Spinner(cls=Fx.spin),
    "Loading...",
    cls="text-center"
)
```

---

## Available Effects Reference

### Entrance Animations
- `Fx.fade_in` - Fade in
- `Fx.slide_up` - Slide from bottom
- `Fx.slide_down` - Slide from top
- `Fx.slide_left` - Slide from right
- `Fx.slide_right` - Slide from left
- `Fx.zoom_in` - Zoom in
- `Fx.bounce_in` - Bounce in

### Hover Effects
- `Fx.hover_lift` - Lift on hover
- `Fx.hover_scale` - Scale on hover
- `Fx.hover_glow` - Glow on hover
- `Fx.hover_tilt` - Tilt on hover
- `Fx.hover_colorize` - Color shift on hover

### Loading States
- `Fx.spin` - Spinning animation
- `Fx.pulse` - Pulsing animation
- `Fx.shimmer` - Shimmer effect

### Visual Effects
- `Fx.glass` - Glass morphism
- `Fx.shadow_soft` - Soft shadow
- `Fx.shadow_sharp` - Sharp shadow
- `Fx.gradient_shift` - Gradient animation

### Modifiers
**Speed:**
- `Fx.fast` - 150ms
- `Fx.slow` - 500ms
- `Fx.slower` - 1000ms

**Delay:**
- `Fx.delay_xs` - 100ms
- `Fx.delay_sm` - 200ms
- `Fx.delay_md` - 300ms
- `Fx.delay_lg` - 500ms
- `Fx.delay_xl` - 1000ms

---

## Accessibility

All effects respect `prefers-reduced-motion` media query. Users who have enabled reduced motion in their OS settings will see instant transitions instead of animations.

::: faststrap.core.effects.Fx
    options:
        show_source: true
        heading_level: 4
