# Задание 1

text_1 = "Привет"
number = 42
float_number = 3.14
numbers = [1, 2, 3]

print(type(text_1))
print(type(number))
print(type(float_number))
print(type(list))


# Задание 2

text_2 = "python PROGRAMMING"

print(text_2.lower())
print(text_2.upper())
print(text_2.capitalize())
print(text_2.title())


# Задание 3

text_with_spaces = "  Hello World  "

print(text_with_spaces.strip())
print(text_with_spaces.lstrip())
print(text_with_spaces.rstrip())


# Задание 4

fruits = "яблоко,банан,апельсин,груша"
fruits_list = fruits.split(",")
fruits_text = " | ".join(fruits_list)

print(fruits_list)
print(fruits_text)


# Задание 5

text_5 = "Я изучаю Python. Python - это круто!"

print(text_5.replace("Python", "Java"))


# Задание 6

text_6 = "Python программирование на Python"

print(text_6.find("Python"))
print(text_6.count("Python"))
print(text_6.find("Java"))


# Задание 7

print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())


# Задание 8

slice_text = "Python very good"

print(slice_text[:3])
print(slice_text[-3:])
print(slice_text[::2])
print(slice_text[::-1])


# Задание 9

print('Он сказал: "Привет"')
print("Первая строка\nВторая строка")
