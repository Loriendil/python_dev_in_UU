# Домашняя работа по уроку "Функции в Python. Функция с параметром"
# создаём функцию, принимающую 3 параметра: n - количество строк, m - количество столбцов
def  get_matrix (n, m, value):
# создаём пустую матрицу - вектор-строку
    matrix = []
# По условию задачи, в случае передачи аргумента со значением 0 или меньше,
# будет возвращаться пустой список. Пустой двухмерный массив или нет, не сказано,
# поэтому делаю самый простой вариант.
    if value <= 0:
        return matrix
# Во внешнем цикле создаём пустой список, а наполняем его во внутреннем цикле сразу значениями
# из переменной value
    else:
# вариант № 1: делаем циклы и решаем в лоб.
        for i in range(n):
            row = []
            for j in range(m):
                row.append(value)
            matrix.append(row)
# Вариант № 2: листая интернет на предмет советов как логичнее и правильнее инициализировать двухмерную матрицу,
# наткнулся на полезную ссылку в одном из комментариев:
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# где сказано, что такой способ не очень хороший (как вариант № 1), но там не было (ну, или я не понял)
# как делать двухмерную матрицу, поэтому написал вот такой код.
# Делают они все одинаково, но вот второй мне кажется красивее.
        matrix = [[value]*n for i in range(m)]
        return matrix
# вызываем функцию для каждого варианта
# result0 - смотрим как функция даст нам отказ
# result1 - квадратная матрица
# result2 - матрица с длинными строками
# result3 - матрица с длинными столбцами
result0 = get_matrix(2,2,-1)
result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)

# выводим решения в консоль
print(result0)
print(result1)
print(result2)
print(result3)
