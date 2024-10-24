# Дополнительное практическое задание по модулю: "Основные операторы"
# Задание "Слишком древний шифр"
# Суть задачи: по заданному числу подобрать такие пары чисел, чтобы они были одновременно и суммой меньше заданного,
# и в сумме кратны заданному.

# Запрашиваем число у пользователя
print(f'Введите натуральное число от 3 до 20: ')
n = int(input())
# создаём пустую строковую переменную
result = ''
# пользователь может ввести любое число, поэтому выделим нужный нам диапазон числе
if n < 3 or n > 20:
    print('incorrect input')
else:
# Создаём два цикла. Один будет перебирать числа (по i) для первой половины пары,
# другой (по j) для другой половины пары.
    for i in range(1, n):
        for j in range(2, n):
# Условие важно, потому что мы можем выйти из цикла не удовлетворив условиям и от того может случиться ситуация - i > j,
# а это нам как раз и не нужно.
            if i < j:
# это условие берётся из того, что в условии задачи сказано, что n "было кратно(делилось без остатка) сумме их значений"
# кратность это деление без остатка, а сумма это сумма как раз i и j.
                if n % (i + j) == 0:
                    result += str(i) + str(j) + ' '
    print(result)