# Задание 1

fruits_1 = ["яблоко"]

fruits_1.append("банан")
print(fruits_1)

fruits_1.extend(["апельсин", "груша"])
print(fruits_1)

fruits_1.insert(1, "виноград")
print(fruits_1)


# Задание 2

fruits_2 = ["яблоко", "банан", "апельсин", "банан"]

fruits_2.remove("банан")
print(fruits_2)

deleted_fruit = fruits_2.pop()

print(fruits_2)
print(deleted_fruit)


# Задание 3

fruits_3 = ["яблоко", "банан", "апельсин", "банан"]

banana_index = fruits_3.index("банан")
banana_count = fruits_3.count("банан")

print(banana_index)
print(banana_count)


# Задание 4

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers.sort()
numbers.reverse()

print(numbers)
