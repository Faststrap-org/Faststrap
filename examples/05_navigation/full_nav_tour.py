"""
Faststrap v0.9.0 Full Tour

Combines all 7 new v0.9.0 components in a study dashboard mini-app:
- Math: rendered equations in study notes
- Switcher: responsive note layout
- SplitPane: master/detail problem browser
- SearchBar: search problems by topic
- ProfileDropdown: user menu
- DataCard: problem metadata
- FilePreview: attached resource preview
"""

from fasthtml.common import (
    A,
    Div,
    FastHTML,
    H1,
    H2,
    H3,
    H4,
    Li,
    P,
    Small,
    Ul,
    serve,
)

from faststrap import (
    Col,
    Container,
    DataCard,
    FilePreview,
    Math,
    Navbar,
    ProfileDropdown,
    Row,
    SearchBar,
    SplitPane,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="light")

PROBLEMS = [
    {
        "id": 1,
        "topic": "Calculus",
        "title": "Derivative of e^x",
        "equation": r"\frac{d}{dx} e^x = e^x",
        "difficulty": "Easy",
        "status": "solved",
        "attachment": "notes.pdf",
    },
    {
        "id": 2,
        "topic": "Physics",
        "title": "Kinetic Energy",
        "equation": r"E_k = \frac{1}{2}mv^2",
        "difficulty": "Medium",
        "status": "in-progress",
        "attachment": "diagram.png",
    },
    {
        "id": 3,
        "topic": "Chemistry",
        "title": "Ideal Gas Law",
        "equation": r"PV = nRT",
        "difficulty": "Easy",
        "status": "solved",
        "attachment": "data.csv",
    },
]


@app.get("/")
def home():
    return Container(
        Navbar(
            SearchBar(
                placeholder="Search problems...",
                endpoint="/search",
                target="#problem-list",
            ),
            ProfileDropdown(
                "Student User",
                subtitle="Physics 101",
                items=[
                    ("Profile", "/profile"),
                    ("Bookmarks", "/bookmarks"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="StudyHub",
            brand_href="/",
        ),
        H1("Study Dashboard", cls="display-5 fw-bold mb-4 mt-4"),
        Row(
            Col(
                DataCard(
                    "Calculus",
                    subtitle="Chapter 3",
                    status="active",
                    metrics={
                        "Problems": "24",
                        "Solved": "18",
                        "Accuracy": "75%",
                    },
                    fields={
                        "Due": "Tomorrow",
                        "Attempts": "3",
                    },
                ),
                span=12, md=6, lg=3,
            ),
            Col(
                DataCard(
                    "Physics",
                    subtitle="Chapter 5",
                    status="warning",
                    metrics={
                        "Problems": "16",
                        "Solved": "8",
                        "Accuracy": "50%",
                    },
                    fields={
                        "Due": "In 3 days",
                        "Attempts": "5",
                    },
                ),
                span=12, md=6, lg=3,
            ),
            Col(
                DataCard(
                    "Chemistry",
                    subtitle="Chapter 2",
                    status="success",
                    metrics={
                        "Problems": "12",
                        "Solved": "12",
                        "Accuracy": "100%",
                    },
                    fields={
                        "Due": "Completed",
                        "Attempts": "1",
                    },
                ),
                span=12, md=6, lg=3,
            ),
            Col(
                DataCard(
                    "Statistics",
                    subtitle="Chapter 4",
                    status="neutral",
                    metrics={
                        "Problems": "20",
                        "Solved": "0",
                        "Accuracy": "—",
                    },
                    fields={
                        "Due": "Next week",
                        "Attempts": "0",
                    },
                ),
                span=12, md=6, lg=3,
            ),
            g=3,
        ),
        H2("Problem Browser", cls="h4 mb-3 mt-4"),
        SplitPane(
            Div(id="problem-list"),
            Div(
                H4("Problem Detail", cls="mb-3"),
                Div(
                    P("Select a problem from the list to view details.",
                      cls="text-muted"),
                    id="problem-detail",
                ),
            ),
            initial_ratio="40/60",
            stack_on="md",
        ),
        cls="my-5",
    )


@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Type a topic or keyword...", cls="text-muted")
    filtered = [p for p in PROBLEMS if q.lower() in p["topic"].lower() or q.lower() in p["title"].lower()]
    if not filtered:
        return P(f"No problems matching '{q}'", cls="text-muted")
    return Ul(
        *[
            Li(
                A(
                    f"{p['title']} ({p['topic']})",
                    href=f"/problem/{p['id']}",
                    cls="text-decoration-none",
                ),
                Small(p["difficulty"], cls="text-muted d-block"),
            )
            for p in filtered
        ],
        cls="list-unstyled",
    )


@app.get("/problem/{pid}")
def problem_detail(pid: int):
    problem = next((p for p in PROBLEMS if p["id"] == pid), None)
    if not problem:
        return P("Problem not found.", cls="text-danger")
    return Container(
        H3(problem["title"], cls="h5 mb-3"),
        Math(problem["equation"], display_mode=True),
        P(f"Difficulty: {problem['difficulty']}", cls="text-muted"),
        P(f"Attachment: {problem['attachment']}", cls="text-muted"),
        FilePreview(
            src=f"https://via.placeholder.com/400x300?text={problem['attachment']}",
            title=problem["attachment"],
            height="150px",
        ),
        A("Back to list", href="/", cls="btn btn-secondary btn-sm mt-3"),
    )


if __name__ == '__main__':
    serve()
