# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"
# создаём переменные и тут же преобразуем ввод с клавиатуры в переменную типа int
first = int(input())
second = int(input())
third =int(input())

# проверяем равны ли между собой все переменные
# и выводим 3, если да.
if first==second==third:
    print('3')
# проверяем на равенство 2 других переменных первой и выводим 2, если да.
elif first==second or first==third:
    print('2')
# проверяем на равенство 2 других переменных второй и выводим 2, если да.
elif second==first or second==third:
    print('2')
# проверяем на равенство 2 других переменных третьей и выводим 2, если да.
elif third==first or third==second:
    print('2')
# оставшийся вариант это неравенство переменных друг другу
# и выводим 0, если да.
else:
    print('0')