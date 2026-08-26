"""
03_forms/input_groups.py
Demonstrates: InputGroup, InputGroupText, Radio, Range

- InputGroup & InputGroupText: Prefix and suffix text/button addons on form inputs
- Radio: Single radio buttons, grouped options, inline and reverse styling
- Range: Native HTML range slider with live feedback
"""

from fasthtml.common import FastHTML, H1, H2, H3, P, Div, Span, Form, serve
from faststrap import (
    add_bootstrap,
    Container,
    InputGroup,
    InputGroupText,
    Input,
    Button,
    Radio,
    Range,
    FormGroup,
    Card,
    Stack,
    Row,
    Col,
    Icon,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Input Groups, Radios & Sliders", cls="display-5 fw-bold mb-2"),
        P("Addon prefixes, grouped choices, and interactive range controls.", cls="lead text-muted mb-5"),

        # ── InputGroup & InputGroupText ────────────────────────────────────
        H2("InputGroup & InputGroupText", cls="h4 fw-semibold mb-1"),
        P("Attach text, currency symbols, or buttons directly to inputs.", cls="text-muted mb-3"),
        Card(
            Stack(
                # Username with @ addon
                FormGroup(
                    InputGroup(
                        InputGroupText("@"),
                        Input("username", placeholder="username", required=True),
                    ),
                    label="Username",
                ),
                # Price with $ prefix and .00 suffix
                FormGroup(
                    InputGroup(
                        InputGroupText("$"),
                        Input("price", placeholder="0", input_type="number", step="0.01"),
                        InputGroupText(".00"),
                    ),
                    label="Amount",
                ),
                # Search with action button
                FormGroup(
                    InputGroup(
                        Input("query", placeholder="Search catalog..."),
                        Button(Icon("search", cls="me-1"), "Search", variant="primary"),
                    ),
                    label="Search with Button Addon",
                ),
                gap=3,
            ),
            header="InputGroup Addon Patterns",
            cls="mb-5",
        ),

        # ── Radio Buttons ──────────────────────────────────────────────────
        H2("Radio Choices", cls="h4 fw-semibold mb-1"),
        P("Single-select radio inputs with standard, inline, and reverse alignments.", cls="text-muted mb-3"),
        Card(
            Row(
                Col(
                    H3("Standard Stacked", cls="h6 fw-bold mb-3"),
                    Radio("billing", label="Monthly Billing ($29/mo)", value="monthly", checked=True),
                    Radio("billing", label="Annual Billing ($290/yr - Save 20%)", value="annual"),
                    Radio("billing", label="Enterprise Custom", value="enterprise", disabled=True),
                    span=12, md=6, cls="mb-3",
                ),
                Col(
                    H3("Inline Choices", cls="h6 fw-bold mb-3"),
                    Div(
                        Radio("size", label="Small", value="sm", inline=True),
                        Radio("size", label="Medium", value="md", value_checked=True, inline=True, checked=True),
                        Radio("size", label="Large", value="lg", inline=True),
                        cls="d-flex gap-3",
                    ),
                    H3("Reverse Label Alignment", cls="h6 fw-bold mt-4 mb-3"),
                    Radio("notifications", label="Email Alerts", value="email", reverse=True, checked=True),
                    Radio("notifications", label="SMS Alerts", value="sms", reverse=True),
                    span=12, md=6, cls="mb-3",
                ),
            ),
            header="Radio Form Controls",
            cls="mb-5",
        ),

        # ── Range Sliders ──────────────────────────────────────────────────
        H2("Range Sliders", cls="h4 fw-semibold mb-1"),
        P("Native slider controls with min, max, step, and oninput update triggers.", cls="text-muted mb-3"),
        Card(
            Stack(
                FormGroup(
                    Range(
                        "volume",
                        min_val=0,
                        max_val=100,
                        value=75,
                        step=5,
                        oninput="document.getElementById('vol-val').textContent = this.value + '%'",
                    ),
                    label=Div(
                        Span("Volume: "),
                        Span("75%", id="vol-val", cls="fw-bold text-primary"),
                    ),
                ),
                FormGroup(
                    Range(
                        "temperature",
                        min_val=16,
                        max_val=30,
                        value=22,
                        step=0.5,
                        oninput="document.getElementById('temp-val').textContent = this.value + '°C'",
                    ),
                    label=Div(
                        Span("Target Temperature: "),
                        Span("22°C", id="temp-val", cls="fw-bold text-success"),
                    ),
                ),
                gap=3,
            ),
            header="Range Inputs with Dynamic Display",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
