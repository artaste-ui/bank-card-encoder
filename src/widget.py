from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(user_input: str) -> str:
    """Принимает все данные карты пользователя"""
    parts = user_input.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"