from typing import Any

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(ex_list: list[dict[str, Any]], sorted_by_state_test: list[dict[str, Any]]) -> None:
    assert filter_by_state(ex_list) == sorted_by_state_test


def test_sort_by_date(ex_list: list[dict[str, Any]], sorted_by_date_test: list[dict[str, Any]]) -> None:
    assert sort_by_date(ex_list) == sorted_by_date_test
