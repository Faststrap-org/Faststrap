# Searchable Select

The `SearchableSelect` component creates a server-side searchable dropdown using HTMX, replacing client-side libraries like Select2 or Choices.js with pure server-side filtering. Perfect for large datasets and dynamic options.

!!! success "Goal"
    By the end of this guide, you'll be able to create searchable dropdowns with **server-side filtering and zero JavaScript dependencies.**

---

## Quick Start

Here's the simplest way to create a searchable select.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <input type="search" class="form-control mb-2" placeholder="Search users...">
    <div class="list-group" style="max-height: 200px; overflow-y: auto;">
      <a href="#" class="list-group-item list-group-item-action">John Doe</a>
      <a href="#" class="list-group-item list-group-item-action">Jane Smith</a>
      <a href="#" class="list-group-item list-group-item-action">Bob Johnson</a>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SearchableSelect(
    endpoint="/api/users/search",
    name="user_id",
    placeholder="Search users..."
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. User Selection

Search and select from large user lists.

```python
FormGroup(
    SearchableSelect(
        endpoint="/api/users/search",
        name="assigned_to",
        placeholder="Search by name or email...",
        debounce=300
    ),
    label="Assign To",
    help_text="Start typing to search users"
)

# Server endpoint
@app.get("/api/users/search")
def search_users(q: str = ""):
    if len(q) < 2:
        return P("Type at least 2 characters", cls="text-muted p-2")
    
    users = db.query(User).filter(
        or_(
            User.name.ilike(f"%{q}%"),
            User.email.ilike(f"%{q}%")
        )
    ).limit(10).all()
    
    if not users:
        return P("No users found", cls="text-muted p-2")
    
    return Div(*[
        A(
            Div(
                Strong(user.name),
                Br(),
                Small(user.email, cls="text-muted")
            ),
            href="#",
            cls="list-group-item list-group-item-action",
            hx_post=f"/select/user/{user.id}",
            hx_target="#user-selection"
        )
        for user in users
    ])
```

### 2. Country/Location Selection

Searchable location picker.

```python
SearchableSelect(
    endpoint="/api/countries/search",
    name="country",
    placeholder="Search countries...",
    initial_options=[
        ("us", "United States"),
        ("uk", "United Kingdom"),
        ("ca", "Canada"),
    ]
)

@app.get("/api/countries/search")
def search_countries(q: str = ""):
    countries = get_countries()  # Your data source
    
    if q:
        countries = [c for c in countries if q.lower() in c.name.lower()]
    
    return Div(*[
        A(
            country.name,
            href="#",
            cls="list-group-item list-group-item-action",
            data_value=country.code
        )
        for country in countries[:20]  # Limit results
    ])
```

### 3. Product Search

E-commerce product selection.

```python
SearchableSelect(
    endpoint="/api/products/search",
    name="product_id",
    placeholder="Search products...",
    min_chars=3,
    debounce=400
)

@app.get("/api/products/search")
def search_products(q: str = ""):
    if len(q) < 3:
        return ""
    
    products = db.query(Product).filter(
        Product.name.ilike(f"%{q}%")
    ).limit(15).all()
    
    return Div(*[
        A(
            Div(
                Img(src=p.image, style="width: 40px; height: 40px; object-fit: cover;", cls="me-2"),
                Div(
                    Strong(p.name),
                    Br(),
                    Small(f"${p.price}", cls="text-success")
                ),
                cls="d-flex align-items-center"
            ),
            href="#",
            cls="list-group-item list-group-item-action"
        )
        for p in products
    ])
```

---

## Practical Functionality

### With Initial Options

Show popular choices before search.

```python
SearchableSelect(
    endpoint="/api/tags/search",
    name="tags",
    placeholder="Search tags...",
    initial_options=[
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("react", "React"),
        ("fasthtml", "FastHTML"),
    ]
)
```

### Custom Debounce

Adjust search delay for different use cases.

```python
# Fast search for small datasets
SearchableSelect(
    endpoint="/api/quick-search",
    name="item",
    debounce=150  # 150ms delay
)

# Slower search for expensive queries
SearchableSelect(
    endpoint="/api/heavy-search",
    name="item",
    debounce=500  # 500ms delay
)
```

### Minimum Characters

Prevent searches that are too broad.

```python
SearchableSelect(
    endpoint="/api/search",
    name="query",
    min_chars=3,  # Require 3+ characters
    placeholder="Type at least 3 characters..."
)

@app.get("/api/search")
def search(q: str = ""):
    if len(q) < 3:
        return P(
            "Please enter at least 3 characters",
            cls="text-muted p-3 text-center"
        )
    
    # Perform search...
```

---

## Integration Patterns

### With Form Submission

```python
Form(
    FormGroup(
        SearchableSelect(
            endpoint="/api/users/search",
            name="user_id",
            placeholder="Select user..."
        ),
        label="User",
        required=True
    ),
    FormGroup(
        Input(name="message"),
        label="Message"
    ),
    Button("Send", type="submit"),
    hx_post="/messages/send"
)
```

### With Loading Indicator

```python
Div(
    SearchableSelect(
        endpoint="/api/search",
        name="item"
    ),
    Div(
        Spinner(size="sm"),
        " Searching...",
        cls="htmx-indicator text-muted mt-2"
    )
)
```

### Multi-Select Pattern

Allow selecting multiple items.

```python
def MultiSearchableSelect(endpoint, name):
    return Div(
        SearchableSelect(
            endpoint=endpoint,
            name=f"{name}_search"
        ),
        Div(id=f"{name}-selected", cls="mt-2"),
        # Hidden inputs for selected values
        Div(id=f"{name}-values")
    )

# When user clicks result
@app.post("/select/{item_id}")
def select_item(item_id: int):
    item = get_item(item_id)
    
    return Div(
        # Add to selected list
        Badge(
            item.name,
            Icon("x", cls="ms-1"),
            cls="me-1",
            hx_delete=f"/deselect/{item_id}",
            hx_target="closest .badge",
            hx_swap="outerHTML"
        ),
        # Add hidden input
        Input(type="hidden", name="items[]", value=item_id),
        hx_swap_oob="beforeend:#selected-items"
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `endpoint` | `str` | Required | Server endpoint for search (receives 'q' param) |
| `name` | `str` | Required | Form field name |
| `placeholder` | `str` | "Search..." | Search input placeholder |
| `initial_options` | `list[tuple]` | `None` | Initial options as (value, text) tuples |
| `debounce` | `int` | 300 | Milliseconds to wait after typing |
| `min_chars` | `int` | 2 | Minimum characters before searching |
| `select_id` | `str \| None` | Auto | Unique ID for the select element |
| `**kwargs` | `Any` | - | Additional HTML attributes |

---

## Best Practices

### ✅ Do This

```python
# Limit results to prevent overwhelming UI
@app.get("/api/search")
def search(q: str):
    results = query.filter(...).limit(20).all()  # Max 20
    return render_results(results)

# Show helpful empty states
if not results:
    return P("No results found. Try different keywords.", cls="text-muted p-3")

# Use debounce to reduce server load
SearchableSelect(
    endpoint="/api/search",
    debounce=300  # Wait for user to finish typing
)

# Provide visual feedback
return Div(
    Icon("search", cls="text-muted me-2"),
    "Searching...",
    cls="htmx-indicator"
)
```

### ❌ Don't Do This

```python
# Don't return unlimited results
@app.get("/api/search")
def search(q: str):
    return query.all()  # Could be thousands!

# Don't search on every keystroke
SearchableSelect(
    debounce=0  # Server overload!
)

# Don't forget minimum characters
@app.get("/api/search")
def search(q: str):
    # Searching for "a" returns everything!
    return query.filter(name.ilike(f"%{q}%")).all()
```

---

## Complete Example

Full searchable user selector.

```python
from fasthtml.common import *
from faststrap import SearchableSelect, FormGroup, Button

@app.get("/assign-task")
def assign_task_form():
    return Form(
        FormGroup(
            SearchableSelect(
                endpoint="/api/users/search",
                name="assigned_to",
                placeholder="Search by name or email...",
                debounce=300
            ),
            label="Assign To",
            help_text="Start typing to search users",
            required=True
        ),
        FormGroup(
            Input(name="task_name"),
            label="Task Name",
            required=True
        ),
        Button("Assign Task", type="submit", variant="primary"),
        hx_post="/tasks/assign"
    )

@app.get("/api/users/search")
def search_users(q: str = ""):
    # Require minimum characters
    if len(q) < 2:
        return P(
            Icon("search", cls="me-2"),
            "Type at least 2 characters to search",
            cls="text-muted p-3 text-center"
        )
    
    # Search users
    users = db.query(User).filter(
        or_(
            User.name.ilike(f"%{q}%"),
            User.email.ilike(f"%{q}%")
        )
    ).limit(15).all()
    
    # Handle empty results
    if not users:
        return P(
            Icon("inbox", cls="me-2"),
            "No users found",
            cls="text-muted p-3 text-center"
        )
    
    # Return results
    return Div(*[
        A(
            Div(
                Img(
                    src=user.avatar or "/static/default-avatar.png",
                    cls="rounded-circle me-2",
                    style="width: 32px; height: 32px; object-fit: cover;"
                ),
                Div(
                    Strong(user.name),
                    Br(),
                    Small(user.email, cls="text-muted")
                ),
                cls="d-flex align-items-center"
            ),
            href="#",
            cls="list-group-item list-group-item-action",
            onclick=f"selectUser({user.id}, '{user.name}')"
        )
        for user in users
    ])
```

---

::: faststrap.components.forms.searchable_select.SearchableSelect
    options:
        show_source: true
        heading_level: 4
