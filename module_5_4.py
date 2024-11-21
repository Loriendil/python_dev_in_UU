# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"
# Задача "История строительства"

# Создаю класс House
class House:
# В классе House создаю атрибут houses_history = [], который будет хранить названия созданных объектов.
    houses_history = []
    def __new__(cls, *args: str, **kwargs: int):
# Вписываю ограничение по типу для входного параметра *args, **kwargs
# Название строения (например, 'ЖК Эльбрус') из входного параметра конструктора класса
# берётся по первому элементу кортежа.
# С помощью встроенного метода .append() класса list() добавляю в список название строения,
# используя ссылку на сам класс - cls.
        cls.houses_history.append(args[0])
        instance = super(House, cls).__new__(cls)
        return instance

# Для того чтобы не было свалки данных введём позиционный аргумент name и именованный аргумент floors.
# Заодно повысим читаемость кода.
    def __init__(self, name, floors):
        self.args = name
        self.kwargs = floors

    def __del__(self):
# при удалении благодаря разделению на name и floors я могу вполне легально использовать без индексов
# и остальной магии (в плохом смысле этого слова) просто ссылку на args.
        print(f'{self.args} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)