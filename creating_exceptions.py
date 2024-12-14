# Домашнее задание по теме "Создание исключений"

# Создаю 3 класса (2 из которых классы-исключения)
class Car:
    """
    Ключевые аргументы:
    model - название автомобиля (строка)
    __vin - vin номер автомобиля (целое число)
    __numbers - номера автомобиля (строка)
    Методы:
    __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    Возвращает True, если корректный, в других случаях выбрасывает исключение

    __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
     Возвращает True, если корректный, в других случаях выбрасывает исключение.
    """
    def __init__(self, model: str, __vin: int, __numbers: str) -> None:
        self.model = model
        self.__numbers = __numbers

        if self.__is_valid_vin(__vin):
            self.__vin = __vin

        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers

    def __is_valid_vin(self, vin_number: int) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")

        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True


    def __is_valid_numbers(self, numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")

        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

        return True

# Классы-исключения
class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message

# Код из задачи, для проверки усвоения материала лекции "Создание исключений"

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

