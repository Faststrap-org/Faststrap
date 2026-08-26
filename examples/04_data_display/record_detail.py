"""
04_data_display/record_detail.py
Demonstrates: KeyValueList, RecordDetail, JsonViewer

- KeyValueList: simple key-value pairs (settings, metadata)
- RecordDetail: structured detail view with title, subtitle, and sections
- JsonViewer: collapsible JSON tree for API responses and debug data
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    KeyValueList,
    RecordDetail,
    JsonViewer,
    Card,
    Badge,
    Button,
    Row,
    Col,
    Stack,
)

app = FastHTML()
add_bootstrap(app, theme="gray-mist", mode="light")

USER_RECORD = {
    "id": "usr_01HX9FWQXKJ3P",
    "name": "Alice Chen",
    "email": "alice@example.com",
    "role": "Senior Engineer",
    "status": "active",
    "created_at": "2023-04-12T09:21:00Z",
    "last_login": "2024-12-07T14:33:12Z",
    "plan": "Pro",
    "usage": {"api_calls": 48290, "storage_gb": 12.4, "bandwidth_gb": 87.2},
    "permissions": ["read", "write", "admin"],
}


@app.get("/")
def home():
    return Container(
        H1("Record Detail Components", cls="display-5 fw-bold mb-2"),
        P("For displaying structured data, API responses, and detail views.", cls="lead text-muted mb-5"),

        # ── KeyValueList ───────────────────────────────────────────────────
        H2("KeyValueList", cls="h4 fw-semibold mb-1"),
        P("A clean key-value display. Use a dict or list of (key, value) tuples.", cls="text-muted mb-3"),
        Row(
            Col(
                Card(
                    KeyValueList(
                        {
                            "Status": Badge("Active", cls="bg-success"),
                            "Plan": "Pro",
                            "API Calls": "48,290",
                            "Storage": "12.4 GB",
                            "Member Since": "Apr 2023",
                        },
                        striped=True,
                    ),
                    header="Account Overview (striped=True)",
                ),
                span=12, md=6, cls="mb-4",
            ),
            Col(
                Card(
                    KeyValueList(
                        {
                            "CPU Usage": "34%",
                            "Memory": "6.2 / 16 GB",
                            "Disk": "128 / 500 GB",
                            "Uptime": "14d 6h 42m",
                            "Region": "us-east-1",
                        },
                        compact=True,
                    ),
                    header="Server Metrics (compact=True)",
                ),
                span=12, md=6, cls="mb-4",
            ),
        ),

        # ── RecordDetail ───────────────────────────────────────────────────
        H2("RecordDetail", cls="h4 fw-semibold mb-1"),
        P("Full detail view with title, subtitle, and grouped key-value sections.", cls="text-muted mb-3"),
        RecordDetail(
            {
                "User ID": USER_RECORD["id"],
                "Name": USER_RECORD["name"],
                "Email": USER_RECORD["email"],
                "Role": USER_RECORD["role"],
                "Status": Badge("Active", cls="bg-success"),
                "Plan": USER_RECORD["plan"],
                "Created": USER_RECORD["created_at"],
                "Last Login": USER_RECORD["last_login"],
            },
            title="Alice Chen",
            subtitle="Senior Engineer — Pro Plan",
            actions=[
                Button("Edit User", variant="outline-primary", size="sm"),
                Button("Suspend", variant="outline-danger", size="sm"),
            ],
            cls="mb-5",
        ),

        # ── JsonViewer ─────────────────────────────────────────────────────
        H2("JsonViewer", cls="h4 fw-semibold mb-1"),
        P("Collapsible JSON tree — useful for API responses and debug output.", cls="text-muted mb-3"),
        Card(
            JsonViewer(USER_RECORD, title="GET /api/users/usr_01HX9FWQXKJ3P", expanded=True),
            header="API Response Viewer",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
