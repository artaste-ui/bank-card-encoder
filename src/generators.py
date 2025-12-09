def filter_by_currency(transactions, currency):
    '''Возвращает поочерёдно словарь, отфильтрованный по заданному параметру currency'''
    for x in transactions:
        if x.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield x


def transaction_descriptions(transactions):
    '''Возвращает описание каждой операции по очереди'''
    return (transaction["description"] for transaction in transactions)