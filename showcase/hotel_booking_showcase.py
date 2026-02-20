"""
Showcase - Hotel Booking Landing
Inspired by the uploaded booking design.
Built with Faststrap components, presets, and zero custom JavaScript.
"""

from __future__ import annotations

import random
from datetime import datetime
from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H4,
    A,
    Br,
    Div,
    FastHTML,
    Img,
    P,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Button,
    Card,
    Col,
    Container,
    FooterModern,
    FormGroup,
    Fx,
    Icon,
    Input,
    Navbar,
    Row,
    Select,
    Testimonial,
    add_bootstrap,
)
from faststrap.presets import ActiveSearch, AutoRefresh, LazyLoad, LoadingButton, toast_response

app = FastHTML()
add_bootstrap(app, font_family="Montserrat")

ROOMS = [
    {
        "name": "Twin Room",
        "price": "$92 / night",
        "image": "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=1200",
        "desc": "Comfortable room for quick city stays with modern interior.",
    },
    {
        "name": "Deluxe Room",
        "price": "$129 / night",
        "image": "https://images.unsplash.com/photo-1591088398332-8a7791972843?w=1200",
        "desc": "Elegant furnishing and premium amenities for relaxed travel.",
    },
    {
        "name": "Family Suite",
        "price": "$189 / night",
        "image": "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200",
        "desc": "Spacious multi-bed suite for family vacations and group trips.",
    },
    {
        "name": "Presidential Suite",
        "price": "$420 / night",
        "image": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=1200",
        "desc": "Top-tier suite with skyline view and private lounge area.",
    },
]

OFFERS = [
    (
        "Weekend Getaway Package",
        "20% Off",
        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200",
    ),
    (
        "Family Vacation Deal",
        "35% Off",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200",
    ),
    (
        "Spa & Wellness Retreat",
        "15% Off",
        "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=1200",
    ),
]

TEAM = [
    ("Michael Drew", "Manager", "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400"),
    ("Frank Jones", "Host", "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=400"),
    (
        "Mya Mullins",
        "Reception",
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400",
    ),
    ("Ruby Nguyen", "Care", "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400"),
]

TESTIMONIALS = [
    (
        "The booking flow was effortless and the room exceeded expectations.",
        "Melissa Adam",
        "VIA",
    ),
    (
        "Great hospitality and smooth check-in. Perfect business stay.",
        "Ricky Smith",
        "NYC",
    ),
    (
        "Family-friendly service with clean rooms and excellent breakfast.",
        "Leslie May",
        "LA",
    ),
]

SHOWCASE_CSS = """
body { background: #f1f2f6; }
.hs-nav { background: #fff; border-radius: .75rem; }
.hs-hero { background: linear-gradient(120deg, rgba(12,17,28,.8), rgba(12,17,28,.55)), url('https://images.unsplash.com/photo-1455587734955-081b22074882?w=1400') center/cover no-repeat; }
.hs-white-card { background: #fff; border-radius: 1rem; }
.hs-soft { background: #f8f9ff; border-radius: 1rem; }
.hs-dark-cta { background: linear-gradient(140deg, #0f1a2c, #1f2d49); border-radius: 1rem; }
.hs-sticky-booking { margin-top: -2.2rem; position: relative; z-index: 2; }
"""


def room_card(room: dict[str, str], idx: int = 0) -> Any:
    return Card(
        Img(src=room["image"], cls="w-100 object-fit-cover rounded-top", style="height:220px;"),
        Div(
            Div(
                Strong(room["name"], cls="fs-5"),
                Badge(room["price"], variant="light", cls="text-dark"),
                cls="d-flex justify-content-between align-items-center mb-2",
            ),
            P(room["desc"], cls="text-muted mb-3"),
            Button("Check Availability", variant="danger", size="sm"),
            cls="p-3",
        ),
        cls=f"border-0 shadow-sm h-100 {Fx.base} {Fx.fade_in} {Fx.hover_lift} {Fx.delay_sm if idx % 2 else ''}",
    )


