from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    card = input("Введите номер карты: ")
    account = input("Введиет номер счёта: ")
    print(get_mask_card_number(card))
    print(get_mask_account(account))
