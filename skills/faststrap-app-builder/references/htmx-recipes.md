# HTMX Recipes

Use these recipes when a Faststrap app needs interaction but does not need a full client-side JavaScript layer.

Start with existing Faststrap components and presets first. Use custom JavaScript only when HTMX and Bootstrap genuinely cannot support the behavior cleanly.

---

## Recipe 1: Live Search with `ActiveSearch`

Use for:

- searchable product lists
- command-like search panels
- filtered customer or document results

```python
from fasthtml.common import Div, P
from faststrap import Card
from faststrap.presets import ActiveSearch


def search_section():
    return Div(
        ActiveSearch(
            endpoint="/search/customers",
            target="#customer-results",
            placeholder="Search customers...",
            debounce=250,
        ),
        Div(
            P("Start typing to search.", cls="text-muted"),
            id="customer-results",
            cls="mt-3",
        ),
    )


@app.get("/search/customers")
def search_customers(q: str = ""):
    if not q:
        return P("Start typing to search.", cls="text-muted")

    matches = [customer for customer in CUSTOMERS if q.lower() in customer["name"].lower()]

    if not matches:
        return P("No matching customers found.", cls="text-muted")

    return Div(
        *[
            Card(
                customer["name"],
                P(customer["email"], cls="mb-0 text-muted"),
                cls="mb-2",
            )
            for customer in matches
        ]
    )
```

Why this works well:

- no custom JavaScript required
- server remains the source of truth
- easy to restyle results with existing Faststrap components

---

## Recipe 2: Auto-Refreshing Metrics with `AutoRefresh`

Use for:

- operational dashboards
- activity panels
- periodic health/status snapshots

```python
from fasthtml.common import Div
from faststrap import Row, Col, StatCard
from faststrap.presets import AutoRefresh


def metrics_panel():
    return Div(
        Div(id="ops-metrics"),
        AutoRefresh(
            endpoint="/api/ops-metrics",
            target="#ops-metrics",
            interval=10000,
        ),
    )


@app.get("/api/ops-metrics")
def ops_metrics():
    return Row(
        Col(StatCard("CPU", "42%", trend="+3%", trend_type="up"), md=4),
        Col(StatCard("Memory", "71%", trend="-2%", trend_type="down"), md=4),
        Col(StatCard("Jobs", "184", trend="+11%", trend_type="up"), md=4),
        cols=1,
        cols_md=3,
        g=3,
    )
```

Add-on guidance:

- for tables, charts, or event lists, refresh only the changing region
- do not auto-refresh the whole page unless the product explicitly needs it

---

## Recipe 3: Field Validation on Blur with `FormGroup`

Use for:

- email validation
- username uniqueness checks
- coupon or referral code validation

```python
from fasthtml.common import Div, Form
from faststrap import Button, FormGroup, Input


def signup_form():
    return Form(
        FormGroup(
            Input(
                "email",
                input_type="email",
                placeholder="you@example.com",
                hx_post="/validate/email",
                hx_trigger="blur",
                hx_target="#email-feedback",
                hx_swap="outerHTML",
            ),
            label="Email",
            help_text="We'll send a confirmation link.",
        ),
        Div(id="email-feedback"),
        Button("Create Account", type="submit"),
        hx_post="/signup",
        hx_target="#signup-shell",
    )


@app.post("/validate/email")
def validate_email(email: str = ""):
    if not email or "@" not in email:
        return Div("Enter a valid email address.", id="email-feedback", cls="invalid-feedback d-block")

    if email.lower().endswith("@example.com"):
        return Div("Example.com addresses are not allowed.", id="email-feedback", cls="invalid-feedback d-block")

    return Div("Email looks good.", id="email-feedback", cls="valid-feedback d-block")
```

Important notes:

- keep the target stable, like `#email-feedback`
- return either valid or invalid feedback markup from the endpoint
- pair this with server-side validation on final submit too

---

## Recipe 4: Confirming Destructive Actions with `ConfirmDialog`

Use for:

- delete actions
- archive/disable actions
- irreversible workflow confirmations

```python
from faststrap import Button, ConfirmDialog


def delete_user_action(user_id: int):
    return ConfirmDialog(
        title="Delete user?",
        message="This action cannot be undone.",
        confirm_text="Yes, delete",
        cancel_text="Cancel",
        confirm_variant="danger",
        trigger=Button("Delete", variant="danger"),
        hx_delete=f"/users/{user_id}",
        hx_target=f"#user-row-{user_id}",
        hx_swap="outerHTML",
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    remove_user(user_id)
    return ""
```

