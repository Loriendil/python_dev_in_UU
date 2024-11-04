# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Составим рекурсивную функцию, которая имеет позиционный параметр.
# Этот параметр нужен для того, чтобы передать именно список в качестве аргумента, а
# если бы нужно было передать словарь, то нужно было бы писать **kwargs, так как
# тут нужен будет именованный параметр.
def calculate_structure_sum(*args):
# разделения на отдельно сумму по числам, и отдельно на сумму по строкам нет в ТЗ,
# поэтому пишем всё в одну строку.
    res = 0
# Поскольку у нас на входе заранее известно, что будет исключительно список,
# я могу написать такой цикл.
    for item in args:
# Использую встроенную функцию isinstance() для проверки типа данных.
# Она хороша тем, что ей можно передать несколько типов.
        if isinstance(item, (int, float)):
            res += item
# Ещё один способ проверить, просто интересная идея:
        elif type(item) is str:
            res += len(item)
# Список и кортеж здесь отдельно от словаря,
# потому что словарь имеет грубо говоря отдельную структуру, а
# в кортеже и списке нет именованной части.
# Множество также требует отдельного условия, потому что
# в множестве может быть и кортеж, и список, а в кортеже или списке так не может быть.
# UPD:  В списке может быть кортеж! Это я ошибся в рассуждениях! В кортеже может быть список!
# Я только сейчас понял! Это можно всё запихнуть в один цикл перебора по элементам коллекции!
# Множества, списки и кортежи объединяет одно общее свойство - нет именнованных полей! Это всё анонимные коллекции!
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                res += calculate_structure_sum(element)
# перечисляем по паре ключ-значение и суммируем их по ходу итерации
        elif isinstance(item, dict):
            for key, value in item.items():
                res += calculate_structure_sum(key) + calculate_structure_sum(value)
    return res

# Этот код напрямую взят из урока
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print("Сумма: ", result)