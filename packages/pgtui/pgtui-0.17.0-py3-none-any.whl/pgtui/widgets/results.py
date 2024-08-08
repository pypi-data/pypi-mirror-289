from datetime import datetime
from itertools import cycle
from typing import Any, Iterable

from psycopg import Column
from psycopg.rows import TupleRow
from rich.text import Text
from textual import on, work
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import DataTable, Label, TabbedContent, TabPane
from textual.widgets.data_table import CursorType

from pgtui.entities import DataResult, ErrorResult, Result, ResultSet
from pgtui.utils.datetime import format_duration
from pgtui.widgets.status_bar import StatusBar
from pgtui.widgets.tabbed_content import SwitchingTabbedContent


class Results(Widget):
    DEFAULT_CSS = """
    Results:focus-within {
        background: $boost;
    }

    TabPane {
        padding: 0;
    }
    """

    def __init__(self, result_set: ResultSet):
        self.result_set = result_set
        super().__init__()

    def compose(self):
        results = self.result_set.results

        if not results:
            yield Label("No data")
            return

        elif len(results) == 1:
            yield ResultWidget(results[0])

        else:
            with SwitchingTabbedContent(id="results_tabbed_content"):
                for result in results:
                    title = result.command_status or "???"
                    with TabPane(title):
                        yield ResultWidget(result)

    @on(TabbedContent.TabActivated)
    def _on_tab_activated(self, event: TabbedContent.TabActivated):
        if event.tabbed_content.id == "results_tabbed_content":
            self._focus_result()

    # Make this exclusive so future events will cancel any pending ones.
    # This speeds up skipping over tabs.
    @work(group="_focus_result", exclusive=True)
    async def _focus_result(self):
        tc = self.query_one(SwitchingTabbedContent)
        assert tc.active_pane is not None
        tc.active_pane.query_one(ResultWidget).focus_result()


class ResultWidget(Widget):
    DEFAULT_CSS = """
    ResultWidget {
        height: auto;
    }
    """

    def __init__(self, result: Result):
        super().__init__()
        self.result = result

    def compose(self):
        with Container():  # without this scroll is broken
            if isinstance(self.result, DataResult):
                yield ResultsTable(self.result.rows, self.result.columns)
                yield StatusBar(self._format_status(self.result))
            else:
                yield ResultInfo(self.result)

    def focus_result(self):
        # It's one or the other
        self.query(ResultsTable).focus()
        self.query(ResultInfo).focus()

    def _format_status(self, result: DataResult):
        duration = format_duration(result.duration)
        fetched = len(result.rows)
        total = result.num_rows

        if fetched != total:
            return f"Fetched {fetched}/{total} rows in {duration}"
        else:
            return f"Fetched {total} rows in {duration}"


class ResultInfo(Widget, can_focus=True):
    DEFAULT_CSS = """
    ResultInfo {
        padding: 1;
        .title { text-style: bold }
        .query { text-style: dim }
        .error { color: $error-lighten-1 }
    }
    """

    def __init__(self, result: Result):
        super().__init__()
        self.result = result

    def compose(self):
        yield Label(f"{datetime.now()}", classes="title")
        yield Label(f"Query: {self.result.query}", classes="query")
        yield Label(f"Status: {self.result.exec_status.name}")
        if self.result.num_rows is not None:
            yield Label(f"Affected rows: {self.result.num_rows}")
        yield Label(f"Time: {format_duration(self.result.duration)}")
        for notice in self.result.notices:
            yield Label(notice, classes="warning")
        if isinstance(self.result, ErrorResult):
            yield Label(f"ERROR: {self.result.error}", classes="error")


class ResultsTable(DataTable[Any]):
    BINDINGS = [
        ("s", "toggle_cursor", "Selection"),
    ]

    def __init__(
        self,
        rows: Iterable[TupleRow] | None = None,
        columns: Iterable[Column] | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ):
        super().__init__(id=id, classes=classes, disabled=disabled)
        self.cursors: Iterable[CursorType] = cycle(["cell", "row", "column", "none"])
        self.cursor_type = next(self.cursors)

        if columns:
            column_names = [c.name for c in columns]
            self.add_columns(*column_names)

        if rows:
            self.add_rows(mark_nulls(rows))

    def action_toggle_cursor(self):
        self.cursor_type = next(self.cursors)


NULL = Text("<null>", "dim")


def mark_nulls(rows: Iterable[TupleRow]) -> Iterable[TupleRow]:
    """Replaces nulls in db data with a styled <null> marker."""
    return (tuple(cell if cell is not None else NULL for cell in row) for row in rows)
