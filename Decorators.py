# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        print(n)
        if n <= 1:
            raise ValueError('Не верный ввод')
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 'Составное'
        return 'Простое'
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third

result = sum_three(2, 3, 6)
print(result)