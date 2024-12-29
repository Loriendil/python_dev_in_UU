# Домашнее задание по теме "Блокировки и обработка ошибок"
import threading
from random import randint
from time import sleep

class Bank:
    lock = threading.Lock()
    balance:int = 0

    def deposit(self):
        for transaction in range(100):
            rand1 = randint(50, 500)
            with self.lock:
                if self.balance >= 500:
                    break
                sleep(0.001)
                self.balance += rand1
                print(f"Пополнение: {rand1}.Баланс: {self.balance}")

    def take(self):
        for transaction in range(100):
            rand2 = randint(50, 500)
            print(f"Запрос на {rand2}")
            sleep(0.001)
            with self.lock:
                if rand2 <= self.balance:
                    self.balance -= rand2
                    print(f"Снятие: {rand2}.Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')