from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    card = input("Введите номер карты: ")
    account = input("Введиет номер счёта: ")
    user_input = input("Введите тип и номер (например, Visa 7000...): ")
    print(get_mask_card_number(card))
    print(get_mask_account(account))
    print(mask_account_card(user_input))
