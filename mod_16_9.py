# modul 16.9.1
# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры.
# Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры. Например, для прямоугольника
# это будут аргументы x, y, width и height.
#
# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
#
# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.

# class Restangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def getParam(self):
#         print(f"Restangle: x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}")


class Square:
    def __init__(self, x, y, widht):
        self.x = x
        self.y = y
        self.width = widht

    def getParam(self):
        print(f"Square: x = {self.x}, y = {self.y}, width = height = {self.width}")


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def getParam(self):
        print(f"Circle: x = {self.x}, y = {self.y}, radius = {self.radius}")


# modul 16.9.2
# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам необходимо получить длину и
# ширину с итоговыми значениями [площади].
#

class Restangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getAria(self):
        print(f"Restangle: width = {self.width}, height = {self.height}, aria = {self.width*self.height}")


# modul 16.9.3
# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить данные
# о своих клиентах и об их финансовых операциях.
#
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
# Клиент "Иван Петров". Баланс: 50 руб.
#

class ClientPetHome:
    def __init__(self, name, balans):
        self.name = name
        self.balans = balans

    def clientBalans(self):
        print(f"Клиент {self.name}. Баланс: {self.balans} руб.")

# modul 16.9.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать
# программу, которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора
# и примените один из принципов наследования.
#
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Person:
    def __init__(self, name, town):
        self.name = name
        self.town = town

class Guest(Person):
    def __init__(self, name, town, status):
        super().__init__(name, town)
        self.status = status

    def guestInfo(self):
        return f'{self.name}, г. {self.town}, статус гостя - {self.status}'

