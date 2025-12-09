from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Visa 56427548568") == "Visa 5642 75*8 568"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
