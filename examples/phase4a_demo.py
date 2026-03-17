"""Phase 4A Component Demo.

Shows simple and advanced usage of new Phase 4A components:
- Table
- Accordion
- ListGroup & Collapse
- Form Controls (Checkbox, Radio, Switch, Range)
- Input Group & Floating Labels
"""

from fasthtml.common import H1, H2, H5, H6, Div, FastHTML, P, serve

from faststrap import (
    Accordion,
    AccordionItem,
    Badge,
    Button,
    Card,
    Checkbox,
    Col,
    Collapse,
    Container,
    FloatingLabel,
    Input,
    InputGroup,
    InputGroupText,
    ListGroup,
    ListGroupItem,
    Radio,
    Range,
    Row,
    Switch,
    # New Components
    Table,
    TBody,
    TCell,
    THead,
    TRow,
    add_bootstrap,
    create_theme,
)

# Initialize app with standard FastHTML pattern
app = FastHTML()

custom_theme = create_theme(
    primary="#6F42C1",
    secondary="#E9ECEF",
    info="#17A2B8",
    warning="#FFC107",
    danger="#DC3545",
    success="#28A745",
    light="#F8F9FA",
    dark="#343A40",
)
# add_bootstrap(app, theme=custom_theme, mode="light", include_favicon=True)

# Alternative exa

# Use Faststrap's add_bootstrap for correct asset management and theming
add_bootstrap(
    app,
    theme="orange-sunset",
    mode="dark",
)


@app.route("/")
def home():
    """Render the Phase 4A Demo Page."""
    return Container(
        H1("FastStrap Phase 4A Showcase", cls="mb-4"),
        P("Demonstrating the new components added in v0.4.0.", cls="lead mb-5"),
        # 1. Tables
        H2("1. Tables", cls="mt-5 mb-3"),
        Row(
            Col(
                Card(
                    H5("Simple Table", cls="card-title mb-3"),
                    Table(
                        THead(TRow(TCell("First", header=True), TCell("Last", header=True))),
                        TBody(
                            TRow(TCell("John"), TCell("Doe")),
                            TRow(TCell("Jane"), TCell("Smith")),
                        ),
                        striped=True,
                        hover=True,
                    ),
                    body_cls="p-4",
                ),
                width=12,
                xl=6,
            ),
            Col(
                Card(
                    H5("Advanced Table (Responsive, Dark, Bordered)", cls="card-title mb-3"),
                    Table(
                        THead(
                            TRow(
                                TCell("#", header=True),
                                TCell("User", header=True),
                                TCell("Role", header=True),
                                TCell("Status", header=True),
                            ),
                            variant="dark",
                        ),
                        TBody(
                            TRow(
                                TCell("1"),
                                TCell("Admin"),
                                TCell("Super"),
                                TCell("Active", variant="success"),
                            ),
                            TRow(
                                TCell("2"),
                                TCell("User"),
                                TCell("Editor"),
                                TCell("Pending", variant="warning"),
                            ),
                            TRow(
                                TCell("3"),
                                TCell("Guest"),
                                TCell("Viewer"),
                                TCell("Inactive", variant="secondary"),
                            ),
                        ),
                        bordered=True,
                        responsive=True,
                        small=True,
                    ),
                    body_cls="p-4",
                ),
                width=12,
                xl=6,
            ),
        ),
        # 2. Accordion
        H2("2. Accordion", cls="mt-4 mb-3"),
        Row(
            Col(
                Card(
                    H5("Basic Accordion", cls="card-title mb-3"),
                    Accordion(
                        AccordionItem(
                            "This is the first item's body.",
                            title="Accordion Item #1",
                            expanded=True,
                        ),
                        AccordionItem("This is the second item's body.", title="Accordion Item #2"),
                        AccordionItem("This is the third item's body.", title="Accordion Item #3"),
                        accordion_id="basic-accordion",
                    ),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
            Col(
                Card(
                    H5("Flush & Always Open", cls="card-title mb-3"),
                    Accordion(
                        AccordionItem(
                            "Placeholder content for this accordion.",
                            title="Flush Item #1",
                            header_cls="bg-light",
                        ),
                        AccordionItem(
                            "More content here.", title="Flush Item #2", header_cls="text-primary"
                        ),
                        flush=True,
                        always_open=True,
                        accordion_id="flush-accordion",
                    ),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
        ),
        # 3. ListGroup & Collapse
        H2("3. ListGroup & Collapse", cls="mt-4 mb-3"),
        Row(
            Col(
                Card(
                    H5("List Group Variations", cls="card-title mb-3"),
                    ListGroup(
                        ListGroupItem("An item"),
                        ListGroupItem("A second item", active=True),
                        ListGroupItem("A third item", disabled=True),
                        ListGroupItem("A link item", href="#", action=True),
                        ListGroupItem(
                            "With badge", badge=Badge("14", variant="primary", rounded=True)
                        ),
                    ),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
            Col(
                Card(
                    H5("Collapse Demo", cls="card-title mb-3"),
                    Button(
                        "Toggle Collapse",
                        variant="primary",
                        data_bs_toggle="collapse",
                        data_bs_target="#demo-collapse",
                        cls="mb-2",
                    ),
                    Collapse(
                        Card(
                            Div(
                                "This content is hidden by default but shown via toggle.", cls="p-3"
                            )
                        ),
                        collapse_id="demo-collapse",
                        cls="mt-2",
                    ),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
        ),
        # 4. Form Controls
        H2("4. New Form Controls", cls="mt-4 mb-3"),
        Row(
            Col(
                Card(
                    H5("Checks & Radios", cls="card-title mb-3"),
                    H6("Checkboxes"),
                    Checkbox("c1", label="Default checkbox"),
                    Checkbox("c2", label="Checked checkbox", checked=True),
                    Checkbox("c3", label="Disabled checkbox", disabled=True),
                    H6("Switches", cls="mt-3"),
                    Switch("s1", label="Default switch"),
                    Switch("s2", label="Checked switch", checked=True),
                    H6("Radios", cls="mt-3"),
                    Radio("radios", label="Option 1", value="r1", checked=True),
                    Radio("radios", label="Option 2", value="r2"),
                    H6("Inline", cls="mt-3"),
                    Div(
                        Checkbox("i1", label="1", inline=True),
                        Checkbox("i2", label="2", inline=True),
                        Radio("inline_rad", label="A", value="i3", inline=True),
                        Radio("inline_rad", label="B", value="i4", inline=True),
                    ),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
            Col(
                Card(
                    H5("Range, Input Groups & Floating Labels", cls="card-title mb-3"),
                    H6("Range"),
                    Range("range1", label="Example range", min_val=0, max_val=5, step=0.5),
                    H6("Input Groups", cls="mt-3"),
                    InputGroup(
                        InputGroupText("@"), Input("username", placeholder="Username"), cls="mb-3"
                    ),
                    InputGroup(
                        Input("amount", placeholder="Amount"), InputGroupText(".00"), cls="mb-3"
                    ),
                    H6("Floating Labels", cls="mt-3"),
                    FloatingLabel(
                        "float_email", label="Email address", input_type="email", cls="mb-3"
                    ),
                    FloatingLabel("float_pass", label="Password", input_type="password"),
                    body_cls="p-4",
                ),
                width=12,
                md=6,
            ),
        ),
        cls="py-5",
    )


if __name__ == "__main__":
    print("=" * 60)
    print("Run this example with: python examples/phase4a_demo.py")
    print("Then visit: http://localhost:5002")
    print("=" * 60)
    serve(port=5002)
