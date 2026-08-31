# ЗАДАНИЕ 1: Класс Book (Книга)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book_1 = Book("1984", "Джордж Оруэлл", 300)
book_2 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 100)
book_3 = Book("Мастер и Маргарита", "Михаил Булгаков", 400)

print(book_1.get_info())
print(book_2.get_info())
print(book_3.get_info())

print(book_1.is_long())
print(book_2.is_long())
print(book_3.is_long())


# ЗАДАНИЕ 2: Класс BankAccount (Банковский счет)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Валерий")

account.deposit(1000)

print(account.withdraw(500))
print(account.withdraw(1000))

print(account.get_balance())
