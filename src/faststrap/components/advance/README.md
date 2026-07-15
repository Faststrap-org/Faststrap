# `advance/` — Reserved for Future ML/DS Components

This directory is reserved for **advanced ML and data science visualization components** planned for the v0.6.2+ milestone wave.

## Status

The components originally planned here — `DataTable`, `Chart`, `Form Builders`, and general data visualization — have all shipped in their canonical locations:

- `DataTable`, `Chart`, `MetricCard`, `TrendCard`, `KPICard`, `Timeline`, `Stepper`, `CodeBlock`, `JsonViewer` → `display/`
- `FormWizard`, `FormBuilder`, `FormSection`, `LiveValidationField` → `forms/`
- `DashboardGrid`, `FilterBar`, `DateRangePicker`, `MultiSelect`, `RangeSlider`, `ExportButton` → `forms/` and `layout/`

## Planned for This Directory

The following experimental/beta ML visualization components are planned here (marked `@experimental` until stable):

| Component | Description | Status |
|-----------|-------------|--------|
| `DistributionPlot` | Histogram + KDE overlay from pandas Series | Planned |
| `CorrelationMatrix` | Correlation heatmap from DataFrame | Planned |
| `LiveChart` | SSE-powered auto-updating Chart.js chart | Planned |
| `LiveMetric` | Real-time metric display via SSE | Planned |
| `ConfusionMatrix` | sklearn-compatible confusion matrix | Planned |
| `ROCCurve` | ROC curve with AUC annotation | Planned |
| `FeatureImportance` | Feature importance bar chart (sklearn/SHAP) | Planned |
| `ModelMetrics` | Full model evaluation dashboard card | Planned |
| `TimeSeriesPlot` | Time series chart with moving average overlay | Planned |

All components here will:
- Be marked `@experimental` on first ship
- Require `faststrap[chartjs]` or another optional extra where a JS library is needed
- Keep a server-rendered baseline even when JS-enhanced
- Follow the standard `BUILDING_COMPONENTS.md` patterns

## Contributing

See [BUILDING_COMPONENTS.md](../../../BUILDING_COMPONENTS.md) and [ROADMAP.md](../../../ROADMAP.md) for spec details and the planned delivery sequence.
