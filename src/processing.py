def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    new_list = []
    for i in dict_list:
        if i.get("state") == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(dict_list: list, reverse: bool = True) -> list:
    return sorted(dict_list, key=lambda x: x['date'], reverse=reverse)
