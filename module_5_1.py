# Домашняя работа по уроку "Атрибуты и методы объекта"
# Создаю класс House
class House:
# Создаю конструктор класса House с помощью ключевого слова __init__
    def __init__(self, name, number_of_floors):
# Создаю два поля: self.name - имя, self.number_of_floors - кол-во этажей
        self.name = name
        self.number_of_floors = number_of_floors
# Создаю метод класса go_to() выводящий на экран(в консоль) значения от 1 до new_floor(включительно).
    def go_to(self, new_floor):
        if self.number_of_floors > new_floor > 0:
            for floor in range(new_floor+1):
                print(f'Этаж № {floor}')
        else:
            print('Такого этажа не существует')

# Создаю 2 объекта класса House с произвольным названием и количеством этажей
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# Вызываю метод go_to() у этого объекта с произвольным числом
h1.go_to(5)
h2.go_to(10)