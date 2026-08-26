"""
03_forms/date_pickers.py
Demonstrates: CalendarDatePicker, DateRangePicker

CalendarDatePicker: single-date native date input with label support.
DateRangePicker: start/end date pair with optional presets and HTMX endpoint.

Use case: booking forms, report date filters, event scheduling.
"""

from fasthtml.common import FastHTML, H1, H2, H3, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    CalendarDatePicker,
    DateRangePicker,
    Button,
    Alert,
    Card,
    FormGroup,
    Row,
    Col,
    Stack,
)

app = FastHTML()
add_bootstrap(app, theme="cyan-sky", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Date Pickers", cls="display-5 fw-bold mb-2"),
        P("Native date inputs with built-in range and preset support.", cls="lead text-muted mb-5"),

        # ── CalendarDatePicker ─────────────────────────────────────────────
        H2("CalendarDatePicker", cls="h4 fw-semibold mb-1"),
        P("Single-date picker. Wraps a native <input type=date> with optional label, help text, and constraints.", cls="text-muted mb-3"),
        Card(
            Row(
                Col(
                    FormGroup(
                        CalendarDatePicker(name="check_in", label="Check-in Date", min_date="2024-01-01"),
                        label="Check-in",
                    ),
                    span=12, md=6,
                ),
                Col(
                    FormGroup(
                        CalendarDatePicker(name="check_out", label="Check-out Date", min_date="2024-01-01"),
                        label="Check-out",
                    ),
                    span=12, md=6,
                ),
                cls="g-3",
            ),
            Button("Search Availability", variant="primary", cls="mt-3"),
            header="Hotel Booking Form",
            cls="mb-5",
        ),

        # ── DateRangePicker ────────────────────────────────────────────────
        H2("DateRangePicker", cls="h4 fw-semibold mb-1"),
        P("Start/end date pair with quick presets. Submits to an HTMX endpoint on Apply.", cls="text-muted mb-3"),
        Card(
            DateRangePicker(
                start_name="report_start",
                end_name="report_end",
                start_label="From",
                end_label="To",
                presets=[
                    ("Last 7 days", "2024-12-01", "2024-12-07"),
                    ("Last 30 days", "2024-11-08", "2024-12-07"),
                    ("Last quarter", "2024-10-01", "2024-12-31"),
                    ("This year", "2024-01-01", "2024-12-31"),
                ],
                endpoint="/api/filter-report",
                hx_target="#report-results",
                apply_label="Apply Filter",
            ),
            Div("Report results will appear here after selecting a range.", id="report-results", cls="mt-3 text-muted"),
            header="Analytics Date Range Filter",
            cls="mb-5",
        ),

        cls="my-5",
    )


@app.get("/api/filter-report")
def filter_report(report_start: str = "", report_end: str = ""):
    if report_start and report_end:
        return Alert(f"Showing report from {report_start} to {report_end}", variant="info")
    return Alert("Please select a valid date range.", variant="warning")


if __name__ == "__main__":
    serve()
