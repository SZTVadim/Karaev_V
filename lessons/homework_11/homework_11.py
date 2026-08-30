# ЗАДАНИЕ 1: Функции и условия


def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка"

    return price + price * tax_percent / 100


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


# ЗАДАНИЕ 2: Функции с условиями и match/case


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(calculate_total(1000, 10))
print(get_level(75))
print(process_status("pending"))
