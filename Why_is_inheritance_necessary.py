# Домашнее задание по теме "Зачем нужно наследование"

# класс для описания животного, который создаёт базовое поведение для всех животных
class Animal:
# инициализируем аттрибуты класса и выставляет их в базовые значения
    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

# метод описывающий что случится, если животное съест растение
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# класс для описания растения, которое создаёт базовое поведения для всех животных
class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

# описывая класс Fruit я вынужен пока оставить одинаковый код с код метода __init__() класса Plant
class Fruit(Plant):
    def __init__(self, name, edible = True):
        self.name = name
        self.edible = edible

# Проверка
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
