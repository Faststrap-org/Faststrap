# Utility API

These helpers support static asset inspection, SVG rendering, form-validation mapping, and DataTable URL construction. They are useful when building wrappers or integrating Faststrap with an existing application layer.

## DataTable Query Helpers

```python
from faststrap import datatable_page_url, datatable_query_params

params = datatable_query_params(
    sort="created_at",
    direction="desc",
    search="pending",
    page=2,
    per_page=25,
)
url = datatable_page_url("/orders", page=2, per_page=25, sort="created_at", direction="desc")
```

The helpers preserve repeated filter values and keep URL construction in one place. Use `datatable_export_params()` when an export endpoint should receive the current sort, search, and filter state without pagination.

## Form Error Helpers

```python
from faststrap import extract_field_error, map_formgroup_validation

message = extract_field_error(errors, "email")
state = map_formgroup_validation(errors, "email")
```

These helpers accept mapping-shaped validation errors and return values suitable for `FormGroup`, `Input`, and related form components.

## API Reference

::: faststrap.components.display.data_table.datatable_export_params
    options:
        show_source: true
        heading_level: 2

::: faststrap.components.display.data_table.datatable_query_params
    options:
        show_source: true
        heading_level: 2

::: faststrap.components.display.data_table.datatable_page_url
    options:
        show_source: true
        heading_level: 2

::: faststrap.components.forms.errors.extract_field_error
    options:
        show_source: true
        heading_level: 2

::: faststrap.components.forms.errors.map_formgroup_validation
    options:
        show_source: true
        heading_level: 2

::: faststrap.utils.static_management.get_faststrap_static_url
    options:
        show_source: true
        heading_level: 2

::: faststrap.utils.static_management.cleanup_static_resources
    options:
        show_source: true
        heading_level: 2

::: faststrap.components.display.svg.render_svg
    options:
        show_source: true
        heading_level: 2
