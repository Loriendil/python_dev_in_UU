# Домашнее задание по теме "Потоки на классах"

import threading
import time
class Knight(threading.Thread):
    def __init__(self, name:str, power:int)->None:
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self)->None:
        print(f"{self.name},На нас напали враги!")
        self.battle(self.name, self.power)

    @staticmethod
    def battle(name:str, power:int):
        days:int = 1
        enemies:int = 100
        while enemies != 0:
            time.sleep(1)
            enemies -= power
            days += 1
            print(f"{name} сражается {days} день ..., осталось {enemies} воинов")
        print(f"{name} одержал победу спустя {days} дней(дня)")

# Создание класса

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились!")