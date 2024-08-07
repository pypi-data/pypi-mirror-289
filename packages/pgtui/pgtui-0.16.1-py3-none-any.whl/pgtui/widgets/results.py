import re
from datetime import datetime
from itertools import cycle
from typing import Any, Iterable

from psycopg import Column
from psycopg.rows import TupleRow
from rich.text import Text
from textual.app import events
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import DataTable, Label, TabbedContent, TabPane
from textual.widgets.data_table import CursorType

from pgtui.entities import DataResult, ErrorResult, Result, ResultSet
from pgtui.utils import random_id
from pgtui.utils.datetime import format_duration
from pgtui.widgets.status_bar import StatusBar


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
        self.pane_ids: list[str] = []
        super().__init__()

    def compose(self):
        results = self.result_set.results

        if not results:
            yield Label("No data")
            return

        elif len(results) == 1:
            yield ResultWidget(results[0])

        else:
            with TabbedContent():
                for result in results:
                    pane_id = random_id()
                    self.pane_ids.append(pane_id)
                    title = result.command_status or "???"
                    with TabPane(title, id=pane_id):
                        yield ResultWidget(result)

    # Switch tabs with alt+n
    def on_key(self, event: events.Key):
        if not self.pane_ids:
            return

        if m := re.match(r"^alt\+([0-9])$", event.key):
            event.stop()
            idx = int(m.group(1)) - 1
            if idx < len(self.pane_ids):
                tc = self.query_one(TabbedContent)
                tc.active = self.pane_ids[idx]
                assert tc.active_pane
                tc.active_pane.query(ResultsTable).focus()
                tc.active_pane.query(ResultInfo).focus()


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
