def filter_by_currency(transactions, currency):
    '''Возвращает поочерёдно словарь, отфильтрованный по заданному параметру currency'''
    for x in transactions:
        if x.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield x


