# Домашняя работа по уроку "Перегрузка операторов"

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
# Реализую магический метод таким образом, чтобы зайдя в первое условие,
# интерпретатор при необходимости зашёл в следующее, поэтому используем конструкцию if-elif
# в отладке, конечно, яснее будет видно, когда два if принудительно и независимо друг от друга
# вычисляются, но мне этого не надо. Первое условие прошло, значит всё нормально (второе страхует, а
# если случится аномалия, то просто вернём False, что соответствует действительности).
# Здесь нужно вернуть не объект типа House, а значение True / False, поэтому я собственно и не создаю
# как в методе __add__() новый экземпляр типа House.
# Остальные магические методы до перегрузки сложения сделаны по аналогии с методом __eq__()
# По искав в интернете ответ на вопрос почему и зачем в задании с нас требуют использование isinstance(),
# я пришёл к выводу, что это важно для того, чтобы быть точно уверенным в том, что объекты, которые я сравниваю
# точно объекты одного типа, типы полей класса точно совпадают с каждым типом каждого поля моего класса.
# Не появится какого-то неожиданного поведения или ошибок несовместимости.
# Иными словами, если условие с использованием isinstance() выполнено, значит операция типобезопасна
# и однозначно выполнится правильно.
# Это, в том числе может служить ограничением для сложения только наших экземпляров хорошим способом
# (через принудительный вызов ошибки) запретом на сложение экземпляра нашего класса с встроенным типом данных.
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self.number_of_floors == other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self < other
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self <= other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self > other
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self >= other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other.number_of_floors, int):
            return self != other
        else:
            return False
# На многих обучающих сайтах по Python, но не на всех
# (тот же: https://www.toppr.com/guides/python-guide/tutorials/python-object-class/python-operator-overloading/
#  или
# https://www.programiz.com/python-programming/operator-overloading ),
# которые я смог найти возвращают значения, так же как и в уроке - возвращая сумму полей, но вещь это не логичная.
# Мы складываем объекты, значит и возвращать должны объекты. Ниже представлена моя реализация.
# Try-catch-finally (из С#) или try-catch(...) (из С++) мы ещё не знаем, поэтому не будем пока гуглить,
# как это делается в Python и просто вернём то же число, в случае когда у нас произошла аномалия и
# внезапно объект у нас совсем не подходит. Логика в выборе if- elif / isinstance() и та же.

    def __add__(self, value):
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        elif isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            return House(self.name, self.number_of_floors)

    def __radd__(self, value):
        if isinstance(value, House):
            return House(self.name, value.number_of_floors + self.number_of_floors)
        elif isinstance(value, int):
            return House(self.name, value + self.number_of_floors)
        else:
            return House(self.name, self.number_of_floors)

    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return House(self.name, self.number_of_floors)
        elif isinstance(value, int):
            self.number_of_floors += value
            return House(self.name, self.number_of_floors)
        else:
            return House(self.name, self.number_of_floors)


# Создаю 2 объекта класса House с произвольным названием и количеством этажей
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# Вызываю методы __len__() и __str__() у этого объекта с произвольным числом

print(h1)
print(h2)

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__

print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
