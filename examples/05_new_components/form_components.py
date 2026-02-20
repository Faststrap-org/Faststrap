"""
Form Components Demo
Demonstrates FormGroup, ThemeToggle, and SearchableSelect components
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    return Container(
        H1("Form Components Demo", cls="mb-4"),
        # FormGroup Demo
        Card(
            H5("1. FormGroup - Form Field Wrapper", cls="card-title"),
            P("Wraps inputs with labels, help text, and validation:", cls="text-muted"),
            Form(
                FormGroup(
                    Input(name="email", type="email", placeholder="you@example.com"),
                    label="Email Address",
                    help_text="We'll never share your email with anyone else.",
                    required=True,
                ),
                FormGroup(
                    Input(name="password", type="password"),
                    label="Password",
                    help_text="Must be at least 8 characters",
                    required=True,
                ),
                FormGroup(
                    Select(
                        Option("Select a country", value="", selected=True, disabled=True),
                        Option("United States", value="us"),
                        Option("United Kingdom", value="uk"),
                        Option("Canada", value="ca"),
                        name="country",
                    ),
                    label="Country",
                    required=True,
                ),
                Button("Submit", variant="primary", type="submit"),
                hx_post="/api/submit-form",
                hx_target="#form-result",
            ),
            Div(id="form-result", cls="mt-3"),
            cls="mb-4",
        ),
        # FormGroup with Validation
        Card(
            H5("2. FormGroup - With Validation States", cls="card-title"),
            P("Shows validation feedback:", cls="text-muted"),
            FormGroup(
                Input(name="valid-input", value="valid@example.com", type="email"),
                label="Valid Email",
                success="Looks good!",
                is_valid=True,
            ),
            FormGroup(
                Input(name="invalid-input", value="invalid-email", type="email"),
                label="Invalid Email",
                error="Please enter a valid email address",
                is_invalid=True,
            ),
            cls="mb-4",
        ),
        # ThemeToggle Demo
        Card(
            H5("3. ThemeToggle - Dark/Light Mode Switch", cls="card-title"),
            P("Toggle between light and dark themes:", cls="text-muted"),
            ThemeToggle(
                current_theme="light",
                endpoint="/api/toggle-theme",
                show_label=True,
                label_text="Dark Mode",
            ),
            Alert(
                "Note: Theme changes persist via server-side session storage.",
                variant="info",
                cls="mt-3",
            ),
            cls="mb-4",
        ),
        # SearchableSelect Demo
        Card(
            H5("4. SearchableSelect - Server-Side Search Dropdown", cls="card-title"),
            P("Type to search (replaces Select2/Choices.js):", cls="text-muted"),
            SearchableSelect(
                endpoint="/api/search-countries",
                name="country_search",
                select_id="country-search",
                placeholder="Search countries...",
                min_chars=2,
                debounce=300,
                initial_options=[
                    ("us", "United States"),
                    ("uk", "United Kingdom"),
                    ("ca", "Canada"),
                ],
            ),
            Alert(
                Strong("How it works: "),
                "As you type, HTMX sends requests to the server which returns filtered options. No client-side JavaScript libraries needed!",
                variant="info",
                cls="mt-3",
            ),
            cls="mb-4",
        ),
        cls="my-5",
    )


@app.post("/api/submit-form")
def submit_form(email: str, password: str, country: str):
    """Handle form submission"""
    if not email or not password or not country:
        return Alert("Please fill in all required fields", variant="danger")

    return Alert(
        Icon("check-circle-fill", cls="me-2"),
        f"Form submitted successfully! Email: {email}, Country: {country}",
        variant="success",
        dismissible=True,
    )


@app.post("/api/toggle-theme")
def toggle_theme():
    """Toggle theme (in real app, would update session)"""
    return Alert(
        "Theme toggled! (In a real app, this would update your session)", variant="success"
    )


# Sample countries data
COUNTRIES = [
    ("us", "United States"),
    ("uk", "United Kingdom"),
    ("ca", "Canada"),
    ("au", "Australia"),
    ("de", "Germany"),
    ("fr", "France"),
    ("it", "Italy"),
    ("es", "Spain"),
    ("jp", "Japan"),
    ("cn", "China"),
    ("in", "India"),
    ("br", "Brazil"),
]


@app.get("/api/search-countries")
def search_countries(q: str = ""):
    """Search countries endpoint"""
    if len(q) < 2:
        return ""

    results = [(code, name) for code, name in COUNTRIES if q.lower() in name.lower()]

    if not results:
        return P("No countries found", cls="text-muted text-center p-3")

    options = [
        A(
            name,
            href="#",
            cls="list-group-item list-group-item-action",
            data_value=code,
            hx_on_click=(
                "event.preventDefault();"
                "const sel=document.getElementById('country-search');"
                "if(!sel){return;}"
                "sel.innerHTML='';"
                "const opt=document.createElement('option');"
                f"opt.value='{code}';"
                f"opt.text='{name}';"
                "opt.selected=true;"
                "sel.appendChild(opt);"
                "const inp=document.getElementById('country-search-input');"
                f"if(inp){{inp.value='{name}';}}"
                "const box=document.getElementById('country-search-results');"
                "if(box){box.innerHTML='';}"
            ),
        )
        for code, name in results
    ]

    return Div(*options)


serve()
