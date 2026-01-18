"""
Faststrap PWA Demo
Run with: python examples/pwa_demo.py
"""

from fasthtml.common import *

from faststrap import *
from faststrap.pwa import add_pwa

app = FastHTML()

# 1. Add Bootstrap (Standard)
add_bootstrap(app, theme="purple-magic", mode="dark")

# 2. Add PWA capabilities (New in v0.5.2)
add_pwa(
    app,
    name="Faststrap PWA Demo",
    short_name="FS PWA",
    description="A demo of Faststrap PWA capabilities",
    theme_color="#6F42C1",  # Matches purple-magic primary
    icon_path="https://placehold.co/512x512.png",  # Reliable placeholder for demo
)


@app.route("/")
def home():
    return Container(
        # Mobile-First Header
        Navbar(
            brand="Faststrap PWA",
            sticky="top",
            expand="lg",
            items=[
                A("Home", cls="nav-link active"),
                A("Settings", cls="nav-link"),
            ],
        ),
        # Main Content
        Div(
            Hero(
                "PWA Ready 🚀",
                "This app is installable! Open it on mobile to see the magic.",
                Button(
                    "Open Sheet",
                    cls="btn btn-primary",
                    data_bs_toggle="offcanvas",
                    data_bs_target="#demoSheet",
                ),
                cls="text-center py-5",
            ),
            # Feature Grid
            Row(
                Col(Card("Manifest Auto-Generated", header="✅ Zero Config"), cls="mb-3", md=4),
                Col(Card("Service Worker Included", header="✅ Offline Ready"), cls="mb-3", md=4),
                Col(Card("Mobile Components", header="✅ Bottom Nav & Sheets"), cls="mb-3", md=4),
            ),
            cls="py-4",
        ),
        # New Component: Bottom Sheet
        Sheet(
            Div(
                H5("Mobile Actions"),
                P("This is a native-feeling bottom sheet."),
                Button("Close", cls="btn btn-outline-secondary w-100", data_bs_dismiss="offcanvas"),
            ),
            sheet_id="demoSheet",
            title="Options",
        ),
        # New Component: Bottom Nav (Mobile Only)
        # Visible only on small screens
        Div(
            BottomNav(
                BottomNavItem("Home", icon="house-fill", active=True),
                BottomNavItem("Search", icon="search"),
                BottomNavItem("Profile", icon="person-circle"),
                variant="dark",
                fixed=True,
            ),
            cls="d-md-none",
        ),
        # New Component: Smart Install Prompt
        InstallPrompt(title="Install Faststrap Demo", delay=1000),  # Show quickly for demo
    )


serve()
