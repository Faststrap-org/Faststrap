# Testimonial Section

The `TestimonialSection` and `Testimonial` components create beautiful customer testimonial displays with avatars, ratings, and quotes. Perfect for landing pages, marketing sites, and social proof sections.

!!! success "Goal"
    By the end of this guide, you'll be able to create professional testimonial sections **that build trust and credibility instantly.**

---

## Quick Start

Here's the simplest way to create a testimonial.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card">
      <div class="card-body">
        <div class="d-flex align-items-center mb-3">
          <img src="https://ui-avatars.com/api/?name=John+Doe" class="rounded-circle me-3" style="width: 48px; height: 48px;">
          <div>
            <h6 class="mb-0">John Doe</h6>
            <small class="text-muted">CEO, Acme Corp</small>
          </div>
        </div>
        <p class="mb-2">"This product changed my life! Highly recommended."</p>
        <div class="text-warning">
          <i class="bi bi-star-fill"></i>
          <i class="bi bi-star-fill"></i>
          <i class="bi bi-star-fill"></i>
          <i class="bi bi-star-fill"></i>
          <i class="bi bi-star-fill"></i>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Testimonial(
    quote="This product changed my life! Highly recommended.",
    author="John Doe",
    role="CEO, Acme Corp",
    rating=5
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Complete Testimonial Section

Full section with multiple testimonials.

```python
TestimonialSection(
    Testimonial(
        quote="FastStrap made building our app incredibly fast. We launched in weeks, not months!",
        author="Sarah Johnson",
        role="CTO, TechStart",
        avatar="/static/avatars/sarah.jpg",
        rating=5
    ),
    Testimonial(
        quote="The zero-JS philosophy is brilliant. Our pages load instantly and SEO is perfect.",
        author="Mike Chen",
        role="Lead Developer, WebCo",
        avatar="/static/avatars/mike.jpg",
        rating=5
    ),
    Testimonial(
        quote="Best FastHTML framework out there. Clean API, great docs, active community.",
        author="Emma Davis",
        role="Freelance Developer",
        avatar="/static/avatars/emma.jpg",
        rating=5
    ),
    title="What Our Customers Say",
    subtitle="Join thousands of developers building with FastStrap",
    columns=3
)
```

### 2. Without Avatars

Simple text-only testimonials.

```python
Testimonial(
    quote="Simple, powerful, and exactly what I needed.",
    author="Alex Thompson",
    role="Indie Hacker"
)
```

### 3. Without Ratings

Testimonials without star ratings.

```python
Testimonial(
    quote="The documentation is outstanding. I was productive in minutes.",
    author="Lisa Park",
    role="Software Engineer"
)
```

---

## Practical Functionality

### Dynamic Testimonials

Load testimonials from database.

```python
def TestimonialsPage():
    # Get testimonials from database
    testimonials = db.query(Testimonial).filter(
        Testimonial.approved == True
    ).order_by(Testimonial.created_at.desc()).limit(6).all()
    
    return TestimonialSection(
        *[
            Testimonial(
                quote=t.quote,
                author=t.author_name,
                role=t.author_role,
                avatar=t.avatar_url,
                rating=t.rating
            )
            for t in testimonials
        ],
        title="Customer Reviews",
        subtitle=f"Rated {get_average_rating()}/5 by {len(testimonials)} customers"
    )
```

### With Carousel

Rotating testimonials.

```python
from faststrap.components.display import Carousel

Carousel(
    *[
        Testimonial(
            quote=t.quote,
            author=t.author,
            role=t.role,
            rating=t.rating
        )
        for t in featured_testimonials
    ],
    indicators=True,
    controls=True,
    auto_play=True,
    interval=5000
)
```

### Video Testimonials

Embed video testimonials.

```python
Card(
    Div(
        Video(
            src="/static/testimonials/john-doe.mp4",
            controls=True,
            cls="w-100"
        ),
        cls="ratio ratio-16x9"
    ),
    CardBody(
        H6("John Doe"),
        P("CEO, Acme Corp", cls="text-muted small"),
        P('"This product transformed our business."')
    )
)
```

---

## Integration Patterns

### In Landing Page

```python
def LandingPage():
    return Container(
        # Hero section
        Hero(...),
        
        # Features
        FeatureGrid(...),
        
        # Testimonials
        TestimonialSection(
            *get_testimonials(),
            title="Loved by Developers",
            subtitle="See what our community is saying",
            cls="my-5 py-5 bg-light"
        ),
        
        # Pricing
        PricingGroup(...),
        
        # CTA
        CallToAction(...)
    )
```

### With Trust Badges

Combine with company logos.

```python
Section(
    Container(
        H2("Trusted by Industry Leaders", cls="text-center mb-4"),
        
        # Company logos
        Row(
            *[
                Col(
                    Img(src=f"/static/logos/{company}.png", cls="img-fluid"),
                    md=2
                )
                for company in ["google", "microsoft", "amazon", "apple", "meta", "netflix"]
            ],
            cls="justify-content-center align-items-center mb-5"
        ),
        
        # Testimonials
        TestimonialSection(
            *testimonials,
            title="What They're Saying"
        )
    ),
    cls="py-5"
)
```

### Filterable Testimonials

Filter by category or rating.

```python
def TestimonialsWithFilter():
    return Div(
        H2("Customer Stories"),
        
        # Filter buttons
        ButtonGroup(
            Button("All", hx_get="/testimonials?filter=all", hx_target="#testimonials"),
            Button("5 Stars", hx_get="/testimonials?filter=5", hx_target="#testimonials"),
            Button("Developers", hx_get="/testimonials?filter=dev", hx_target="#testimonials"),
            cls="mb-4"
        ),
        
        # Testimonials container
        Div(id="testimonials")
    )

@app.get("/testimonials")
def get_testimonials(filter: str = "all"):
    query = db.query(Testimonial)
    
    if filter == "5":
        query = query.filter(Testimonial.rating == 5)
    elif filter == "dev":
        query = query.filter(Testimonial.category == "developer")
    
    testimonials = query.all()
    
    return TestimonialSection(*[
        Testimonial(
            quote=t.quote,
            author=t.author,
            role=t.role,
            rating=t.rating
        )
        for t in testimonials
    ])
```

---

## Parameter Reference

### Testimonial

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `quote` | `str` | Required | Testimonial quote text |
| `author` | `str` | Required | Author name |
| `role` | `str \| None` | `None` | Author role/title |
| `avatar` | `str \| None` | `None` | Avatar image URL |
| `rating` | `int \| None` | `None` | Star rating (1-5) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### TestimonialSection

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*testimonials` | `Any` | Required | Testimonial components |
| `title` | `str \| None` | `None` | Section title |
| `subtitle` | `str \| None` | `None` | Section subtitle |
| `columns` | `int` | 3 | Number of columns (1-4) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

---

## Best Practices

### ✅ Do This

```python
# Use real customer quotes
Testimonial(
    quote="Specific, authentic feedback from real users",
    author="Real Name",
    role="Actual Title, Company"
)

# Include avatars for credibility
Testimonial(
    quote="...",
    author="...",
    avatar="/path/to/real/photo.jpg"  # Real photo
)

# Show ratings
Testimonial(
    quote="...",
    author="...",
    rating=5  # Helps build trust
)

# Organize in sections
TestimonialSection(
    *testimonials,
    title="What Our Customers Say",
    subtitle="Real feedback from real users"
)
```

### ❌ Don't Do This

```python
# Don't use fake testimonials
Testimonial(
    quote="This is the best product ever!",  # Too generic
    author="Anonymous"  # Not credible
)

# Don't use stock photos
avatar="https://thispersondoesnotexist.com/..."  # Fake!

# Don't show only 5-star reviews
# Include variety for authenticity

# Don't overcrowd
TestimonialSection(*50_testimonials)  # Too many!
```

---

## Complete Example

Full testimonials page with filtering.

```python
from fasthtml.common import *
from faststrap import TestimonialSection, Testimonial, Container

@app.get("/testimonials")
def testimonials_page(category: str = "all"):
    # Get testimonials
    query = db.query(TestimonialModel)
    
    if category != "all":
        query = query.filter(TestimonialModel.category == category)
    
    testimonials = query.order_by(
        TestimonialModel.rating.desc()
    ).limit(12).all()
    
    # Calculate stats
    total = db.query(TestimonialModel).count()
    avg_rating = db.query(func.avg(TestimonialModel.rating)).scalar()
    
    return Container(
        # Header
        Div(
            H1("Customer Stories", cls="text-center"),
            P(
                f"{total} reviews • {avg_rating:.1f}/5 average rating",
                cls="text-center text-muted"
            ),
            cls="my-5"
        ),
        
        # Filter
        ButtonGroup(
            Button(
                "All",
                variant="primary" if category == "all" else "outline-primary",
                hx_get="/testimonials?category=all",
                hx_target="#testimonials-content"
            ),
            Button(
                "Developers",
                variant="primary" if category == "developer" else "outline-primary",
                hx_get="/testimonials?category=developer",
                hx_target="#testimonials-content"
            ),
            Button(
                "Businesses",
                variant="primary" if category == "business" else "outline-primary",
                hx_get="/testimonials?category=business",
                hx_target="#testimonials-content"
            ),
            cls="mb-4 d-flex justify-content-center"
        ),
        
        # Testimonials
        Div(
            TestimonialSection(
                *[
                    Testimonial(
                        quote=t.quote,
                        author=t.author_name,
                        role=t.author_role,
                        avatar=t.avatar_url,
                        rating=t.rating
                    )
                    for t in testimonials
                ],
                columns=3
            ),
            id="testimonials-content"
        )
    )
```

---

::: faststrap.components.patterns.testimonial
    options:
        show_source: true
        heading_level: 4
