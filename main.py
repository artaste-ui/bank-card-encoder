from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425531"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]

    card = input("Введите номер карты: ")
    account = input("Введиет номер счёта: ")
    user_input = input("Введите тип и номер (например, Visa 7000...): ")
    date_string = input("Введите дату: ")
    print(get_mask_card_number(card))
    print(get_mask_account(account))
    print(mask_account_card(user_input))
    print(get_date(date_string))

    print("Только выполненные (EXECUTED):")
    print(filter_by_state(operations))

    print("\nТолько отменённые (CANCELED):")
    print(filter_by_state(operations, "CANCELED"))

    print("\nОтсортированные от новых к старым:")
    print(sort_by_date(operations))

    print("\nОтсортированные от старых к новым:")
    print(sort_by_date(operations, reverse=False))
