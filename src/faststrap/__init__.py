"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.5.6"
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality

# Display
# Presets (HTMX interaction helpers)
from . import presets
from .accessibility import FocusTrap, LiveRegion, SkipLink, VisuallyHidden
from .components.display import (
    Badge,
    Card,
    Carousel,
    CarouselItem,
    EmptyState,
    Figure,
    Image,
    Sheet,
    StatCard,
    Table,
    TBody,
    TCell,
    TextClamp,
    THead,
    TRow,
)

# Feedback
from .components.feedback import (
    Alert,
    ConfirmDialog,
    ErrorDialog,
    ErrorPage,
    ErrorToast,
    InfoToast,
    InstallPrompt,
    Modal,
    NoticeAlert,
    NoticeToast,
    Placeholder,
    PlaceholderButton,
    PlaceholderCard,
    Popover,
    Progress,
    ProgressBar,
    SimpleToast,
    Spinner,
    SuccessToast,
    Toast,
    ToastContainer,
    Tooltip,
    WarningToast,
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
    FormGroup,
    FormGroupFromErrors,
    Input,
    InputGroup,
    InputGroupText,
    Radio,
    Range,
    SearchableSelect,
    Select,
    Switch,
    ThemeToggle,
    ToggleGroup,
    extract_field_error,
    map_formgroup_validation,
)

# Layout
from .components.layout import Col, Container, Hero, Row

# Navigation
from .components.navigation import (
    Accordion,
    AccordionItem,
    BottomNav,
    BottomNavItem,
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
    FooterModern,
    NavbarModern,
    PricingGroup,
    PricingTier,
    Testimonial,
    TestimonialSection,
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
from .layouts import AuthLayout, DashboardLayout, LandingLayout

# PWA
from .pwa import PwaMeta, add_pwa

# SEO helpers
from .seo import SEO, PageMeta, StructuredData

# Utils
from .utils import cleanup_static_resources, get_faststrap_static_url
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "mount_assets",
    "merge_classes",
    # Accessibility
    "SkipLink",
    "LiveRegion",
    "VisuallyHidden",
    "FocusTrap",
    # PWA
    "PwaMeta",
    "add_pwa",
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
    "FormGroup",
    "Radio",
    "Switch",
    "Range",
    "Input",
    "InputGroup",
    "InputGroupText",
    "FloatingLabel",
    "SearchableSelect",
    "Select",
    "ThemeToggle",
    "ToggleGroup",
    "extract_field_error",
    "map_formgroup_validation",
    "FormGroupFromErrors",
    # Display
    "Badge",
    "Card",
    "Carousel",
    "CarouselItem",
    "EmptyState",
    "Figure",
    "Image",
    "Sheet",
    "StatCard",
    "TextClamp",
    "Table",
    "THead",
    "TBody",
    "TRow",
    "TCell",
    "Alert",
    "ErrorPage",
    "ErrorDialog",
    "InstallPrompt",
    "ConfirmDialog",
    "Toast",
    "SimpleToast",
    "NoticeToast",
    "NoticeAlert",
    "SuccessToast",
    "ErrorToast",
    "WarningToast",
    "InfoToast",
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
    "BottomNav",
    "BottomNavItem",
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
    "AuthLayout",
    "DashboardLayout",
    "LandingLayout",
    # Patterns
    "NavbarModern",
    "Feature",
    "FeatureGrid",
    "FooterModern",
    "Testimonial",
    "TestimonialSection",
    "PricingGroup",
    "PricingTier",
    # Presets
    "presets",
    # SEO
    "SEO",
    "PageMeta",
    "StructuredData",
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
