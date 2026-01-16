"""
Example: Blog Application

Demonstrates: Complete blog platform with posts, comments, and admin
Components: Card, Button, Badge, Alert, Modal, Table, Form components
Difficulty: Intermediate

A full-featured blog application showing:
- Post listing and detail pages
- Markdown content support
- Comments system
- Admin dashboard for managing posts
- Responsive design
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)

# Sample blog posts (in production, use a database)
posts = [
    {
        "id": 1,
        "title": "Getting Started with Faststrap",
        "slug": "getting-started-faststrap",
        "author": "John Doe",
        "date": "2026-01-01",
        "excerpt": "Learn how to build beautiful web UIs in pure Python with Faststrap.",
        "content": "Faststrap makes it easy to build modern web applications...",
        "tags": ["tutorial", "beginner"],
        "comments": 5,
    },
    {
        "id": 2,
        "title": "Building a Dashboard with DashboardLayout",
        "slug": "building-dashboard",
        "author": "Jane Smith",
        "date": "2026-01-02",
        "excerpt": "Create professional admin panels with Faststrap's DashboardLayout component.",
        "content": "The DashboardLayout component provides everything you need...",
        "tags": ["tutorial", "advanced"],
        "comments": 3,
    },
    {
        "id": 3,
        "title": "Zero-JS Animations with Fx",
        "slug": "zero-js-animations",
        "author": "Bob Johnson",
        "date": "2026-01-03",
        "excerpt": "Add beautiful animations without writing a single line of JavaScript.",
        "content": "Faststrap's Fx module provides pure CSS animations...",
        "tags": ["effects", "design"],
        "comments": 8,
    },
]


@app.get("/")
def index():
    """Blog home page with post listing"""
    return Container(
        # Header
        Div(
            H1("My Faststrap Blog", cls=f"{Fx.fade_in}"),
            P(
                "Tutorials, tips, and insights about web development",
                cls=f"text-muted {Fx.fade_in} {Fx.delay_sm}",
            ),
            cls="text-center my-5",
        ),
        # Posts grid
        Col(
            *[
                Row(
                    Card(
                        Div(
                            H5(post["title"], cls="card-title"),
                            P(
                                Icon("person", cls="me-1"),
                                post["author"],
                                " • ",
                                Icon("calendar", cls="me-1"),
                                post["date"],
                                cls="text-muted small mb-2",
                            ),
                            P(post["excerpt"], cls="card-text"),
                            Div(
                                *[
                                    Badge(tag, variant="secondary", cls="me-1")
                                    for tag in post["tags"]
                                ],
                                cls="mb-3",
                            ),
                            Div(
                                Button(
                                    "Read More", href=f"/post/{post['slug']}", variant="primary"
                                ),
                                Span(
                                    Icon("chat-left-text", cls="me-1"),
                                    f"{post['comments']} comments",
                                    cls="text-muted small ms-3",
                                ),
                                cls="d-flex justify-content-between align-items-center",
                            ),
                        ),
                        cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.shadow_soft} mb-4",
                    ),
                    md=12,
                )
                for post in posts
            ],
            cls="mb-4",
        ),
        cls="py-4",
    )


@app.get("/post/{slug}")
def post_detail(slug: str):
    """Individual blog post page"""
    # Find post by slug
    post = next((p for p in posts if p["slug"] == slug), None)

    if not post:
        return Container(
            Alert("Post not found", variant="danger"),
            Button("Back to Blog", href="/", variant="primary"),
        )

    return Container(
        # Back button
        Button(Icon("arrow-left"), " Back to Blog", href="/", variant="link", cls="mb-3"),
        # Post content
        Card(
            H1(post["title"], cls="mb-3"),
            P(
                Icon("person", cls="me-1"),
                post["author"],
                " • ",
                Icon("calendar", cls="me-1"),
                post["date"],
                cls="text-muted mb-3",
            ),
            Div(*[Badge(tag, variant="secondary", cls="me-1") for tag in post["tags"]], cls="mb-4"),
            P(post["content"], cls="lead"),
            cls="p-4",
        ),
        # Comments section
        Card(
            H4("Comments", cls="mb-3"),
            P(f"{post['comments']} comments", cls="text-muted"),
            # Comment form
            Form(
                Input("name", label="Your Name", placeholder="John Doe", required=True),
                Input("comment", label="Comment", input_type="textarea", rows=3, required=True),
                Button("Post Comment", variant="primary", type="submit"),
                method="post",
                action=f"/post/{slug}/comment",
            ),
            cls="p-4 mt-4",
        ),
        cls="py-4",
    )


@app.post("/post/{slug}/comment")
def create_comment(slug: str, name: str, comment: str):
    """Handle comment submission"""
    return Container(
        Alert(
            H4("Comment Posted!", cls="alert-heading"),
            P(f"Thank you, {name}! Your comment has been added."),
            variant="success",
        ),
        Button("Back to Post", href=f"/post/{slug}", variant="primary"),
        cls="py-4",
    )


@app.get("/admin")
def admin_dashboard():
    """Admin dashboard for managing posts"""
    return Container(
        H1("Blog Admin", cls="mb-4"),
        Button(Icon("plus"), " New Post", variant="primary", cls="mb-3"),
        Card(
            Table(
                THead(Tr(Th("Title"), Th("Author"), Th("Date"), Th("Comments"), Th("Actions"))),
                TBody(
                    *[
                        Tr(
                            Td(post["title"]),
                            Td(post["author"]),
                            Td(post["date"]),
                            Td(str(post["comments"])),
                            Td(
                                Button(
                                    Icon("pencil"), size="sm", variant="outline-primary", cls="me-1"
                                ),
                                Button(Icon("trash"), size="sm", variant="outline-danger"),
                            ),
                        )
                        for post in posts
                    ]
                ),
                striped=True,
                hover=True,
            ),
            header="All Posts",
        ),
        cls="py-4",
    )


if __name__ == "__main__":
    serve(port=5019)