@app.get("/")
def home() -> Any:
    return Div(
        Style(SHOWCASE_CSS),
        Container(
            # Header
            Div(
                Navbar(
                    brand=Span("Booking.com", cls="fw-bold text-danger"),
                    items=[
                        Div(
                            A("Home", href="#home", cls="nav-link"),
                            A("Rooms", href="#rooms", cls="nav-link"),
                            A("Deals", href="#deals", cls="nav-link"),
                            A("Contact", href="#contact", cls="nav-link"),
                            cls="navbar-nav me-auto mb-2 mb-lg-0",
                        ),
                        Div(
                            Span(Icon("telephone", cls="me-1"), "(888) 234-5678", cls="me-3 small"),
                            Button("Request a Quote", variant="danger", size="sm"),
                            cls="d-flex align-items-center",
                        ),
                    ],
                    variant="light",
                    expand="lg",
                    sticky="top",
                    cls="hs-nav shadow-sm px-2",
                ),
                cls="pt-3 position-sticky top-0 z-3",
            ),
            # Hero
            Div(
                Row(
                    Col(
                        Div(
                            Badge("WELCOME TO COMFORT", variant="light", cls="text-dark mb-3"),
                            H1(
                                "Your Trusted",
                                Br(),
                                "Partner for",
                                Br(),
                                "Memorable Stays.",
                                cls=f"display-4 text-white fw-bold {Fx.base} {Fx.slide_up}",
                            ),
                            P(
                                "Experience premium hospitality and discover rooms designed "
                                "for comfort, style, and unforgettable moments.",
                                cls=f"text-light fs-5 mt-3 mb-4 {Fx.base} {Fx.fade_in} {Fx.delay_sm}",
                            ),
                            AutoRefresh(
                                endpoint="/api/live-demand",
                                target="this",
                                interval=8000,
                                content=Div("Checking live demand...", cls="text-light small"),
                                cls="mb-3",
                            ),
                            cls="p-5",
                        ),
                        lg=7,
                        cols=12,
                    ),
                    Col(
                        Div(
                            Card(
                                H4("Find Your Stay", cls="mb-3"),
                                FormGroup(
                                    Input("checkin", input_type="date"),
                                    label="Check In",
                                ),
                                FormGroup(
                                    Input("checkout", input_type="date"),
                                    label="Check Out",
                                ),
                                FormGroup(
                                    Select(
                                        "guests",
                                        ("1", "1 Guest"),
                                        ("2", "2 Guests", True),
                                        ("3", "3 Guests"),
                                        ("4", "4+ Guests"),
                                    ),
                                    label="Guests",
                                ),
                                LoadingButton(
                                    "Search Rooms",
                                    endpoint="/api/check-availability",
                                    target="#booking-result",
                                    variant="danger",
                                    cls="w-100",
                                ),
                                Div(id="booking-result", cls="mt-3"),
                                cls=f"border-0 shadow hs-white-card {Fx.base} {Fx.zoom_in}",
                            ),
                            cls="p-3",
                        ),
                        lg=5,
                        cols=12,
                    ),
                ),
                id="home",
                cls="hs-hero rounded-4 overflow-hidden mt-3",
            ),
            # Search and room listing
            Div(
                Div(
                    ActiveSearch(
                        endpoint="/api/search-rooms",
                        target="#room-search-results",
                        placeholder="Search room type (e.g. deluxe, suite)...",
                        debounce=250,
                    ),
                    cls="mb-3",
                ),
                Div(id="room-search-results"),
                Row(
                    *[
                        Col(room_card(r, i), lg=3, md=6, cols=12, cls="mb-4")
                        for i, r in enumerate(ROOMS)
                    ],
                    cls="g-3",
                ),
                id="rooms",
                cls="mt-5",
            ),
            # Story + team section
            Div(
                H2("Every stay has a story", cls="fw-bold mb-3"),
                LazyLoad(
                    endpoint="/api/lazy-testimonials",
                    placeholder=Div("Loading guest stories...", cls="text-muted"),
                ),
                H2("The Heart of Every Great Stay", cls="fw-bold mt-5 mb-3"),
                Row(
                    *[
                        Col(
                            Card(
                                Img(
                                    src=img,
                                    cls="w-100 rounded-top object-fit-cover",
                                    style="height:220px;",
                                ),
                                Div(
                                    Strong(name),
                                    P(role, cls="small text-muted"),
                                    cls="p-3 text-center",
                                ),
                                cls=f"border-0 shadow-sm {Fx.base} {Fx.fade_in} {Fx.hover_scale}",
                            ),
                            lg=3,
                            md=6,
                            cols=12,
                            cls="mb-3",
                        )
                        for name, role, img in TEAM
                    ],
                    cls="g-3",
                ),
                cls="hs-soft p-4 mt-5",
            ),
            # Offers
            Div(
                H2("Indulge in Luxury for Less", cls="fw-bold mb-3"),
                LazyLoad(
                    endpoint="/api/lazy-offers",
                    placeholder=Div("Loading special offers...", cls="text-muted"),
                ),
                id="deals",
                cls="mt-5",
            ),
            # Contact CTA + footer
            Div(
                Row(
                    Col(
                        Div(
                            H2(
                                "Make your reservation today and create lasting memories",
                                cls="text-white",
                            ),
                            P(
                                "Fast booking, trusted support, and premium room experiences.",
                                cls="text-light-emphasis",
                            ),
                            cls="p-4",
                        ),
                        lg=7,
                        cols=12,
                    ),
                    Col(
                        Card(
                            H4("Get in Touch"),
                            FormGroup(Input("full_name", placeholder="Full Name"), label="Name"),
                            FormGroup(
                                Input("email", input_type="email", placeholder="Email"),
                                label="Email",
                            ),
                            FormGroup(Input("phone", placeholder="Phone"), label="Phone"),
                            Button("Send Message", variant="danger", cls="w-100"),
                            cls="border-0 shadow",
                        ),
                        lg=5,
                        cols=12,
                    ),
                    cls="g-3 align-items-center",
                ),
                id="contact",
                cls="hs-dark-cta mt-5 p-4",
            ),
            FooterModern(
                brand="Booking.com",
                tagline="From quick business trips to family vacations, we make every stay remarkable.",
                columns=[
                    {
                        "title": "Service",
                        "links": [
                            {"text": "Room Booking", "href": "#rooms"},
                            {"text": "Special Offers", "href": "#deals"},
                            {"text": "Contact", "href": "#contact"},
                        ],
                    },
                    {
                        "title": "Company",
                        "links": [
                            {"text": "About Us", "href": "#"},
                            {"text": "Careers", "href": "#"},
                            {"text": "Terms", "href": "#"},
                        ],
                    },
                ],
                social_links=[
                    {"icon": "instagram", "href": "#"},
                    {"icon": "facebook", "href": "#"},
                    {"icon": "twitter-x", "href": "#"},
                ],
                bg_variant="dark",
                text_variant="light",
                cls="rounded-4 mt-4",
                copyright_text="© 2026 Booking.com - All rights reserved.",
            ),
            cls="py-4",
        ),
        cls="container-xl",
    )


