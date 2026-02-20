# Presets Module

The `faststrap.presets` module provides ready-to-use HTMX interaction patterns and server-side response helpers that eliminate boilerplate for common web interactions. This is **the killer feature** that makes FastHTML development dramatically easier.

!!! success "Goal"
    By the end of this guide, you'll be able to add live search, infinite scroll, auto-refresh, and other dynamic features **with single-line Python calls.**

---

## Quick Start

```python
from faststrap.presets import ActiveSearch, hx_redirect

# Live search in one line
search = ActiveSearch(endpoint="/search", target="#results")

# Server-side redirect
return hx_redirect("/dashboard")
```

---

## Interaction Presets

### ActiveSearch

Live search with debounced server requests.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <input type="search" class="form-control" placeholder="Search products...">
    <div id="results" class="mt-3">
      <p class="text-muted">Start typing to search...</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap.presets import ActiveSearch

# Search input with 300ms debounce

ActiveSearch(
    endpoint="/search",
    target="#results",
    placeholder="Search products...",
    debounce=300
)

# Server endpoint

@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Start typing to search...", cls="text-muted")

    products = db.query(Product).filter(
        Product.name.ilike(f"%{q}%")
    ).limit(10).all()
    
    return Div(*[
        Card(product.name, product.price)
        for product in products
    ])

```
  </div>
</div>

### InfiniteScroll

Infinite feed loading on scroll.

```python
from faststrap.presets import InfiniteScroll

# Feed container
Div(
    *initial_posts,
    InfiniteScroll(
        endpoint="/feed?page=2",
        target="#feed",
        threshold="200px"
    ),
    id="feed"
)

# Server endpoint
@app.get("/feed")
def get_feed(page: int = 1):
    posts = db.query(Post).offset((page-1)*10).limit(10).all()
    
    items = [PostCard(post) for post in posts]
    
    # Add next page loader
    if len(posts) == 10:
        items.append(
            InfiniteScroll(
                endpoint=f"/feed?page={page+1}",
                target="#feed"
            )
        )
    
    return Div(*items)
```

### AutoRefresh

Auto-polling for live updates.

```python
from faststrap.presets import AutoRefresh

# Live metrics dashboard
Div(
    H3("Server Metrics"),
    Div(id="metrics"),
    AutoRefresh(
        endpoint="/metrics",
        target="#metrics",
        interval=5000  # 5 seconds
    )
)

# Server endpoint
@app.get("/metrics")
def get_metrics():
    return Div(
        StatCard("CPU", f"{get_cpu_usage()}%"),
        StatCard("Memory", f"{get_memory_usage()}%"),
        StatCard("Requests", get_request_count())
    )
```

### LazyLoad

Lazy-loaded content blocks.

```python
from faststrap.presets import LazyLoad

# Heavy widget loaded on demand
Card(
    H4("Analytics"),
    LazyLoad(
        endpoint="/widgets/analytics",
        placeholder=Div("Loading analytics...", cls="text-muted")
    )
)

# Server endpoint
@app.get("/widgets/analytics")
def analytics_widget():
    # Expensive computation
    data = compute_analytics()
    return render_chart(data)
```

### LoadingButton

Button with automatic loading state.

```python
from faststrap.presets import LoadingButton

# Automatically shows spinner during request
LoadingButton(
    "Save Profile",
    endpoint="/profile/save",
    target="#profile-form",
    loading_text="Saving..."
)
```

---

## Response Helpers

### hx_redirect

Client-side redirect via HX-Redirect header.

```python
from faststrap.presets import hx_redirect

@app.post("/login")
def login(email: str, password: str):
    user = authenticate(email, password)
    if user:
        req.session["user_id"] = user.id
        return hx_redirect("/dashboard")
    else:
        return ErrorDialog(message="Invalid credentials")
```

### hx_refresh

Full page refresh.

```python
from faststrap.presets import hx_refresh

@app.post("/settings/save")
def save_settings(req):
    # Save settings
    update_settings(req.form)
    
    # Refresh entire page to apply changes
    return hx_refresh()
```

### hx_trigger

Trigger client-side events.

```python
from faststrap.presets import hx_trigger

@app.post("/cart/add")
def add_to_cart(product_id: int):
    cart.add(product_id)
    
    # Trigger custom event to update cart count
    return hx_trigger("cartUpdated")

