"""
Presets Interactions Demo
Demonstrates all 5 HTMX interaction presets: ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton
"""

from fasthtml.common import H1, H5, Br, Div, FastHTML, P, Small, Strong, serve

from faststrap import (
    Alert,
    Card,
    Container,
    Icon,
    ListGroup,
    ListGroupItem,
    add_bootstrap,
)
from faststrap.presets import ActiveSearch, AutoRefresh, InfiniteScroll, LazyLoad, LoadingButton

app = FastHTML()
add_bootstrap(app)

# Sample data
USERS = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Smith", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com"},
    {"id": 4, "name": "Diana Prince", "email": "diana@example.com"},
    {"id": 5, "name": "Eve Adams", "email": "eve@example.com"},
]


@app.get("/")
def home():
    return Container(
        H1("HTMX Interaction Presets Demo", cls="mb-4"),
        # ActiveSearch Demo
        Card(
            H5("1. ActiveSearch - Live Search with Debouncing", cls="card-title"),
            P("Type to search users (debounced):", cls="text-muted"),
            ActiveSearch(
                endpoint="/api/search-users",
                target="#search-results",
                placeholder="Search users...",
                debounce=300,
            ),
            Div(id="search-results", cls="mt-3"),
            cls="mb-4",
        ),
        # InfiniteScroll Demo
        Card(
            H5("2. InfiniteScroll - Load More on Scroll", cls="card-title"),
            P("Scroll to bottom to load more items:", cls="text-muted"),
            Div(
                *[Div(f"Item {i}", cls="p-3 border-bottom") for i in range(1, 6)],
                InfiniteScroll(
                    endpoint="/api/load-more",
                    target="#infinite-list",
                    threshold="200px",
                ),
                id="infinite-list",
                style=(
                    "max-height: 300px; overflow-y: auto;"
                    " border: 1px solid #dee2e6; border-radius: 0.25rem;"
                ),
            ),
            cls="mb-4",
        ),
        # AutoRefresh Demo
        Card(
            H5("3. AutoRefresh - Auto-updating Content", cls="card-title"),
            P("Updates every 5 seconds:", cls="text-muted"),
            Div(
                AutoRefresh(
                    endpoint="/api/current-time",
                    target="#auto-refresh-content",
                    interval=5000,
                ),
                id="auto-refresh-content",
                cls="p-3 bg-light rounded",
            ),
            cls="mb-4",
        ),
        # LazyLoad Demo
        Card(
            H5("4. LazyLoad - Load Content on Visibility", cls="card-title"),
            P("Content loads when scrolled into view:", cls="text-muted"),
            Div(
                P(
                    "Scroll down to see lazy-loaded content...",
                    cls="text-center text-muted",
                ),
                Div(style="height: 400px;"),  # Spacer
                LazyLoad(
                    endpoint="/api/lazy-content",
                ),
                id="lazy-content",
            ),
            cls="mb-4",
        ),
        # LoadingButton Demo
        Card(
            H5("5. LoadingButton - Button with Loading State", cls="card-title"),
            P("Click to simulate a slow operation:", cls="text-muted"),
            LoadingButton(
                "Process Data",
                endpoint="/api/slow-operation",
                target="#operation-result",
                variant="primary",
            ),
            Div(id="operation-result", cls="mt-3"),
            cls="mb-4",
        ),
        cls="my-5",
    )


@app.get("/api/search-users")
def search_users(q: str = ""):
    """Search users endpoint"""
    if len(q) < 2:
        return ""

    results = [
        u for u in USERS if q.lower() in u["name"].lower() or q.lower() in u["email"].lower()
    ]

    if not results:
        return Div(
            Alert("No users found", variant="info"),
            hx_swap_oob="innerHTML:#search-results",
        )

    return Div(
        ListGroup(
            *[
                ListGroupItem(Div(Strong(u["name"]), Br(), Small(u["email"], cls="text-muted")))
                for u in results
            ]
        ),
        hx_swap_oob="innerHTML:#search-results",
    )


# Global counter for infinite scroll
page_counter = {"count": 5}


@app.get("/api/load-more")
def load_more():
    """Load more items for infinite scroll"""
    import time

    time.sleep(0.5)  # Simulate network delay

    start = page_counter["count"] + 1
    end = start + 5
    page_counter["count"] = end

    items = [Div(f"Item {i}", cls="p-3 border-bottom") for i in range(start, end)]

    # Add another infinite scroll trigger if more items available
    if end < 50:
        items.append(
            InfiniteScroll(
                endpoint="/api/load-more",
                target="#infinite-list",
                threshold="200px",
            )
        )
    else:
        items.append(Div("No more items", cls="p-3 text-center text-muted"))

    return Div(*items)


@app.get("/api/current-time")
def current_time():
    """Return current time"""
    from datetime import datetime

    now = datetime.now().strftime("%H:%M:%S")
    return Div(
        Icon("clock", cls="me-2"),
        f"Current time: {now}",
        cls="d-flex align-items-center",
    )


@app.get("/api/lazy-content")
def lazy_content():
    """Lazy-loaded content"""
    import time

    time.sleep(1)  # Simulate loading

    return Card(
        H5("Lazy-Loaded Content!", cls="text-success"),
        P("This content was loaded only when you scrolled it into view."),
        P("This saves bandwidth and improves initial page load time."),
        variant="success",
    )


@app.get("/api/slow-operation")
def slow_operation():
    """Simulate slow operation"""
    import time

    time.sleep(2)  # Simulate processing

    return Div(
        Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Operation completed successfully!",
            variant="success",
            dismissible=True,
        ),
        hx_swap_oob="innerHTML:#operation-result",
    )


serve()
