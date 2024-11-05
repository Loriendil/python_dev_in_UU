# Домашняя работа по уроку "Модули и пакеты"
# импортируем из библиотеки math переменную (?) бесконечность inf
from math import inf
# Создаю функцию divide
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second
