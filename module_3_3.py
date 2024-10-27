# Домашнее задание по уроку "Распаковка позиционных параметров".
# Создайте функцию print_params() с тремя позиционными параметрами,
# которая принимает три параметра со значениями по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(f'Первый элемент: "{a}" | Второй элемент: "{b}" | Третий элемент: "{c}"')

def print_params2(item, list_my = None):
    if list_my is None:
        list_my = []
        list_my .append(item)
    print(f'Содержимое списка: {list_my}')

# Создаю список values_list с тремя элементами разных типов.
values_list = [5.2, '1234abcd', False]
# Создаю словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
values_dict = {'a': 32, 'b': True, 'c':'efgh5678'}
values_list_2 = [54.32, 'Строка' ]

# Вызываю функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Вызываю функцию print_params без аргументов.
print_params()
# Проверяю, работают ли вызовы функций print_params(b = 25), print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])
# Передаю values_list в функцию print_params, используя распаковку параметров (* для списка)
print_params(*values_list)
# Передаю values_dict в функцию print_params, используя распаковку параметров (** для словаря)
print_params(**values_dict)
# Распаковка и отдельные параметры
print_params(*values_list_2, 42)

# Второй вариант функции из задания
print_params2(25, [1,2,3])