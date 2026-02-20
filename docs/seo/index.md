# SEO Module

The SEO module provides comprehensive tools for adding search engine optimization metadata to your FastHTML applications. It includes components for meta tags, Open Graph, Twitter Cards, and structured data (JSON-LD).

## Quick Start

```python
from fasthtml.common import *
from faststrap import SEO, StructuredData

app = FastHTML()

@app.get("/")
def home():
    return (
        SEO(
            title="My Site - Welcome",
            description="The best site on the internet",
            image="/assets/og-image.jpg",
            url="https://mysite.com/"
        ),
        Container(
            H1("Welcome!"),
        )
    )
```

## Components

### SEO()

The main component for generating SEO meta tags.

**Parameters:**

- `title` (str): Page title (also used for og:title and twitter:title)
- `description` (str): Page description
- `keywords` (list[str]): List of keywords
- `image` (str): Image URL for social sharing
- `url` (str): Canonical URL
- `type` (str): Open Graph type ("website", "article", "product")
- `article` (bool): If True, adds article-specific meta tags
- `published_time` (str): Article published time (ISO 8601)
- `modified_time` (str): Article modified time (ISO 8601)
- `author` (str): Article author name
- `section` (str): Article section/category
- `tags` (list[str]): Article tags
- `twitter_card` (str): Twitter card type
- `twitter_site` (str): Twitter site handle (@username)
- `twitter_creator` (str): Twitter creator handle
- `robots` (str): Robots meta tag value (default: "index, follow")
- `canonical` (str): Canonical URL (if different from url)
- `locale` (str): Page locale (e.g., "en_US")
- `alternate_locales` (list[str]): List of alternate locales

**Returns:** Tuple of meta tag elements to include in page head

### StructuredData

Helper class for generating Schema.org structured data in JSON-LD format.

#### Methods

##### `StructuredData.article()`

Generate Article structured data.

```python
StructuredData.article(
    headline="Blog Post Title",
    description="Post description",
    image="https://example.com/image.jpg",
    author="John Doe",
    published="2026-02-12T10:00:00Z",
    modified="2026-02-12T14:30:00Z"
)
```

##### `StructuredData.product()`

Generate Product structured data.

```python
StructuredData.product(
    name="Product Name",
    description="Product description",
    image="https://example.com/product.jpg",
    price="99.99",
    currency="USD",
    rating=4.5,
    review_count=127,
    availability="InStock"
)
```

##### `StructuredData.breadcrumb()`

Generate BreadcrumbList structured data.

```python
StructuredData.breadcrumb([
    ("Home", "https://example.com/"),
    ("Products", "https://example.com/products"),
    ("Item", "https://example.com/products/item")
])
```

##### `StructuredData.organization()`

Generate Organization structured data.

```python
StructuredData.organization(
    name="Company Name",
    url="https://example.com",
    logo="https://example.com/logo.png",
    social_links=[
        "https://twitter.com/company",
        "https://linkedin.com/company/company"
    ]
)
```

##### `StructuredData.local_business()`

Generate LocalBusiness structured data.

```python
StructuredData.local_business(
    name="Business Name",
    address={
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "country": "US"
    },
    phone="+1-555-123-4567",
    hours={
        "Monday-Friday": "9:00-17:00",
        "Saturday-Sunday": "10:00-14:00"
    }
)
```

## Usage Examples

### Basic Page SEO

```python
@app.get("/")
def home():
    return (
        SEO(
            title="My Site - Home",
            description="Welcome to my site",
            keywords=["python", "fasthtml", "web"],
            image="/assets/og-image.jpg",
            url="https://mysite.com/"
        ),
        Container(H1("Home"))
    )
```

### Blog Post with Article SEO

```python
@app.get("/blog/{slug}")
def blog_post(slug: str):
    post = get_post(slug)
    
    return (
        SEO(
            title=f"{post.title} - My Blog",
            description=post.excerpt,
            image=post.featured_image,
            url=f"https://mysite.com/blog/{slug}",
            article=True,
            published_time=post.published_at,
            modified_time=post.updated_at,
            author=post.author,
            section="Technology",
            tags=post.tags,
            twitter_site="@myblog",
            twitter_creator="@author"
        ),
        StructuredData.article(
            headline=post.title,
            description=post.excerpt,
            image=post.featured_image,
            author=post.author,
            published=post.published_at,
            modified=post.updated_at
        ),
        Container(
            H1(post.title),
            Div(post.content)
        )
    )
```

