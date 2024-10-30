# Самостоятельная работа по уроку "Рекурсия"
# Создаю функцию get_multiplied_digits и параметр number в ней
def get_multiplied_digit(number):
# Создаю переменную str_number и 
# записываю строковое представление 
# числа number в неё используя функцию str()
    str_number = str(number)
# Cоздаю переменную first и 
# записываю в неё первый символ из str_number
# в неё используя функцию int()
    first = int(str_number[0])
# Делаю ветвление основанное на длине оставшегося 
# от расматриваемой строки
    if len(str_number) > 1:
# Умножаю первую цифру числа на результат работы этой же функции с числом,
# но уже без первой цифры
        return first * get_multiplied_digit(int(str_number[1:]))
# если длина строки осталась из одоного символа, то возвращаем этот символ
    elif not len(str_number) > 1: 
        return first

result = get_multiplied_digit(40203)
print(f'Сумма цифр в числе: {result}')
