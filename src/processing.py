from typing import Any

info_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(list_of_dictionaries: list[dict[str, Any]], state_id: str = 'EXECUTED') -> list[dict[str, Any]]:
    """ Функция, которая принимает список словарей и значений для ключа state, после чего
    возвращает список, содержащий только словари с указанным ключом"""

    result_list = []

    for key in list_of_dictionaries:
        if key.get('state') == state_id:
            result_list.append(key)
    return result_list


def sort_by_date(info_list: list[dict[str, Any]], sort: bool = True) -> list[dict[str, Any]]:
    """ Функция, которая принимает список, после чего возвращает отсортированный по дате список """
    sorted_list = sorted(info_list, key=lambda x: x['date'], reverse=sort)
    return sorted_list


print(sort_by_date(info_list))
