# Домашнее задание по теме "Очереди для обмена данными между потоками."
import queue
from threading import Thread
from time import sleep
from random import randint


class Table:
    def __init__(self, number: int):
        self.number = number
        # вообще тут скрытое преобразование типа на самом деле!
        # С этим к сожалению ничего не сделать - так написано задание!
        # По-хорошему нужен Nullable, но кто же нам об этом расскажет...
        self._guest = None

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, value):
        self._guest = value

class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.customers_threads = []
        self.q = queue.Queue()

    def guest_arrival(self, *customers):
        # создаём очередь для ожидающих гостей
        for table, guest in zip(self.tables, customers):
            table.guest = guest
            print(f"{guest.name} сел(-а) за стол номер {table.number}")
            table.guest.start() # Запускаем поток представляющий клиента кафе

        # записываем тех, кого персонал кафе должен обслужить
        for customer in customers[len(self.tables):]:
            self.q.put(customer)
            print(f"{customer.name} в очереди")

    # Обслуживание гостей.
    # По-хорошему стоило бы назвать этот метод serving_clients, а
    # то деньги с гостей брать это прям верх коммерсантства.
    def discuss_guests(self):
    # Обслуживание происходит пока очередь не пустая или хотя бы один стол занят
        while not self.q.empty() or any(table.guest is not None for table in self.tables):
    # перебор по столам и завершение потоков, представляющих клиентов кафе, которые уже за столами.
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол № {table.number} свободен")
                    table.guest.join() # Останавливаем поток представляющий клиента кафе
                    table.guest = None

    # перебор по очереди и запуск потоков, представляющих клиентов кафе, которые
    # ещё в очереди и требуется их "поместить" за стол
                if not self.q.empty() and table.guest is None:
                    guest = self.q.get()
                    table.guest = guest
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол № {table.number}")
                    table.guest.start()  # Запускаем поток представляющий клиента кафе


if __name__ == '__main__':
    # Такой код предлагается заданием использовать, поэтому куда я денусь...
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()