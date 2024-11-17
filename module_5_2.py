# Домашняя работа по уроку "Специальные методы классов"
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
# Реализую магический метод __len__()
    def __len__(self):
        return self.number_of_floors
# Реализую магический метод __str__()
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
# Создаю 2 объекта класса House с произвольным названием и количеством этажей
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# Вызываю методы __len__() и __str__() у этого объекта с произвольным числом

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))