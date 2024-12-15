def get_mask_card_number(n) -> str:
    """Функция для создания маски номера карты"""
    mask = ""
    # Создаём маску
    for i in range(len(n)):
        try:
            int(n[i])
        except ValueError:
            pass
        else:
            p = i
            for t in range(len(n)):
                if t in range(p+6, len(n)-4):
                    mask += "*"
                else:
                    mask += n[t]

            # Вставляем в маску пробелы
            mask = mask[:p+4] + " " + mask[p+4:]
            mask = mask[:p+9] + " " + mask[p+9:]
            mask = mask[:p+14] + " " + mask[p+14:]
            return mask


def get_mask_account(n) -> str:
    """Функция для создания маски номера счёта"""
    for i in range(len(n)):
        try:
            int(i)
        except ValueError:
            pass
        else:
            mask = "Счет **" + n[-4:]
            return mask


def mask_account_card(n) -> str:
    if "Счет" in n or "Счёт" in n:
        return get_mask_account(n)
    else:
        return get_mask_card_number(n)


def get_date(date) -> str:
    """Функция, обрабатывающая дату"""
    date_uncoded = ""
    for i in range(len(date)):
        if i not in range(10, len(date)) and date[i] != "-":
            date_uncoded += date[i]
        else:
            pass
    # Вставляем точки
    date_uncoded = date_uncoded[:4] + "." + date_uncoded[4:]
    date_uncoded = date_uncoded[:7] + "." + date_uncoded[7:]
    return date_uncoded


# Пользователь вводит номер карты или счета
user_input_num = input()
print(mask_account_card(user_input_num))

# Пользователь вводит необработанную дату
user_input_date = input()
print(get_date(user_input_date))