@app.get("/api/live-demand")
def live_demand() -> Any:
    count = random.randint(24, 89)
    now = datetime.now().strftime("%H:%M")
    return Div(
        Badge(f"{count} travelers are viewing rooms now", variant="danger", cls="me-2"),
        Span(f"updated {now}", cls="small text-light"),
    )


@app.post("/api/check-availability")
def check_availability() -> Any:
    return toast_response(
        content=Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Rooms available! Scroll down to choose your preferred stay.",
            variant="success",
        ),
        message="Availability updated successfully.",
        variant="success",
    )


@app.get("/api/search-rooms")
def search_rooms(q: str = "") -> Any:
    query = q.strip().lower()
    if len(query) < 2:
        return ""
    matches = [r for r in ROOMS if query in r["name"].lower() or query in r["desc"].lower()]
    if not matches:
        return Div("No matching rooms found.", cls="alert alert-warning")
    return Row(*[Col(room_card(r), md=6, cols=12, cls="mb-3") for r in matches], cls="g-3 mb-3")


@app.get("/api/lazy-testimonials")
def lazy_testimonials() -> Any:
    return Row(
        *[
            Col(
                Testimonial(quote=q, author=a, role=city, rating=5, cls=f"{Fx.base} {Fx.fade_in}"),
                lg=4,
                cols=12,
                cls="mb-3",
            )
            for q, a, city in TESTIMONIALS
        ],
        cls="g-3",
    )


@app.get("/api/lazy-offers")
def lazy_offers() -> Any:
    return Row(
        *[
            Col(
                Card(
                    Img(src=img, cls="w-100 rounded-top object-fit-cover", style="height:180px;"),
                    Div(
                        Badge(badge, variant="danger", cls="mb-2"),
                        Strong(title, cls="d-block"),
                        Button("Book Offer", variant="outline-danger", size="sm", cls="mt-2"),
                        cls="p-3",
                    ),
                    cls=f"border-0 shadow-sm h-100 {Fx.base} {Fx.fade_in} {Fx.hover_lift}",
                ),
                lg=4,
                cols=12,
                cls="mb-3",
            )
            for title, badge, img in OFFERS
        ],
        cls="g-3",
    )


serve()
