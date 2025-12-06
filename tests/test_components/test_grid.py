"""Tests for Grid components (Container, Row, Col)."""

from faststrap.components.layout import Container, Row, Col


class TestContainer:
    """Tests for Container component."""

    def test_container_basic(self):
        """Container renders with fixed width."""
        container = Container("Content")
        html = str(container)

        assert "Content" in html
        assert "container" in html
        assert "container-fluid" not in html

    def test_container_fluid(self):
        """Container can be fluid (full-width)."""
        container = Container("Content", fluid=True)
        html = str(container)

        assert "container-fluid" in html

    def test_container_fluid_string(self):
        """Container accepts 'fluid' as string."""
        container = Container("Content", fluid="fluid")
        html = str(container)

        assert "container-fluid" in html

    def test_container_responsive_fluid(self):
        """Container can be fluid until breakpoint."""
        container = Container("Content", fluid="lg")
        html = str(container)

        assert "container-lg" in html


class TestRow:
    """Tests for Row component."""

    def test_row_basic(self):
        """Row renders correctly."""
        row = Row("Content")
        html = str(row)

        assert "Content" in html
        assert "row" in html

    def test_row_cols(self):
        """Row can specify number of columns."""
        row = Row("Content", cols=3)
        html = str(row)

        assert "row-cols-3" in html

    def test_row_responsive_cols(self):
        """Row supports responsive column counts."""
        row = Row("Content", cols=1, cols_md=2, cols_lg=3)
        html = str(row)

        assert "row-cols-1" in html
        assert "row-cols-md-2" in html
        assert "row-cols-lg-3" in html


class TestCol:
    """Tests for Col component."""

    def test_col_auto(self):
        """Col with auto width."""
        col = Col("Content")
        html = str(col)

        assert "Content" in html
        assert "col" in html

    def test_col_fixed_span(self):
        """Col with fixed span."""
        col = Col("Content", span=6)
        html = str(col)

        assert "col-6" in html

    def test_col_responsive(self):
        """Col with responsive sizing."""
        col = Col("Content", span=12, md=6, lg=4)
        html = str(col)

        assert "col-12" in html
        assert "col-md-6" in html
        assert "col-lg-4" in html

    def test_col_offset(self):
        """Col with offset."""
        col = Col("Content", span=6, offset=3)
        html = str(col)

        assert "col-6" in html
        assert "offset-3" in html

    def test_col_responsive_offset(self):
        """Col with responsive offsets."""
        col = Col("Content", span=6, offset_md=2, offset_lg=3)
        html = str(col)

        assert "offset-md-2" in html
        assert "offset-lg-3" in html


class TestGridIntegration:
    """Integration tests for grid system."""

    def test_container_row_col(self):
        """Complete grid structure works."""
        grid = Container(Row(Col("Column 1", span=6), Col("Column 2", span=6)))
        html = str(grid)

        assert "container" in html
        assert "row" in html
        assert "col-6" in html
        assert "Column 1" in html
        assert "Column 2" in html

    def test_responsive_grid(self):
        """Responsive grid layout."""
        grid = Container(
            Row(
                Col("A", span=12, md=6, lg=4),
                Col("B", span=12, md=6, lg=4),
                Col("C", span=12, md=12, lg=4),
            ),
            fluid="lg",
        )
        html = str(grid)

        assert "container-lg" in html
        assert "col-12" in html
        assert "col-md-6" in html
        assert "col-lg-4" in html
