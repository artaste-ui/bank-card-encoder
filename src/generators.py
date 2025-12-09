def filter_by_currency(transactions, currency):
    '''Возвращает поочерёдно словарь, отфильтрованный по заданному параметру currency'''
    for x in transactions:
        if x.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield x


def transaction_descriptions(transactions):
    '''Возвращает описание каждой операции по очереди'''
    return (transaction["description"] for transaction in transactions)


def card_number_generator(start, stop):
    '''Возвращает сгенерированный номер карты'''
    for n in range(start, stop + 1):
        card = f"{n:016}"
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
