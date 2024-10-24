# Домашняя работа по уроку "Пространство имён"
# Описываем сначала функции, потом основной код. Наоборот не работает, почему-то.
# На самом деле поскольку тут нет декларирования сигнатуры метода,
# поэтому тут собственно и не должно так работать...
calls = 0

# Опишем функцию подсчёта вызовов функций
def count_calls():
    global calls
    calls += 1

# Опишем функцию, считающую количество символов (len()), выводящую слово заглавными(upper()) и
# прописными буквами (lower())Код: "str.upper(str1)"  PyCharm не подчёркивает как ошибку, но это ОШИБКА!!! 
def string_info(str1):
    count_calls()
    return len(str1), str1.upper(), str1.lower()

# Опишем функцию, которая проверяет содержание в представленном списке слова
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower() # подсказка в примечаниях в самом задании! Все в одном регистре!
    for item in list_to_search:
        if string.lower() == item.lower():
            return True # Дьявольское форматирование! Следите за отступами и табуляциями ... 
    return False

# Тело основной "функции"
print('------------------------------------------------------------------------------------------------')
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

print('------------------------------------------------------------------------------------------------')

print(string_info('Tetrakishexahedron'))
print(string_info('Ichthyophagous'))
print(is_contains('Rhabdophobia', ['phob', 'phobiaIA', 'rhabdopHOBIA']))
print(is_contains('auto', ['automotive', 'autistic']))
print(calls)
print('------------------------------------------------------------------------------------------------')
