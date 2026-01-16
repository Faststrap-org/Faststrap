"""
Example: Calculator Application

Demonstrates: Interactive calculator with HTMX
Components: Button, Card, ButtonGroup
Difficulty: Intermediate

A functional calculator showing:
- HTMX-powered calculations (no JavaScript!)
- Keyboard support
- Calculation history
- Clean, responsive design
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)

# Calculator state (in production, use session)
current_value = "0"
previous_value = ""
operation = ""
history = []


@app.get("/")
def index():
    """Calculator main page"""
    return Container(
        Row(
            Col(
                Card(
                    H3("Calculator", cls="text-center mb-3"),
                    # Display
                    Div(
                        H2(current_value, id="display", cls="text-end p-3 bg-light rounded"),
                        cls="mb-3",
                    ),
                    # Calculator buttons
                    Div(
                        # Row 1: Clear, +/-,%, ÷
                        Div(
                            calc_button("C", "clear", "danger"),
                            calc_button("±", "negate", "secondary"),
                            calc_button("%", "percent", "secondary"),
                            calc_button("÷", "divide", "warning"),
                            cls="d-grid gap-2 mb-2",
                            style={"grid-template-columns": "repeat(4, 1fr)"},
                        ),
                        # Row 2: 7, 8, 9, ×
                        Div(
                            calc_button("7", "digit"),
                            calc_button("8", "digit"),
                            calc_button("9", "digit"),
                            calc_button("×", "multiply", "warning"),
                            cls="d-grid gap-2 mb-2",
                            style={"grid-template-columns": "repeat(4, 1fr)"},
                        ),
                        # Row 3: 4, 5, 6, −
                        Div(
                            calc_button("4", "digit"),
                            calc_button("5", "digit"),
                            calc_button("6", "digit"),
                            calc_button("−", "subtract", "warning"),
                            cls="d-grid gap-2 mb-2",
                            style={"grid-template-columns": "repeat(4, 1fr)"},
                        ),
                        # Row 4: 1, 2, 3, +
                        Div(
                            calc_button("1", "digit"),
                            calc_button("2", "digit"),
                            calc_button("3", "digit"),
                            calc_button("+", "add", "warning"),
                            cls="d-grid gap-2 mb-2",
                            style={"grid-template-columns": "repeat(4, 1fr)"},
                        ),
                        # Row 5: 0, ., =
                        Div(
                            calc_button("0", "digit", style={"grid-column": "span 2"}),
                            calc_button(".", "decimal"),
                            calc_button("=", "equals", "success"),
                            cls="d-grid gap-2",
                            style={"grid-template-columns": "repeat(4, 1fr)"},
                        ),
                    ),
                    cls="p-4 shadow",
                ),
                md=6,
            ),
            # History panel
            Col(
                Card(
                    H5("History", cls="mb-3"),
                    Div(
                        *(
                            [P(h, cls="mb-1 font-monospace") for h in reversed(history[-10:])]
                            if history
                            else P("No calculations yet", cls="text-muted")
                        ),
                        id="history",
                        cls="border rounded p-2",
                        style={"max-height": "400px", "overflow-y": "auto"},
                    ),
                    Button(
                        "Clear History",
                        variant="outline-danger",
                        size="sm",
                        hx_post="/clear-history",
                        hx_target="#history",
                        cls="mt-3",
                    ),
                    cls="p-4",
                ),
                md=6,
            ),
        ),
        cls="py-5",
        style={"max-width": "900px"},
    )


def calc_button(label: str, action: str, variant: str = "outline-secondary", **kwargs):
    """Helper to create calculator button"""
    return Button(
        label,
        variant=variant,
        hx_post=f"/calc/{action}/{label}",
        hx_target="#display",
        hx_swap="innerHTML",
        **kwargs,
    )


@app.post("/calc/digit/{digit}")
def handle_digit(digit: str):
    """Handle digit input"""
    global current_value
    if current_value == "0":
        current_value = digit
    else:
        current_value += digit
    return current_value


@app.post("/calc/decimal/{dot}")
def handle_decimal(dot: str):
    """Handle decimal point"""
    global current_value
    if "." not in current_value:
        current_value += "."
    return current_value


@app.post("/calc/clear/{c}")
def handle_clear(c: str):
    """Clear calculator"""
    global current_value, previous_value, operation
    current_value = "0"
    previous_value = ""
    operation = ""
    return current_value


@app.post("/calc/{op}/{symbol}")
def handle_operation(op: str, symbol: str):
    """Handle operations"""
    global current_value, previous_value, operation, history

    if op == "negate":
        current_value = str(-float(current_value))
    elif op == "percent":
        current_value = str(float(current_value) / 100)
    elif op in ["add", "subtract", "multiply", "divide"]:
        previous_value = current_value
        operation = op
        current_value = "0"
    elif op == "equals" and previous_value and operation:
        a = float(previous_value)
        b = float(current_value)

        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else "Error"

        # Add to history
        op_symbols = {"add": "+", "subtract": "−", "multiply": "×", "divide": "÷"}
        history.append(f"{previous_value} {op_symbols[operation]} {current_value} = {result}")

        current_value = str(result)
        previous_value = ""
        operation = ""

    return current_value


@app.post("/clear-history")
def clear_history():
    """Clear calculation history"""
    global history
    history = []
    return P("No calculations yet", cls="text-muted")


if __name__ == "__main__":
    serve(port=5019)
