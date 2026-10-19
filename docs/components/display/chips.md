# Chip And ChipGroup

`Chip` is the interactive/filter-oriented counterpart to the informational `Badge`. `Tag` remains available and compatible; use `Chip` when selected state, a value, or removal is part of the UI contract.

```python
from faststrap import Chip, ChipGroup

ChipGroup(
    Chip("Python", value="python", selected=True, hx_get="/items?tag=python"),
    Chip("ML", value="ml", removable=True, on_remove="hx-delete='/filters/ml'"),
    label="Filter by topic",
)
```

| Component | Important parameters |
| --- | --- |
| `Chip` | `variant`, `size`, `selected`, `removable`, `icon`, `on_remove`, `value`, and HTML/HTMX attributes. |
| `ChipGroup` | `selected` index, accessible `label`, `gap`, `wrap`, and HTML/HTMX attributes. |

Selection is server-rendered. For a filter request, add HTMX attributes to each chip and return the updated result region from the route.

::: faststrap.components.display.tag.Chip
    options:
        show_source: true

::: faststrap.components.display.tag.ChipGroup
    options:
        show_source: true
