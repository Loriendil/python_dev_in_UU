# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# Создаю список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаю список, в который я буду складывать только простые числа
primes = []
# Создаю список, в который я буду складывать не простые числа
not_primes = []

# Создаём цикл, который перебирает все элементы списка
for i in range(len(numbers)):
# Поскольку число 1 не относится ни к простым, ни к сложным числам, отбросим его и
# заодно все отрицательные числа
    if numbers[i] <= 1:
        continue
    else:
        # Создаём флаг, обозначающий нахождение простого числа
        is_prime = True
        # Создаём цикл, который перебирает множители. В примечании к заданию сказано о
        # необходимости проверки на простоту числа нужно убедиться, что выбранное число
        # не делиться ни на что в диапазоне от 2 до этого числа (не включительно).
        # В интернете говорят, что выгоднее проверять до квадратного корня из рассматриваемого числа.
        # После извлечения корня float приводится к int в сторону уменьшения, поэтому прибавляем 1, потому что
        # нам нужно в сторону увеличения.
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
        # на данном диапазоне числе множители быстро кончаются, поэтому нет смысла поверят до конца и
        # просто прерываем цикл как только выполнится условие
                break
        # После установления флага по нему добавляем в выбранный список
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])

print('Исходный код: ')
print('number = ', numbers)
print('Вывод в консоль: ')
print('Primes: ', primes)
print('Not Primes: ', not_primes)