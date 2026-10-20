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

Plain `Chip("Label")` stays a non-interactive `<span>`. Supplying `href` makes it an anchor; supplying `type` or an HTMX action such as `hx_get`/`hx_post` makes it a native `<button type="button">` so it is keyboard-operable. A removable chip cannot also be an `href`, explicit button, or direct HTMX action because its remove control must not be nested inside another interactive control; put `on_remove` on its internal remove button instead. Selection styling/ARIA is still server-rendered and does not create a client-side toggle.

::: faststrap.components.display.tag.Chip
    options:
        show_source: true

::: faststrap.components.display.tag.ChipGroup
    options:
        show_source: true
For an accessible native control, ordinary non-removable selected chips render as buttons and expose `aria-pressed`. Link chips remain links and use `aria-current` for the selected destination. Removable chips keep their non-button wrapper so the remove button is not nested inside another button. `ChipGroup(selected=...)` synchronizes the selected visual class and ARIA state; it does not add client-side selection behavior by itself.
