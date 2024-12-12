# Домашнее задание по теме "Try и Except"
# Функция складывает числа(int, float) и строки(str)
def add_everything_up(a:float | int, b: str)-> str:
    c:str
    try:
        c = a + b
    except TypeError:
        a = str(a)
        b = str(b)
        c = a + b
    return c

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))