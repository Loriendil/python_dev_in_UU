# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list:list[int | float], *functions)->dict[str, int | float]:
    """
    Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.

    :param int_list: Список из чисел
    :param functions: неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    :return: словарь, где ключом будет название вызванной функции, а значением -
            её результат работы со списком int_list
    """
    results = dict()

    for function in functions:
        results[function.__name__] = function(int_list)

    return results

print(apply_all_func([6,20, 15, 9], max,min))
print(apply_all_func([6,20, 15, 9], len, sum, sorted))