Why this should be the default:

- clear safety affordance
- keeps the destructive action server-driven
- avoids ad hoc confirmation JavaScript

---

## Recipe 5: Lazy Loading Expensive Sections with `LazyLoad`

Use for:

- below-the-fold analytics
- reviews/testimonials
- secondary tabs or heavier content regions

```python
from fasthtml.common import Div
from faststrap import PlaceholderCard
from faststrap.presets import LazyLoad


def analytics_tab():
    return Div(
        LazyLoad(
            endpoint="/fragments/analytics-deep-dive",
            placeholder=PlaceholderCard(animation="glow"),
        )
    )


@app.get("/fragments/analytics-deep-dive")
def analytics_deep_dive():
    return Div(
        build_chart_section(),
        build_event_table(),
    )
```

Use this when:

- the content is expensive to compute
- the content is below the fold
- the first render should stay fast and clean

---

## Recipe 6: Inline Editing Without a Dedicated Component

Use for:

- editable table cells
- settings panels
- quick admin edits

Display state:

```python
from fasthtml.common import Div, Span
from faststrap import Button, Input


def customer_name_cell(customer: dict):
    return Div(
        Span(customer["name"], cls="me-2"),
        Button(
            "Edit",
            variant="link",
            hx_get=f"/customers/{customer['id']}/edit-name",
            hx_target=f"#customer-name-{customer['id']}",
            hx_swap="outerHTML",
        ),
        id=f"customer-name-{customer['id']}",
    )
```

Edit state:

```python
@app.get("/customers/{customer_id}/edit-name")
def edit_customer_name(customer_id: int):
    customer = get_customer(customer_id)
    return Div(
        Input(name="name", value=customer["name"], cls="me-2"),
        Button(
            "Save",
            variant="primary",
            hx_post=f"/customers/{customer_id}/edit-name",
            hx_include="closest div",
            hx_target=f"#customer-name-{customer_id}",
            hx_swap="outerHTML",
        ),
        Button(
            "Cancel",
            variant="link",
            hx_get=f"/customers/{customer_id}/display-name",
            hx_target=f"#customer-name-{customer_id}",
            hx_swap="outerHTML",
        ),
        id=f"customer-name-{customer_id}",
        cls="d-flex align-items-center gap-2",
    )


@app.post("/customers/{customer_id}/edit-name")
def save_customer_name(customer_id: int, name: str):
    update_customer_name(customer_id, name)
    customer = get_customer(customer_id)
    return customer_name_cell(customer)
```

Alternatively, use the `InlineEditor` component from `faststrap` for a built-in editable field pattern.

---

## Recipe 7: Button Loading State with `LoadingButton`

Use for:

- form submissions
- delete/archive actions
- any action that hits the server and should not be repeated

```python
from faststrap import LoadingButton

LoadingButton(
    "Save",
    endpoint="/api/save",
    method="post",
    target="#form",
    variant="primary",
)
```

`LoadingButton` automatically:

- disables the button during the request via `hx-disabled-elt="this"`
- shows a spinner via `hx-indicator="this"`
- sets `aria-busy="true"`

For non-HTMX forms, use `Button(loading=True)` and toggle it with JavaScript, or show a `Spinner` next to the button during submission.

---

## Loading and Empty-State Guidance

When a route fetches or swaps content, always account for these states:

- loading:
  - `Spinner(...)`
  - `Placeholder(...)`
  - `PlaceholderCard(...)`
- empty:
  - `EmptyState(...)`
- success:
  - toast, inline message, or refreshed content
- error:
  - `Alert(...)`, inline `invalid-feedback`, or `ErrorDialog(...)`

Do not leave a blank region during HTMX swaps when a visible loading or empty state would clarify the experience.

---

## When Not to Use HTMX First

Use HTMX only where it fits well. Reach for custom JavaScript or other browser APIs when the feature is fundamentally client-driven:

- rich charting interactions beyond simple refresh/swap patterns
- real-time collaborative editing
- geolocation, camera, media capture, or notification permission flows
- service worker logic and offline caching
- keyboard-driven experiences that require persistent client interaction state

HTMX should be the default interaction tool, not an ideological requirement.
