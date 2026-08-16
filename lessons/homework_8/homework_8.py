# ЗАДАНИЕ 1: Список и list comprehension

temps = [18, 22, -3, 25, 19, -1, 21]

temps_fahrenheit = [temp * 9 / 5 + 32 for temp in temps]

print(temps_fahrenheit)


# ЗАДАНИЕ 2: Словарь и dict comprehension

users = {
    "ivan": "qwerty",
    "maria": "12345",
    "petr": "admin",
    "anna": "pass",
    "guest": "guest"
}

password_lengths = {login: len(password) for login, password in users.items()}

print(password_lengths)


# ЗАДАНИЕ 3: Кортеж и tuple(...)

scores = (10, 7, 0, 9, 8, 5)

scores_x_10 = tuple(round(element * 1.1, 1) for element in scores)

print(scores_x_10)
