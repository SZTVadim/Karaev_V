"""
Домашнее задание 14
Тема: ООП - Инкапсуляция, Полиморфизм, Наследование, Абстракция
"""

from abc import ABC, abstractmethod


# ЧАСТЬ 1: Абстракция


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# ЧАСТЬ 2: Наследование


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


# ЧАСТЬ 3: Инкапсуляция


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals


# ЧАСТЬ 4: Полиморфизм


def animal_sound(animal):
    # полиморфизм потому что метод ведет себя неодинаково в зависимости от обьекта
    animal.make_sound()


dog1 = Dog("Лупа", 3)
dog2 = Dog("Пупа", 5)
cat1 = Cat("Кыся", 2)

zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print("Количество животных:", zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)


# Animal() создать напрямую нельзя,
# потому что класс абстрактный, нужно работать через наследников