# Or with event detail
return hx_trigger({
    "showToast": {
        "message": "Added to cart!",
        "variant": "success"
    }
})
```

### toast_response

Return content + out-of-band toast.

```python
from faststrap.presets import toast_response

@app.post("/profile/save")
def save_profile(req):
    # Save profile
    update_profile(req.form)
    
    # Return updated profile + success toast
    return toast_response(
        content=ProfileCard(req.user),
        message="Profile saved successfully!",
        variant="success"
    )
```

---

## Auth Decorator

### @require_auth

Session-based route protection.

```python
from faststrap.presets import require_auth

@app.get("/dashboard")
@require_auth(login_url="/login")
def dashboard(req):
    user = req.session.get("user")
    return DashboardLayout(user=user)

# Custom session key
@app.get("/admin")
@require_auth(
    login_url="/admin/login",
    session_key="admin_id"
)
def admin_panel(req):
    return AdminPanel()

# Disable return-url query parameter
@app.get("/premium")
@require_auth(
    login_url="/login",
    redirect_param=None
)
def premium_feature(req):
    return PremiumContent()
```

---

## Complete Examples

### Live Search with Filters

```python
from faststrap.presets import ActiveSearch

def ProductSearch():
    return Div(
        Row(
            Col(
                ActiveSearch(
                    endpoint="/products/search",
                    target="#product-results",
                    placeholder="Search products..."
                ),
                md=8
            ),
            Col(
                Select(
                    Option("All Categories", value=""),
                    *[Option(cat.name, value=cat.id) for cat in categories],
                    hx_get="/products/search",
                    hx_target="#product-results",
                    hx_include="[name='q']"
                ),
                md=4
            )
        ),
        Div(id="product-results", cls="mt-4")
    )

@app.get("/products/search")
def search_products(q: str = "", category: str = ""):
    query = db.query(Product)
    
    if q:
        query = query.filter(Product.name.ilike(f"%{q}%"))
    if category:
        query = query.filter(Product.category_id == category)
    
    products = query.limit(20).all()
    
    return Div(*[ProductCard(p) for p in products])
```

### Infinite Scroll Feed

```python
from faststrap.presets import InfiniteScroll

@app.get("/")
def home():
    posts = get_posts(page=1)
    
    return Container(
        H1("Latest Posts"),
        Div(
            *[PostCard(post) for post in posts],
            InfiniteScroll(
                endpoint="/posts?page=2",
                target="#feed"
            ),
            id="feed"
        )
    )

@app.get("/posts")
def get_posts_page(page: int = 1):
    posts = db.query(Post).offset((page-1)*10).limit(10).all()
    
    items = [PostCard(post) for post in posts]
    
    # Add next loader if more posts exist
    if len(posts) == 10:
        items.append(
            InfiniteScroll(
                endpoint=f"/posts?page={page+1}",
                target="#feed"
            )
        )
    
    return Div(*items)
```

---

## API Reference

### Interaction Presets

| Function | Parameters | Description |
| :--- | :--- | :--- |
| `ActiveSearch` | `endpoint`, `target`, `placeholder`, `debounce` | Live search input |
| `InfiniteScroll` | `endpoint`, `target`, `threshold` | Infinite scroll loader |
| `AutoRefresh` | `endpoint`, `target`, `interval` | Auto-polling element |
| `LazyLoad` | `endpoint`, `placeholder`, `trigger` | Lazy-loaded content |
| `LoadingButton` | `text`, `endpoint`, `target`, `method` | Button with loading state |

### Response Helpers

| Function | Parameters | Returns | Description |
| :--- | :--- | :--- | :--- |
| `hx_redirect` | `url: str` | `Response` | Client-side redirect |
| `hx_refresh` | - | `Response` | Full page refresh |
| `hx_trigger` | `event: str \| dict` | `Response` | Trigger client event |
| `hx_reswap` | `strategy: str` | `Response` | Change swap strategy |
| `hx_retarget` | `selector: str` | `Response` | Change target element |
| `toast_response` | `content`, `message`, `variant` | `Any` | Content + OOB toast |

### Auth

| Decorator | Parameters | Description |
| :--- | :--- | :--- |
| `@require_auth` | `login_url`, `session_key`, `redirect_param` | Protect routes |

---

::: faststrap.presets
    options:
        show_source: true
        heading_level: 4
