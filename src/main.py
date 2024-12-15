from typing import Union


def get_mask_card_number(n: Union[str]) -> Union[str]:
    """Функция для создания маски номера карты"""
    mask = ""
    if len(n) != 16:
        return "Некорректный ввод"
    # Создаём маску
    for i in range(len(n)):
        if i in range(6, 12):
            mask = (mask + "*")
        else:
            mask = mask + n[i]
    # Вставляем в маску пробелы
    mask = mask[:4] + " " + mask[4:]
    mask = mask[:9] + " " + mask[9:]
    mask = mask[:14] + " " + mask[14:]

    return mask


def get_mask_account(n: Union[str]) -> Union[str]:
    """Функция для создания маски номера счёта"""
    mask = "**" + n[-4:]
    return mask


# Просим пользователя ввести номер карты и выводим маску номера карты
print("Впишите номер карты:")

user_input = input()
print(get_mask_card_number(user_input))

# Просим пользователя ввести номер счёта и выводим маску номера счёта
print("Впишите номер счёта")

user_input = input()
print(get_mask_account(user_input))
