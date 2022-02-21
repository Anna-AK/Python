
from mod_16_9 import Restangle, Square, Circle, ClientPetHome, Person, Guest

#modul 16.9.1
sq_1 = Square(2, 3, 5)
circ_1 = Circle(5, -7, 8)

sq_1.getParam()
circ_1.getParam()

# modul 16.9.2
rest_1 = Restangle(0, 0, 5, 7)
rest_1.getAria()

# modul 16.9.3
cl_1 = ClientPetHome("Петр Петров", 150)
cl_2 = ClientPetHome("Виктория Викторова", 550)
cl_1.clientBalans()
cl_2.clientBalans()

# modul 16.9.4
list_guests = [
    {"name": "Петр Петров", "town": "Москва", "status": "Волонтер"},
    {"name": "Павел Павлов", "town": "Санкт-Петербург", "status": "Наставник"},
    {"name": "Виктория Викторова", "town": "Краснодар", "status": "Волонтер"},
    {"name": "Светлана Светлова", "town": "Иркутск", "status": "Наставник"},
]

# Выводим список гостей на консоль в формате: Иван Петров, г. Москва, статус "Наставник"
print("Список на корпоратив:")

for x in list_guests:
    guest = Guest(x['name'], x['town'], x['status'])
    print(guest.guestInfo())
