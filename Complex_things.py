# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def  personal_sum(numbers:list | set | tuple | dict)->tuple:
    result = 0
    incorrect_data = 0
    # поскольку у нас в задании не сказано конкретно какая разновидность коллекции, будет проверять всё на свете
    # список, множество и кортеж в одну сторону, словарь отдельно
    if type(numbers) is not dict:
        for item in numbers:
            try:
                result += item
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы: {item}")  # строка не по заданию, но
                                                                              # она как раз реализует поведение
                                                                              # из примера вывода в консоль
                incorrect_data += 1
    else:
        # try - except как и try-catch-finally это цикл наоборот, если можно так выразится,
        # поэтому в блоке else нам нужен костыль с проверкой типа данных, иначе суммируем по второму кругу
        for key, value in numbers.items():
        # Этот код я оставил здесь для того, чтобы показать как это работает на самом деле, потому что ОЧЕНЬ не очевидно.
            # try:
            #     result += key
            #     try:
            #         result += value
            #         try:
            #             result = result + key + value
            #         except TypeError:
            #             print(f"Некорректный тип данных для подсчёта суммы: {key}, {value}")
            #             incorrect_data += 1
            #     except TypeError:
            #         print(f"Некорректный тип данных для подсчёта суммы: {value}")
            #         result += key
            #         incorrect_data += 1
            # except TypeError:
            #     print(f"Некорректный тип данных для подсчёта суммы: {key}")
            #     result += value
            #     incorrect_data += 1
            # else:
            #     if isinstance(key,int | float) and isinstance(value,int | float):
            #         continue
            #
            # Поскольку вложенные try-except, как try-catch-catch(...), try-catch-finally в том, виде
            # как это представлено в закомментированном виде ересь, напишем в правильном ключе.
            # Логика такая: проверил, проверь следующее.
            # Для правильного результата ПРЕДНАЗНАЧЕН блок else, поэтому не надо ломать язык.
            # Нужно на нём говорить правильно. Прям как с "словить" из лекции.
            # Может быть это удобно с какой-то точки зрения, но это ломает красоту и логику родного языка.
            try:
                result += key
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы: {key}")
                result += value
                incorrect_data += 1
            else:
                try:
                    result += value
                except TypeError:
                    print(f"Некорректный тип данных для подсчёта суммы: {value}")
                    result += key
                    incorrect_data += 1
                else:
                    result = result + key + value

    return tuple([result, incorrect_data]) # можно вернуть через запятую, но так я подчёркиваю что это именно кортеж.


def calculate_average(numbers:list | set | tuple | dict)-> float | None:
    res:int
    incor_data:int
    average:float
    if type(numbers) is not dict:
        try:
            res, incor_data = personal_sum(numbers)
            if incor_data == 0:
                average = res / len(numbers)
            else:
                average = res / (len(numbers) - incor_data)

        except ZeroDivisionError:
            return 0
        except TypeError:
            print(f"В numbers записан некорректный тип данных")
            return None
        else:
            return average
    else:
        try:
            res, incor_data = personal_sum(numbers)
            count = len(numbers) * 2 # метод len() не даёт количество членов словаря.
            # Поскольку у нас строка в словаре может состоять исключительно из двух элементов,
            # поэтому тут магия чисел. Мерзость, но что поделать.
            if incor_data == 0:
                average = res / count
            else:
                average = res / (count - incor_data)
        except ZeroDivisionError:
            return 0
        except TypeError:
            print(f"В numbers записан некорректный тип данных")
            return None
        else:
            return average

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

print("-----------------Моя проверка-----------------")
print(f"Результат 5: {calculate_average({'ключ 1': 1, 'ключ 2': 2})}") # сумма 3, среднее 1.5
print(f"Результат 6: {calculate_average({4: 1, 3: 2})}") # сумма 10, среднее 5
print(f"Результат 7: {calculate_average({'ключ 5': 'значение -1', 'ключ 6': 'значение -2'})}") # None