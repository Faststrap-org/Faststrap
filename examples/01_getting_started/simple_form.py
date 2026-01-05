"""
Example: Simple Form

Demonstrates: Building forms with Faststrap
Components: Input, Select, Switch, Button, Alert
Difficulty: Beginner

Learn how to create forms with validation and feedback.
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return Container(
        Card(
            H3("Contact Form", cls="mb-4"),
            Form(
                Input("name", label="Your Name", placeholder="John Doe", required=True),
                Input(
                    "email",
                    label="Email Address",
                    input_type="email",
                    placeholder="john@example.com",
                    required=True,
                ),
                Select(
                    "subject",
                    ("", "-- Select Subject --"),
                    ("general", "General Inquiry"),
                    ("support", "Technical Support"),
                    ("feedback", "Feedback"),
                    label="Subject",
                    required=True,
                ),
                Input(
                    "message",
                    label="Message",
                    input_type="textarea",
                    placeholder="Your message here...",
                    rows=4,
                    required=True,
                ),
                Switch("newsletter", label="Subscribe to newsletter"),
                Button("Submit", variant="primary", type="submit", cls="w-100 mt-3"),
                method="post",
                action="/submit",
            ),
            cls="p-4 shadow",
        ),
        cls="py-5",
        style={"max-width": "600px"},
    )


@app.route("/submit")
def post(name: str, email: str, subject: str, message: str, newsletter: bool = False):
    return Container(
        Alert(
            H4("Thank you!", cls="alert-heading"),
            P(f"We received your message, {name}!"),
            P(f"We'll respond to {email} soon."),
            variant="success",
        ),
        Button("Send Another", href="/", variant="primary"),
        cls="py-5",
    )


if __name__ == "__main__":
    serve(port=5007)
