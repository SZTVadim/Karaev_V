# Karaev_V
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 12) ==========
# Задача 12: Работа со строкой

text = "  Status: OK  "

text = text.strip()
text = text.lower()

print(text)
print(text.endswith("ok"))


# ========== Часть 2 (задача 1) ==========
# Задача 1: Извлечение данных из словаря

user = {"id": 101, "name": "Ivan", "role": "admin", "active": True}

name = user["name"]
role = user["role"]

print(name)
print(role)
