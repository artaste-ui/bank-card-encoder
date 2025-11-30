from typing import Any


def filter_by_state(dict_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, сортирующая список словарей по параметру state"""
    new_list = []
    for i in dict_list:
        if i.get("state") == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(dict_list: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, сорирующая список словарей по параметру date"""
    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse)
