"""Faststrap v0.9.0+ Component Demo

Demonstrates modern components including v0.9.0 additions:
- SearchBar with HTMX live search
- ProfileDropdown for authenticated user menu
- DataCard for structured metadata
- SplitPane for resizable master/detail layout
- Switcher for responsive row-to-column layout
- Toast/ToastContainer for notifications
- Modal and Drawer for overlays
- Card, Button, Badge, Alert for base surfaces
"""

from fasthtml.common import (
    FastHTML,
    Div,
    H1,
    H2,
    H5,
    P,
    A,
    Ul,
    Li,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    serve,
)

from faststrap import (
    add_bootstrap,
    Container,
    Navbar,
    SearchBar,
    ProfileDropdown,
    ToastContainer,
    Toast,
    DataCard,
    Button,
    Card,
    Row,
    Col,
    Switcher,
    SplitPane,
    Modal,
    Drawer,
    Table,
)

app = FastHTML()
add_bootstrap(app, mode="dark", use_cdn=False)

ITEMS = [
    {"id": 1, "name": "Alpha", "status": "Active", "value": "$1,200"},
    {"id": 2, "name": "Beta", "status": "Pending", "value": "$850"},
    {"id": 3, "name": "Gamma", "status": "Active", "value": "$2,400"},
    {"id": 4, "name": "Delta", "status": "Review", "value": "$620"},
]


@app.get("/")
def home():
    return Div(
        Navbar(
            SearchBar(
                placeholder="Search items...",
                endpoint="/search",
                target="#search-results",
                cls="me-3",
            ),
            ProfileDropdown(
                "Alex Developer",
                subtitle="alex@example.com",
                items=[
                    ("Profile", "/profile"),
                    ("Settings", "/settings"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="Faststrap Demo",
            brand_href="/",
        ),
        ToastContainer(
            Toast(
                "Welcome to Faststrap v0.9.0!",
                title="Success",
                variant="success",
                id="welcomeToast",
            ),
            position="top-end",
        ),
        Container(
            H1("Faststrap v0.9.0+ Demo", cls="my-5"),
            P("Modern components with HTMX-first interactions.", cls="lead mb-5"),
            Row(
                Col(
                    DataCard(
                        "Revenue",
                        subtitle="Q4 2024",
                        status="active",
                        metrics={
                            "Total": "$5,070",
                            "Growth": "+12%",
                            "Accounts": "4",
                        },
                        fields={
                            "Period": "Oct-Dec",
                            "Updated": "Just now",
                        },
                        footer=Button("View report", variant="primary", size="sm"),
                        variant="primary",
                    ),
                    span=12, md=6, lg=3,
                ),
                Col(
                    DataCard(
                        "Users",
                        subtitle="Active",
                        status="warning",
                        metrics={
                            "Online": "128",
                            "New": "24",
                            "Churn": "2.1%",
                        },
                        fields={
                            "Region": "Global",
                            "Plan": "Mixed",
                        },
                    ),
                    span=12, md=6, lg=3,
                ),
                Col(
                    Card(
                        H5("Responsive layout", cls="card-title"),
                        P("Side-by-side on desktop, stacked on mobile."),
                        Switcher(
                            Div(P("Left panel"), cls="p-3 border rounded"),
                            Div(P("Right panel"), cls="p-3 border rounded"),
                            ratio="1fr 1fr",
                            gap=3,
                        ),
                        header="Switcher Demo",
                    ),
                    span=12, md=6, lg=3,
                ),
                Col(
                    Card(
                        Button(
                            "Open Modal",
                            variant="primary",
                            data_bs_toggle="modal",
                            data_bs_target="#demoModal",
                            cls="mb-2 w-100",
                        ),
                        Button(
                            "Open Drawer",
                            variant="secondary",
                            data_bs_toggle="offcanvas",
                            data_bs_target="#demoDrawer",
                            cls="w-100",
                        ),
                        header="Actions",
                    ),
                    span=12, md=6, lg=3,
                ),
                g=3,
                cls="mb-5",
            ),
            H2("SplitPane Demo", cls="h4 mb-3"),
            SplitPane(
                Card(
                    H5("Navigation"),
                    Ul(
                        Li(A("Dashboard", href="#")),
                        Li(A("Projects", href="#")),
                        Li(A("Settings", href="#")),
                    ),
                    header="Master",
                ),
                Card(
                    H5("Content"),
                    P("Drag the divider to resize. On mobile, panes stack."),
                    Div(id="search-results"),
                    header="Detail",
                ),
                initial_ratio="30/70",
                collapsible=True,
                stack_on="md",
            ),
            cls="py-5",
        ),
        Modal(
            P("This is a modal dialog with Bootstrap JS!"),
            P("Click outside or press ESC to close."),
            modal_id="demoModal",
            title="Demo Modal",
            footer=Div(
                Button("Close", variant="secondary", data_bs_dismiss="modal"),
                Button("Save Changes", variant="primary"),
            ),
        ),
        Drawer(
            Div(
                H2("Menu", cls="h5 mb-3"),
                A("Dashboard", href="/dashboard", cls="d-block mb-2"),
                A("Settings", href="/settings", cls="d-block mb-2"),
                A("Profile", href="/profile", cls="d-block mb-2"),
                A("Logout", href="/logout", cls="d-block text-danger"),
            ),
            drawer_id="demoDrawer",
            title="Navigation",
            placement="start",
        ),
    )


@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Type to search...", cls="text-muted")
    filtered = [i for i in ITEMS if q.lower() in i["name"].lower() or q.lower() in i["status"].lower()]
    if not filtered:
        return P(f"No results for '{q}'", cls="text-muted")
    return Table(
        Thead(Tr(Th("ID"), Th("Name"), Th("Status"), Th("Value"))),
        Tbody(*[Tr(Td(i["id"]), Td(i["name"]), Td(i["status"]), Td(i["value"])) for i in filtered]),
        striped=True,
        hover=True,
        cls="mt-3",
    )


if __name__ == "__main__":
    print("Faststrap v0.9.0+ Component Demo")
    print("Visit: http://localhost:5001")
    serve()
