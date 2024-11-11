# Домашняя работа по уроку "Пространство имен."
# Создаю новую функцию test_function
def test_function():
# Создаю внутри test_function другую функцию - inner_function,
    def inner_function():
        print("Я в области видимости функции test_function")
# Вызываю функцию inner_function внутри функции test_function
    inner_function()

# inner_function() - вызов ошибки NameError:
# name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()