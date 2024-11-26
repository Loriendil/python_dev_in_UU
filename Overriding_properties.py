# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

# Создаю родительский класс Vehicle.
class Vehicle:
    # Создаю атрибут класса, который имеет константное (постоянное) значение
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # Создаю атрибуты объекта и присваиваю им значения
    def __init__(self, owner:str, __model:str,  __color:str, __engine_power:int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def print_info(self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horsepower(self))
        print(Vehicle.get_color(self))
        print(f'Владелец: {self.owner}')
#Создаю методы класса которые предназначены для установки и получения значений
# приватных полей класса. Наличие сеттера даёт возможность изменить значение поля,
# в то время как его отсутствие означает такое отсутствие. Такая же ситуация с геттером.
# Методы возвращают строку заданного в ТЗ вида.
    def get_model(self):
        return  f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'
# Реализуем сеттер для цвета таким образом, чтобы можно было получить доступ к
# переменной  __COLOR_VARIANTS с помощью self
    def set_color(self,  new_color:str):
        if  new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color =  new_color
            return
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Создаю класс Sedan и делаю его дочерним у класса Vehicle
class Sedan(Vehicle):
# Создаю аттрибут класса
    __PASSENGERS_LIMIT = 5

# Проверка из задания
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в том числа вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()