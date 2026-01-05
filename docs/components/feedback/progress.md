# Progress

The `Progress` component creates visual progress bars to show completion status. Perfect for uploads, downloads, multi-step forms, and any process with measurable progress.

!!! success "Goal"
    Master creating progress bars, understand Bootstrap progress classes, and build engaging progress indicators that keep users informed.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Progress Documentation](https://getbootstrap.com/docs/5.3/components/progress/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="progress" role="progressbar">
      <div class="progress-bar" style="width: 75%">75%</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Progress

Progress(75, label="75%")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Color Variants - Indicate Status

Use colors to show different states or priorities.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <div class="progress" role="progressbar">
        <div class="progress-bar bg-success" style="width: 25%">25%</div>
      </div>
    </div>
    <div class="mb-3">
      <div class="progress" role="progressbar">
        <div class="progress-bar bg-info" style="width: 50%">50%</div>
      </div>
    </div>
    <div class="mb-3">
      <div class="progress" role="progressbar">
        <div class="progress-bar bg-warning" style="width: 75%">75%</div>
      </div>
    </div>
    <div class="mb-3">
      <div class="progress" role="progressbar">
        <div class="progress-bar bg-danger" style="width: 100%">Complete!</div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Progress(25, variant="success", label="25%")
Progress(50, variant="info", label="50%")
Progress(75, variant="warning", label="75%")
Progress(100, variant="danger", label="Complete!")
```
  </div>
</div>

---

### 2. Striped & Animated - Add Visual Interest

Make progress bars more engaging with stripes and animation.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label small text-muted">Striped</label>
      <div class="progress" role="progressbar">
        <div class="progress-bar progress-bar-striped bg-primary" style="width: 60%"></div>
      </div>
    </div>
    <div class="mb-3">
      <label class="form-label small text-muted">Animated Stripes</label>
      <div class="progress" role="progressbar">
        <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" style="width: 75%"></div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Striped progress bar
Progress(60, variant="primary", striped=True)

# Animated striped progress bar
Progress(75, variant="success", striped=True, animated=True)
```
  </div>
</div>

**When to use animation:**
- ✅ Active uploads/downloads
- ✅ Processing operations
- ✅ Real-time updates
- ❌ Static completion percentages
- ❌ Historical data

---

### 3. Custom Heights - Match Your Design

Adjust bar height for different contexts.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label small text-muted">Thin (5px)</label>
      <div class="progress" role="progressbar" style="height: 5px">
        <div class="progress-bar bg-primary" style="width: 50%"></div>
      </div>
    </div>
    <div class="mb-3">
      <label class="form-label small text-muted">Default (16px)</label>
      <div class="progress" role="progressbar">
        <div class="progress-bar bg-info" style="width: 50%"></div>
      </div>
    </div>
    <div class="mb-3">
      <label class="form-label small text-muted">Thick (30px)</label>
      <div class="progress" role="progressbar" style="height: 30px">
        <div class="progress-bar bg-success" style="width: 50%">50%</div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Thin - subtle indicators
Progress(50, variant="primary", height="5px")

# Default - standard use
Progress(50, variant="info")

# Thick - prominent displays, with labels
Progress(50, variant="success", height="30px", label="50%")
```
  </div>
</div>

---

### 4. Stacked Progress - Multiple Segments

Show multiple progress segments in one bar.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="progress" role="progressbar">
      <div class="progress-bar bg-success" style="width: 30%">30%</div>
      <div class="progress-bar bg-warning" style="width: 20%">20%</div>
      <div class="progress-bar bg-danger" style="width: 15%">15%</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import ProgressBar
from fasthtml.common import Div

# Stacked progress bars
Div(
    ProgressBar(30, variant="success", label="30%"),
    ProgressBar(20, variant="warning", label="20%"),
    ProgressBar(15, variant="danger", label="15%"),
    cls="progress"
)
```
  </div>
</div>

**Perfect for:**
- Storage usage (used/available/reserved)
- Task completion by category
- Resource allocation
- Survey responses by option

---

## Practical Functionality

### File Upload Progress with HTMX

Show real-time upload progress.

```python
from faststrap import Progress, Card, Button
from fasthtml.common import Div, Form, Input

@app.get("/")
def home():
    return Card(
        Form(
            Input(type="file", name="file", cls="form-control mb-3"),
            Button("Upload", type="submit", variant="primary"),
            hx_post="/upload",
            hx_target="#upload-progress",
            hx_encoding="multipart/form-data"
        ),
        Div(id="upload-progress"),
        header="File Upload"
    )

@app.post("/upload")
async def upload(file: UploadFile):
    # Simulate chunked upload with progress updates
    total_size = file.size
    uploaded = 0
    
    # Return progress updates via SSE or polling
    return Progress(
        uploaded,
        max_value=total_size,
        variant="success",
        striped=True,
        animated=True,
        label=f"{(uploaded/total_size)*100:.0f}%"
    )
```

---

### Multi-Step Form Progress

Show users where they are in a multi-step process.

```python
from faststrap import Progress, Card, Button, Fx

def StepIndicator(current_step: int, total_steps: int):
    progress_pct = (current_step / total_steps) * 100
    
    return Card(
        Div(
            Div(
                f"Step {current_step} of {total_steps}",
                cls="text-muted small mb-2"
            ),
            Progress(
                progress_pct,
                variant="primary",
                height="8px",
                cls=Fx.fade_in
            ),
            cls="mb-4"
        ),
        # Form content here
        Div(
            Button("Previous", variant="outline-secondary", 
                   hx_get=f"/step/{current_step-1}" if current_step > 1 else None,
                   disabled=current_step == 1),
            Button("Next", variant="primary",
                   hx_get=f"/step/{current_step+1}" if current_step < total_steps else None),
            cls="d-flex justify-content-between"
        )
    )

@app.get("/step/{step}")
def show_step(step: int):
    return StepIndicator(step, total_steps=5)
```

---

### Dynamic Progress Updates

Update progress in real-time with HTMX polling.

```python
@app.get("/")
def home():
    return Div(
        Button(
            "Start Task",
            hx_post="/start-task",
            hx_target="#progress-container"
        ),
        Div(id="progress-container")
    )

@app.post("/start-task")
def start_task():
    # Start background task
    task_id = start_background_task()
    
    # Return progress bar that polls for updates
    return Div(
        Progress(0, variant="primary", striped=True, animated=True, label="0%"),
        id="task-progress",
        hx_get=f"/task-status/{task_id}",
        hx_trigger="every 1s",  # Poll every second
        hx_swap="outerHTML"
    )

@app.get("/task-status/{task_id}")
def task_status(task_id: str):
    progress = get_task_progress(task_id)  # 0-100
    
    if progress >= 100:
        return Div("Task complete!", cls="alert alert-success")
    
    return Div(
        Progress(progress, variant="primary", striped=True, animated=True, 
                label=f"{progress}%"),
        id="task-progress",
        hx_get=f"/task-status/{task_id}",
        hx_trigger="every 1s",
        hx_swap="outerHTML"
    )
```

---

## Bootstrap CSS Classes Explained

### Core Progress Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.progress` | **Container** - Wraps progress bar(s) | Gray background, rounded corners |
| `.progress-bar` | **Bar** - The colored progress indicator | Fills container based on width |
| `.bg-{variant}` | **Color** - Applies variant color | primary, success, danger, etc. |
| `.progress-bar-striped` | **Stripes** - Diagonal stripe pattern | Visual interest |
| `.progress-bar-animated` | **Animation** - Animates stripes | Moving stripes effect |

### Sizing & Layout

| Class | Purpose | Use Case |
|-------|---------|----------|
| `style="height: Xpx"` | **Custom height** - On `.progress` container | Thin/thick bars |
| `style="width: X%"` | **Progress value** - On `.progress-bar` | Actual progress |
| `.mb-3` | **Margin bottom** - Spacing between bars | Multiple progress bars |

### Accessibility Classes

| Attribute | Purpose | Value |
|-----------|---------|-------|
| `role="progressbar"` | **ARIA role** - Identifies as progress | Always present |
| `aria-valuenow` | **Current value** - For screen readers | 0-100 |
| `aria-valuemin` | **Minimum value** - Usually 0 | 0 |
| `aria-valuemax` | **Maximum value** - Usually 100 | 100 |

---

## Responsive Progress Patterns

### Mobile-Friendly Progress

```python
from faststrap import Progress, Container, Row, Col

Container(
    Row(
        Col(
            Progress(
                75,
                variant="primary",
                height="20px",  # Larger for touch visibility
                label="75%",
                cls="mb-3"
            ),
            cols=12  # Full width on mobile
        )
    )
)
```

### Conditional Styling Based on Progress

```python
def SmartProgress(value: int):
    # Change color based on progress
    if value < 30:
        variant = "danger"
    elif value < 70:
        variant = "warning"
    else:
        variant="success"
    
    return Progress(
        value,
        variant=variant,
        striped=True,
        animated=value < 100,  # Stop animation when complete
        label=f"{value}%"
    )
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

```python
from faststrap import set_component_defaults, Progress

# All progress bars use success variant and stripes
set_component_defaults("Progress", variant="success", striped=True)

# Now all progress bars inherit these defaults
Progress(50)  # ← Automatically success + striped

# Override when needed
Progress(25, variant="danger", striped=False)
```

**Common Default Patterns:**

```python
# Upload-heavy apps - animated progress
set_component_defaults("Progress", striped=True, animated=True)

# Thin progress indicators
set_component_defaults("Progress", height="5px")

# Success-themed apps
set_component_defaults("Progress", variant="success")
```

---

## Common Recipes

### The "Storage Usage" Pattern

Show storage capacity with stacked bars.

```python
def StorageIndicator(used_gb: float, total_gb: float):
    used_pct = (used_gb / total_gb) * 100
    free_pct = 100 - used_pct
    
    return Div(
        Div(
            f"{used_gb:.1f} GB of {total_gb} GB used",
            cls="text-muted small mb-2"
        ),
        Div(
            ProgressBar(used_pct, variant="primary"),
            ProgressBar(free_pct, variant="light"),
            cls="progress"
        )
    )
```

### The "Skill Level" Pattern

Show proficiency levels.

```python
def SkillBar(skill: str, level: int):
    return Div(
        Div(
            skill,
            Badge(f"{level}%", variant="secondary", cls="float-end"),
            cls="mb-1"
        ),
        Progress(level, variant="info", height="8px"),
        cls="mb-3"
    )

# Usage
SkillBar("Python", 90)
SkillBar("JavaScript", 75)
SkillBar("SQL", 85)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | `int` | Required | Current progress value |
| `max_value` | `int` | `100` | Maximum value |
| `variant` | `VariantType \| None` | `"primary"` | Color variant |
| `striped` | `bool \| None` | `False` | Use striped style |
| `animated` | `bool \| None` | `False` | Animate stripes (requires striped=True) |
| `label` | `str \| None` | `None` | Label text to display |
| `height` | `str \| None` | `None` | Custom height (e.g., "20px") |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, id, style) |

::: faststrap.components.feedback.progress.Progress
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.feedback.progress.ProgressBar
    options:
        show_source: true
        heading_level: 4