### E-commerce Product Page

```python
@app.get("/product/{id}")
def product_page(id: str):
    product = get_product(id)
    
    return (
        SEO(
            title=f"{product.name} - Buy Online",
            description=product.description,
            image=product.images[0],
            url=f"https://mysite.com/product/{id}",
            type="product",
            twitter_site="@mystore"
        ),
        StructuredData.product(
            name=product.name,
            description=product.description,
            image=product.images[0],
            price=str(product.price),
            currency="USD",
            rating=product.avg_rating,
            review_count=product.review_count,
            availability="InStock" if product.in_stock else "OutOfStock"
        ),
        Container(
            H1(product.name),
            P(product.description)
        )
    )
```

### Local Business Page

```python
@app.get("/")
def home():
    return (
        SEO(
            title="Joe's Coffee - Best Coffee in Town",
            description="Visit Joe's Coffee for the best coffee in Springfield",
            image="/assets/shop.jpg",
            url="https://joescoffee.com/"
        ),
        StructuredData.local_business(
            name="Joe's Coffee Shop",
            address={
                "street": "123 Main St",
                "city": "Springfield",
                "state": "IL",
                "zip": "62701",
                "country": "US"
            },
            phone="+1-555-123-4567",
            hours={
                "Monday-Friday": "7:00-19:00",
                "Saturday-Sunday": "8:00-17:00"
            }
        ),
        Container(H1("Joe's Coffee"))
    )
```

### Multi-language Site

```python
@app.get("/es/about")
def about_es():
    return (
        SEO(
            title="Acerca de Nosotros",
            description="Información sobre nuestra empresa",
            url="https://example.com/es/about",
            locale="es_ES",
            alternate_locales=["en_US", "fr_FR"]
        ),
        Container(H1("Acerca de Nosotros"))
    )
```

## Generated HTML

### Basic Meta Tags

```html
<title>Page Title</title>
<meta name="title" content="Page Title">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2, keyword3">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://example.com/page">
```

### Open Graph Tags

```html
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Page description">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
```

### Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Page description">
<meta name="twitter:image" content="https://example.com/image.jpg">
<meta name="twitter:site" content="@sitehandle">
```

### Article Tags

```html
<meta property="og:type" content="article">
<meta property="article:published_time" content="2026-02-12T10:00:00Z">
<meta property="article:modified_time" content="2026-02-12T14:30:00Z">
<meta property="article:author" content="John Doe">
<meta property="article:section" content="Technology">
<meta property="article:tag" content="python">
<meta property="article:tag" content="fasthtml">
```

### Structured Data (JSON-LD)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Blog Post Title",
  "description": "Post description",
  "image": "https://example.com/image.jpg",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "datePublished": "2026-02-12T10:00:00Z",
  "dateModified": "2026-02-12T14:30:00Z"
}
</script>
```

## Best Practices

### 1. Always Include Basic SEO

Every page should have at minimum:

- Title
- Description
- Canonical URL

```python
SEO(
    title="Page Title - Site Name",
    description="Page description (150-160 characters)",
    url="https://example.com/page"
)
```

### 2. Use Descriptive Titles

- Keep titles under 60 characters
- Include your brand name
- Make titles unique per page

```python
# Good
title="10 Python Tips - My Blog"

# Bad
title="Blog Post"
```

### 3. Write Compelling Descriptions

- Keep descriptions 150-160 characters
- Include target keywords naturally
- Make them actionable

```python
description="Learn 10 essential Python tips to write cleaner code. Perfect for beginners and experienced developers."
```

### 4. Use High-Quality Images

- Use images at least 1200x630px for social sharing
- Use absolute URLs for images
- Optimize images for fast loading

```python
image="https://example.com/assets/og-image.jpg"  # Good
image="/assets/og-image.jpg"  # Works, but absolute is better
```

### 5. Add Structured Data

Use structured data for:

- Blog posts (Article)
- Products (Product)
- Local businesses (LocalBusiness)
- Organizations (Organization)

```python
return (
    SEO(...),
    StructuredData.article(...),
    # Your page content
)
```

### 6. Test Your SEO

Use these tools to validate:

- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)

## API Reference

See the [SEO API documentation](../api/seo.md) for complete parameter details and return types.

## Examples

See the [examples directory](../../examples/05_new_components/seo_demo.py) for complete working examples.
