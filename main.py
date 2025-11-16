from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    card = input("Введите номер карты: ")
    account = input("Введиет номер счёта: ")
    user_input = input("Введите тип и номер (например, Visa 7000...): ")
    date_string = input("Введите дату: ")
    print(get_mask_card_number(card))
    print(get_mask_account(account))
    print(mask_account_card(user_input))
    print(get_date(date_string))
