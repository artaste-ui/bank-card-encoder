from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Принимает все данные карты пользователя"""
    parts = user_input.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """
    Принимает: '2024-03-11T02:26:18.671407'
    Возвращает: '11.03.2024'
    """
    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
