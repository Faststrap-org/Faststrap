"""
FastShop - Complete Mini E-commerce System with Faststrap
Features: Products, Categories, Cart, Checkout, Orders, Admin Panel
"""

from datetime import datetime

from fasthtml.common import *

from faststrap import (
    Alert,
    Badge,
    Button,
    ButtonGroup,
    Card,
    Col,
    Container,
    Icon,
    Input,
    Navbar,
    Row,
    Select,
    Table,
    add_bootstrap,
    create_theme,
)

# Initialize FastHTML app
app = FastHTML()

# Add Bootstrap with custom theme
theme_color = create_theme(
    primary="#2563eb", secondary="#64748b", success="#16a34a", danger="#dc2626", warning="#f59e0b"
)
add_bootstrap(app, theme=theme_color)

# ============================================================================
# DATA MODELS (In-memory storage - replace with DB in production)
# ============================================================================

# Sample Products Database
PRODUCTS = {
    "1": {
        "id": "1",
        "name": "Classic White T-Shirt",
        "price": 29.99,
        "category": "Clothing",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 50,
        "image": "👕",
        "description": "Premium cotton t-shirt",
    },
    "2": {
        "id": "2",
        "name": "Denim Jeans",
        "price": 79.99,
        "category": "Clothing",
        "sizes": ["28", "30", "32", "34", "36"],
        "stock": 30,
        "image": "👖",
        "description": "Classic fit denim jeans",
    },
    "3": {
        "id": "3",
        "name": "Running Shoes",
        "price": 89.99,
        "category": "Footwear",
        "sizes": ["7", "8", "9", "10", "11"],
        "stock": 25,
        "image": "👟",
        "description": "Lightweight running shoes",
    },
    "4": {
        "id": "4",
        "name": "Leather Wallet",
        "price": 39.99,
        "category": "Accessories",
        "sizes": ["One Size"],
        "stock": 100,
        "image": "👛",
        "description": "Genuine leather wallet",
    },
    "5": {
        "id": "5",
        "name": "Baseball Cap",
        "price": 24.99,
        "category": "Accessories",
        "sizes": ["One Size"],
        "stock": 75,
        "image": "🧢",
        "description": "Adjustable baseball cap",
    },
    "6": {
        "id": "6",
        "name": "Backpack",
        "price": 59.99,
        "category": "Accessories",
        "sizes": ["One Size"],
        "stock": 40,
        "image": "🎒",
        "description": "Durable travel backpack",
    },
    "7": {
        "id": "7",
        "name": "Sneakers",
        "price": 69.99,
        "category": "Footwear",
        "sizes": ["7", "8", "9", "10", "11"],
        "stock": 35,
        "image": "👞",
        "description": "Casual everyday sneakers",
    },
    "8": {
        "id": "8",
        "name": "Hoodie",
        "price": 49.99,
        "category": "Clothing",
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "stock": 45,
        "image": "🧥",
        "description": "Cozy pullover hoodie",
    },
}

# Shopping Cart (session-based in production)
CART = {}

# Orders Database
ORDERS = {}
ORDER_COUNTER = 1000

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def get_cart_total():
    """Calculate total items and price in cart"""
    total_items = sum(item["quantity"] for item in CART.values())
    total_price = sum(item["quantity"] * item["price"] for item in CART.values())
    return total_items, total_price


def get_categories():
    """Get unique categories from products"""
    return sorted({p["category"] for p in PRODUCTS.values()})


def filter_products(category=None, search=None):
    """Filter products by category and search term"""
    products = list(PRODUCTS.values())

    if category and category != "All":
        products = [p for p in products if p["category"] == category]

    if search:
        search = search.lower()
        products = [
            p for p in products if search in p["name"].lower() or search in p["description"].lower()
        ]

    return products


# ============================================================================
# LAYOUT COMPONENTS
# ============================================================================


