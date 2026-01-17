"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.5.1"
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
# Display
from .components.display import (
    Badge,
    Card,
    Carousel,
    CarouselItem,
    EmptyState,
    Figure,
    Image,
    StatCard,
    Table,
    TBody,
    TCell,
    THead,
    TRow,
)

# Feedback
from .components.feedback import (
    Alert,
    ConfirmDialog,
    Modal,
    Placeholder,
    PlaceholderButton,
    PlaceholderCard,
    Popover,
    Progress,
    ProgressBar,
    SimpleToast,
    Spinner,
    Toast,
    ToastContainer,
    Tooltip,
)

# Forms
from .components.forms import (
    Button,
    ButtonGroup,
    ButtonToolbar,
    Checkbox,
    CloseButton,
    FileInput,
    FloatingLabel,
    Input,
    InputGroup,
    InputGroupText,
    Radio,
    Range,
    Select,
    Switch,
)

# Layout
from .components.layout import Col, Container, Hero, Row

# Navigation
from .components.navigation import (
    Accordion,
    AccordionItem,
    Breadcrumb,
    Collapse,
    Drawer,
    Dropdown,
    DropdownDivider,
    DropdownItem,
    GlassNavbar,
    GlassNavItem,
    ListGroup,
    ListGroupItem,
    Navbar,
    Pagination,
    Scrollspy,
    SidebarNavbar,
    SidebarNavItem,
    TabPane,
    Tabs,
)

# Patterns
from .components.patterns import (
    Feature,
    FeatureGrid,
    NavbarModern,
    PricingGroup,
    PricingTier,
)
from .core._stability import beta, experimental, stable
from .core.assets import add_bootstrap, get_assets, mount_assets
from .core.base import merge_classes
from .core.effects import Fx
from .core.theme import (
    Theme,
    create_theme,
    get_builtin_theme,
    list_builtin_themes,
    reset_component_defaults,
    resolve_defaults,
    set_component_defaults,
)
from .layouts import DashboardLayout, LandingLayout

# Utils
from .utils import cleanup_static_resources, get_faststrap_static_url
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "mount_assets",
    "merge_classes",
    # Theme
    "Theme",
    "create_theme",
    "get_builtin_theme",
    "list_builtin_themes",
    "set_component_defaults",
    "reset_component_defaults",
    "resolve_defaults",
    # Forms
    "Button",
    "CloseButton",
    "ButtonGroup",
    "ButtonToolbar",
    "Checkbox",
    "FileInput",
    "Radio",
    "Switch",
    "Range",
    "Input",
    "InputGroup",
    "InputGroupText",
    "FloatingLabel",
    "Select",
    # Display
    "Badge",
    "Card",
    "Carousel",
    "CarouselItem",
    "EmptyState",
    "Figure",
    "Image",
    "StatCard",
    "Table",
    "THead",
    "TBody",
    "TRow",
    "TCell",
    "Alert",
    "ConfirmDialog",
    "Toast",
    "SimpleToast",
    "ToastContainer",
    "Modal",
    "Placeholder",
    "PlaceholderButton",
    "PlaceholderCard",
    "Popover",
    "Tooltip",
    "Progress",
    "ProgressBar",
    "Spinner",
    # Layout
    "Container",
    "Row",
    "Col",
    "Hero",
    # Navigation
    "Accordion",
    "AccordionItem",
    "Collapse",
    "Drawer",
    "ListGroup",
    "ListGroupItem",
    "Navbar",
    "GlassNavbar",
    "GlassNavItem",
    "Scrollspy",
    "SidebarNavbar",
    "SidebarNavItem",
    "Pagination",
    "Breadcrumb",
    "Dropdown",
    "DropdownItem",
    "DropdownDivider",
    "Tabs",
    "TabPane",
    # Layouts
    "DashboardLayout",
    "LandingLayout",
    # Patterns
    "NavbarModern",
    "Feature",
    "FeatureGrid",
    "PricingGroup",
    "PricingTier",
    # Utils
    "Icon",
    "get_faststrap_static_url",
    "cleanup_static_resources",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
    "Fx",
    # Stability
    "stable",
    "beta",
    "experimental",
]
