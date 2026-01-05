"""
Example: Hello World

Demonstrates: Minimal Faststrap application
Components: Container, Card, Button
Difficulty: Beginner

This is your first Faststrap app! It shows how to:
- Set up a basic FastHTML app with Faststrap
- Use Container for layout
- Create a Card component
- Add a Button with styling
"""

from fasthtml.common import *

from faststrap import *

# Create FastHTML app with Faststrap
app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return Container(
        Card(
            H1("Welcome to Faststrap! 🎉", cls="card-title"),
            P(
                "You've just created your first Faststrap application. "
                "This is a Card component inside a Container.",
                cls="card-text",
            ),
            Button("Click Me!", variant="primary", onclick="alert('Hello from Faststrap!')"),
            cls="mt-5 shadow",
        ),
        cls="py-5",
    )


# Run the app
if __name__ == "__main__":
    serve(port=5020)
