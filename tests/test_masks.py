import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("5642754865681234", "5642 75** **** 1234"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_num, cypher",
    [
        ("7000792289606361", "**6361"),
        ("5642754865681234", "**1234"),
    ],
)
def test_get_mask_account(card_num: str, cypher: str) -> None:
    assert get_mask_account(card_num) == cypher