def page_layout(content, active_tab="shop"):
    """Main page layout with navigation"""
    total_items, _ = get_cart_total()

    return Html(
        Head(
            Title("FastShop - Modern E-commerce"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            *app.hdrs,
        ),
        Body(
            # Navigation Bar
            Navbar(
                Div(
                    A("🛒 FastShop", href="/", cls="navbar-brand fs-3 fw-bold"),
                    cls="container-fluid",
                ),
                Div(
                    Ul(
                        Li(
                            A(
                                "Shop",
                                href="/",
                                cls=f"nav-link {'active' if active_tab=='shop' else ''}",
                            ),
                            cls="nav-item",
                        ),
                        Li(
                            A(
                                "Orders",
                                href="/orders",
                                cls=f"nav-link {'active' if active_tab=='orders' else ''}",
                            ),
                            cls="nav-item",
                        ),
                        Li(
                            A(
                                "Admin",
                                href="/admin",
                                cls=f"nav-link {'active' if active_tab=='admin' else ''}",
                            ),
                            cls="nav-item",
                        ),
                        cls="navbar-nav me-auto",
                    ),
                    A(
                        Button(
                            Icon("cart3"),
                            f" Cart ({total_items})",
                            variant="primary",
                            id="cart-btn",
                        ),
                        href="/cart",
                        cls="text-decoration-none",
                    ),
                    cls="collapse navbar-collapse",
                ),
                variant="light",
                expand="lg",
            ),
            # Main Content
            Div(content, cls="container my-4"),
            # Footer
            Div(
                Container(
                    Row(
                        Col(
                            P(
                                "© 2024 FastShop. Built with FastHTML + Faststrap",
                                cls="text-center text-muted mb-0",
                            )
                        )
                    )
                ),
                cls="bg-light py-4 mt-5",
            ),
        ),
    )


# ============================================================================
# SHOP PAGE (Main Store)
# ============================================================================


@app.get("/")
def shop(category: str = None, search: str = None):
    """Main shop page with products"""
    products = filter_products(category, search)
    categories = get_categories()

    # Filter/Search Bar
    filter_section = Card(
        Row(
            Col(
                Select(
                    "category",
                    ("All", "All Categories"),
                    *[(cat, cat) for cat in categories],
                    label="Category",
                    selected=category or "All",
                    hx_get="/",
                    hx_target="#product-grid",
                    hx_include="[name='search']",
                    # name="category"
                ),
                cols=12,
                md=4,
            ),
            Col(
                Input(
                    "search",
                    placeholder="Search products...",
                    value=search or "",
                    label="Search",
                    hx_get="/",
                    hx_target="#product-grid",
                    hx_trigger="keyup changed delay:500ms",
                    hx_include="[name='category']",
                ),
                cols=12,
                md=6,
            ),
            Col(
                Div(
                    Button(
                        "Clear Filters",
                        variant="outline-secondary",
                        onclick="window.location.href='/'",
                        cls="w-100",
                    ),
                    style={"padding-top": "32px"},
                ),
                cols=12,
                md=2,
            ),
        ),
        cls="mb-4",
    )

    # Products Grid
    if not products:
        products_section = Alert(
            "No products found. Try different filters!", variant="info", cls="text-center"
        )
    else:
        product_cards = []
        for product in products:
            product_cards.append(
                Col(
                    Card(
                        Div(
                            H1(product["image"], cls="text-center", style={"font-size": "4rem"}),
                            cls="card-body text-center",
                        ),
                        Div(
                            H5(product["name"], cls="card-title"),
                            P(product["description"], cls="card-text text-muted small"),
                            Div(
                                Badge(product["category"], variant="secondary"),
                                " ",
                                Badge(
                                    f"{product['stock']} in stock",
                                    variant="success" if product["stock"] > 10 else "warning",
                                ),
                                cls="mb-2",
                            ),
                            H4(f"${product['price']}", cls="text-primary fw-bold"),
                            Button(
                                Icon("cart-plus"),
                                " Add to Cart",
                                variant="primary",
                                cls="w-100",
                                hx_post=f"/cart/add/{product['id']}",
                                hx_target="#cart-btn",
                                hx_swap="outerHTML",
                            ),
                            cls="card-body",
                        ),
                        cls="h-100 shadow-sm hover-shadow",
                        style={"transition": "transform 0.2s"},
                    ),
                    cols=12,
                    sm=6,
                    md=4,
                    lg=3,
                    cls="mb-4",
                )
            )

        products_section = Div(Row(*product_cards), id="product-grid")

    content = Div(H1("Welcome to FastShop", cls="mb-4"), filter_section, products_section)

    return page_layout(content, "shop")


# ============================================================================
# CART PAGE
# ============================================================================


@app.get("/cart")
def view_cart():
    """Shopping cart page"""
    if not CART:
        content = Div(
            Alert(
                H4("Your cart is empty", cls="alert-heading"),
                P("Start shopping to add items to your cart!"),
                A(Button("Continue Shopping", variant="primary"), href="/"),
                variant="info",
                cls="text-center",
            )
        )
    else:
        # Cart Items
        cart_rows = []
        for item_id, item in CART.items():
            cart_rows.append(
                Tr(
                    Td(
                        Div(
                            Span(item["image"], style={"font-size": "2rem"}),
                            " ",
                            Strong(item["name"]),
                        )
                    ),
                    Td(f"${item['price']:.2f}"),
                    Td(f"{item['size']}"),
                    Td(
                        ButtonGroup(
                            Button(
                                "-",
                                variant="outline-secondary",
                                size="sm",
                                hx_post=f"/cart/decrease/{item_id}",
                                hx_target="#cart-content",
                                hx_swap="innerHTML",
                            ),
                            Span(str(item["quantity"]), cls="px-3 py-1 bg-light border"),
                            Button(
                                "+",
                                variant="outline-secondary",
                                size="sm",
                                hx_post=f"/cart/increase/{item_id}",
                                hx_target="#cart-content",
                                hx_swap="innerHTML",
                            ),
                        )
                    ),
                    Td(Strong(f"${item['price'] * item['quantity']:.2f}")),
                    Td(
                        Button(
                            Icon("trash"),
                            variant="danger",
                            size="sm",
                            hx_post=f"/cart/remove/{item_id}",
                            hx_target="#cart-content",
                            hx_swap="innerHTML",
                            hx_confirm="Remove this item from cart?",
                        )
                    ),
                )
            )

        _, total_price = get_cart_total()

        content = Div(
            Div(
                H1("Shopping Cart", cls="mb-4"),
                Table(
                    Thead(
                        Tr(
                            Th("Product"),
                            Th("Price"),
                            Th("Size"),
                            Th("Quantity"),
                            Th("Subtotal"),
                            Th("Action"),
                        )
                    ),
                    Tbody(*cart_rows),
                    striped=True,
                    hover=True,
                    cls="mb-4",
                ),
                Row(
                    Col(
                        A(Button("Continue Shopping", variant="outline-secondary"), href="/"),
                        cols=12,
                        md=6,
                    ),
                    Col(
                        Card(
                            H4("Order Summary"),
                            Hr(),
                            Div(
                                Div(
                                    Span("Subtotal:"),
                                    Strong(f"${total_price:.2f}", cls="float-end"),
                                ),
                                Div(
                                    Span("Shipping:"), Strong("FREE", cls="float-end text-success")
                                ),
                                Hr(),
                                Div(
                                    H5("Total:"),
                                    H4(f"${total_price:.2f}", cls="float-end text-primary"),
                                ),
                            ),
                            A(
                                Button("Proceed to Checkout", variant="primary", cls="w-100 mt-3"),
                                href="/checkout",
                            ),
                            cls="bg-light",
                        ),
                        cols=12,
                        md=6,
                    ),
                ),
            ),
            id="cart-content",
        )

    return page_layout(content, "shop")


# ============================================================================
# CART ACTIONS (HTMX Endpoints)
# ============================================================================


@app.post("/cart/add/{product_id}")
def add_to_cart(product_id: str):
    """Add product to cart (requires size selection in production)"""
    product = PRODUCTS.get(product_id)
    if not product:
        return Button("Error", variant="danger", disabled=True)

    # Use first available size for demo
    size = product["sizes"][0]
    cart_key = f"{product_id}_{size}"

    if cart_key in CART:
        CART[cart_key]["quantity"] += 1
    else:
        CART[cart_key] = {
            "id": product_id,
            "name": product["name"],
            "price": product["price"],
            "size": size,
            "quantity": 1,
            "image": product["image"],
        }

    total_items, _ = get_cart_total()
    return Button(
        Icon("cart3"),
        f" Cart ({total_items})",
        variant="primary",
        id="cart-btn",
        onclick="window.location.href='/cart'",
    )


@app.post("/cart/increase/{item_id}")
def increase_quantity(item_id: str):
    """Increase item quantity"""
    if item_id in CART:
        CART[item_id]["quantity"] += 1
    return cart_content()


@app.post("/cart/decrease/{item_id}")
def decrease_quantity(item_id: str):
    """Decrease item quantity"""
    if item_id in CART and CART[item_id]["quantity"] > 1:
        CART[item_id]["quantity"] -= 1
    return cart_content()


@app.post("/cart/remove/{item_id}")
def remove_from_cart(item_id: str):
    """Remove item from cart"""
    if item_id in CART:
        del CART[item_id]
    return cart_content()


def cart_content():
    """Return updated cart content for HTMX"""
    if not CART:
        return Alert(
            H4("Your cart is empty", cls="alert-heading"),
            P("Start shopping to add items to your cart!"),
            A(Button("Continue Shopping", variant="primary"), href="/"),
            variant="info",
            cls="text-center",
        )

    # Generate cart table (same as view_cart)
    cart_rows = []
    for item_id, item in CART.items():
        cart_rows.append(
            Tr(
                Td(
                    Div(Span(item["image"], style={"font-size": "2rem"}), " ", Strong(item["name"]))
                ),
                Td(f"${item['price']:.2f}"),
                Td(f"{item['size']}"),
                Td(
                    ButtonGroup(
                        Button(
                            "-",
                            variant="outline-secondary",
                            size="sm",
                            hx_post=f"/cart/decrease/{item_id}",
                            hx_target="#cart-content",
                            hx_swap="innerHTML",
                        ),
                        Span(str(item["quantity"]), cls="px-3 py-1 bg-light border"),
                        Button(
                            "+",
                            variant="outline-secondary",
                            size="sm",
                            hx_post=f"/cart/increase/{item_id}",
                            hx_target="#cart-content",
                            hx_swap="innerHTML",
                        ),
                    )
                ),
                Td(Strong(f"${item['price'] * item['quantity']:.2f}")),
                Td(
                    Button(
                        Icon("trash"),
                        variant="danger",
                        size="sm",
                        hx_post=f"/cart/remove/{item_id}",
                        hx_target="#cart-content",
                        hx_swap="innerHTML",
                        hx_confirm="Remove this item?",
                    )
                ),
            )
        )

    _, total_price = get_cart_total()

    return Div(
        H1("Shopping Cart", cls="mb-4"),
        Table(
            Thead(
                Tr(
                    Th("Product"),
                    Th("Price"),
                    Th("Size"),
                    Th("Quantity"),
                    Th("Subtotal"),
                    Th("Action"),
                )
            ),
            Tbody(*cart_rows),
            striped=True,
            hover=True,
            cls="mb-4",
        ),
        Row(
            Col(
                A(Button("Continue Shopping", variant="outline-secondary"), href="/"), cols=12, md=6
            ),
            Col(
                Card(
                    H4("Order Summary"),
                    Hr(),
                    Div(
                        Div(Span("Subtotal:"), Strong(f"${total_price:.2f}", cls="float-end")),
                        Div(Span("Shipping:"), Strong("FREE", cls="float-end text-success")),
                        Hr(),
                        Div(H5("Total:"), H4(f"${total_price:.2f}", cls="float-end text-primary")),
                    ),
                    A(
                        Button("Proceed to Checkout", variant="primary", cls="w-100 mt-3"),
                        href="/checkout",
                    ),
                    cls="bg-light",
                ),
                cols=12,
                md=6,
            ),
        ),
    )


# ============================================================================
# CHECKOUT PAGE
# ============================================================================


@app.get("/checkout")
def checkout_page():
    """Checkout form"""
    if not CART:
        return page_layout(
            Alert("Your cart is empty!", variant="warning", cls="text-center"), "shop"
        )

    _, total_price = get_cart_total()

    content = Div(
        H1("Checkout", cls="mb-4"),
        Row(
            Col(
                Card(
                    H4("Shipping Information", cls="card-header"),
                    Form(
                        Row(
                            Col(
                                Input("first_name", label="First Name", required=True),
                                cols=12,
                                md=6,
                            ),
                            Col(
                                Input("last_name", label="Last Name", required=True), cols=12, md=6
                            ),
                        ),
                        Input("email", input_type="email", label="Email", required=True),
                        Input("phone", input_type="tel", label="Phone", required=True),
                        Input("address", label="Street Address", required=True),
                        Row(
                            Col(Input("city", label="City", required=True), cols=12, md=6),
                            Col(Input("state", label="State", required=True), cols=12, md=3),
                            Col(Input("zip", label="ZIP Code", required=True), cols=12, md=3),
                        ),
                        Button("Place Order", variant="primary", type="submit", cls="w-100 mt-3"),
                        hx_post="/checkout/submit",
                        hx_target="body",
                    ),
                    cls="mb-4",
                ),
                cols=12,
                md=8,
            ),
            Col(
                Card(
                    H4("Order Summary", cls="card-header"),
                    Ul(
                        *[
                            Li(
                                f"{item['name']} ({item['size']}) x {item['quantity']} - ${item['price'] * item['quantity']:.2f}"
                            )
                            for item in CART.values()
                        ],
                        cls="list-group list-group-flush",
                    ),
                    Div(
                        Hr(),
                        H5("Total: ", Strong(f"${total_price:.2f}", cls="text-primary")),
                        cls="card-body",
                    ),
                ),
                cols=12,
                md=4,
            ),
        ),
    )

    return page_layout(content, "shop")


@app.post("/checkout/submit")
def submit_order(
    first_name: str,
    last_name: str,
    email: str,
    phone: str,
    address: str,
    city: str,
    state: str,
    zip: str,
):
    """Process order submission"""
    global ORDER_COUNTER

    if not CART:
        return page_layout(Alert("Cart is empty!", variant="danger"), "shop")

    # Create order
    order_id = f"ORD-{ORDER_COUNTER}"
    ORDER_COUNTER += 1

    _, total_price = get_cart_total()

    ORDERS[order_id] = {
        "id": order_id,
        "customer": {
            "name": f"{first_name} {last_name}",
            "email": email,
            "phone": phone,
            "address": f"{address}, {city}, {state} {zip}",
        },
        "items": list(CART.values()),
        "total": total_price,
        "status": "Processing",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    # Clear cart
    CART.clear()

    # Success page
    return page_layout(
        Div(
            Alert(
                H3("🎉 Order Placed Successfully!", cls="alert-heading"),
                P(f"Your order {order_id} has been confirmed."),
                P(f"Total: ${total_price:.2f}"),
                P("We'll send a confirmation email shortly."),
                Hr(),
                A(Button("View Order", variant="primary"), href=f"/orders/{order_id}", cls="me-2"),
                A(Button("Continue Shopping", variant="outline-secondary"), href="/"),
                variant="success",
            ),
            cls="text-center mt-5",
        ),
        "shop",
    )


# ============================================================================
# ORDERS PAGE
# ============================================================================


@app.get("/orders")
def orders_list():
    """List all orders"""
    if not ORDERS:
        content = Alert("No orders yet. Start shopping!", variant="info", cls="text-center")
    else:
        order_rows = []
        for order in sorted(ORDERS.values(), key=lambda x: x["date"], reverse=True):
            status_variant = {
                "Processing": "warning",
                "Shipped": "info",
                "Delivered": "success",
                "Cancelled": "danger",
            }.get(order["status"], "secondary")

            order_rows.append(
                Tr(
                    Td(Strong(order["id"])),
                    Td(order["date"]),
                    Td(order["customer"]["name"]),
                    Td(f"${order['total']:.2f}"),
                    Td(Badge(order["status"], variant=status_variant)),
                    Td(
                        A(
                            Button("View", variant="outline-primary", size="sm"),
                            href=f"/orders/{order['id']}",
                        )
                    ),
                )
            )

        content = Div(
            H1("My Orders", cls="mb-4"),
            Table(
                Thead(
                    Tr(
                        Th("Order ID"),
                        Th("Date"),
                        Th("Customer"),
                        Th("Total"),
                        Th("Status"),
                        Th("Action"),
                    )
                ),
                Tbody(*order_rows),
                striped=True,
                hover=True,
            ),
        )

    return page_layout(content, "orders")


@app.get("/orders/{order_id}")
def order_detail(order_id: str):
    """View specific order"""
    order = ORDERS.get(order_id)
    if not order:
        return page_layout(Alert("Order not found!", variant="danger"), "orders")

    status_variant = {
        "Processing": "warning",
        "Shipped": "info",
        "Delivered": "success",
        "Cancelled": "danger",
    }.get(order["status"], "secondary")

    content = Div(
        H1(f"Order {order_id}", cls="mb-4"),
        Row(
            Col(
                Card(
                    H4("Order Details", cls="card-header"),
                    Div(
                        P(Strong("Date: "), order["date"]),
                        P(Strong("Status: "), Badge(order["status"], variant=status_variant)),
                        P(Strong("Total: "), f"${order['total']:.2f}"),
                        cls="card-body",
                    ),
                ),
                Card(
                    H4("Customer Information", cls="card-header"),
                    Div(
                        P(Strong("Name: "), order["customer"]["name"]),
                        P(Strong("Email: "), order["customer"]["email"]),
                        P(Strong("Phone: "), order["customer"]["phone"]),
                        P(Strong("Address: "), order["customer"]["address"]),
                        cls="card-body",
                    ),
                    cls="mt-3",
                ),
                cols=12,
                md=5,
            ),
            Col(
                Card(
                    H4("Items", cls="card-header"),
                    Table(
                        Thead(Tr(Th("Product"), Th("Size"), Th("Qty"), Th("Price"))),
                        Tbody(
                            *[
                                Tr(
                                    Td(item["name"]),
                                    Td(item["size"]),
                                    Td(item["quantity"]),
                                    Td(f"${item['price'] * item['quantity']:.2f}"),
                                )
                                for item in order["items"]
                            ]
                        ),
                        striped=True,
                    ),
                ),
                cols=12,
                md=7,
            ),
        ),
        A(Button("Back to Orders", variant="secondary", cls="mt-3"), href="/orders"),
    )

    return page_layout(content, "orders")


# ============================================================================
# ADMIN PANEL
# ============================================================================


@app.get("/admin")
def admin_panel():
    """Admin dashboard"""
    total_products = len(PRODUCTS)
    total_orders = len(ORDERS)
    total_revenue = sum(order["total"] for order in ORDERS.values())

    content = Div(
        H1("Admin Dashboard", cls="mb-4"),
        Row(
            Col(
                Card(
                    Div(
                        H2(str(total_products), cls="display-4 text-primary"),
                        P("Total Products", cls="text-muted"),
                        cls="card-body text-center",
                    )
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    Div(
                        H2(str(total_orders), cls="display-4 text-success"),
                        P("Total Orders", cls="text-muted"),
                        cls="card-body text-center",
                    )
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    Div(
                        H2(f"${total_revenue:.2f}", cls="display-4 text-warning"),
                        P("Total Revenue", cls="text-muted"),
                        cls="card-body text-center",
                    )
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
        ),
        Card(
            H4("Recent Orders", cls="card-header"),
            (
                Table(
                    Thead(
                        Tr(Th("Order ID"), Th("Customer"), Th("Total"), Th("Status"), Th("Date"))
                    ),
                    Tbody(
                        *[
                            Tr(
                                Td(order["id"]),
                                Td(order["customer"]["name"]),
                                Td(f"${order['total']:.2f}"),
                                Td(Badge(order["status"], variant="warning")),
                                Td(order["date"]),
                            )
                            for order in sorted(
                                ORDERS.values(), key=lambda x: x["date"], reverse=True
                            )[:5]
                        ]
                    ),
                    striped=True,
                    hover=True,
                )
                if ORDERS
                else P("No orders yet", cls="card-body text-muted")
            ),
        ),
    )

    return page_layout(content, "admin")


# ============================================================================
# START SERVER
# ============================================================================

if __name__ == "__main__":
    serve(port=8033)
