# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи"
# Для вычисления площади треугольника по формуле Герона подключаем библиотеку math,
# а также для использования константы Пи
import math

class Figure:
    # В задаче сказано, что атрибут класса Figure должен быть задан в
    # переменной sides_count, но в предыдущем уроке мы константы,
    # записывали заглавными буквами и при необходимости переопределяли
    # в классах наследниках.
    # В целях соблюдения единообразия написания программных текстов
    # я буду писать атрибуты класса в этой программе также заглавными буквами.
    SIDES_COUNT = 0
    # Ввод у меня кортежами, вывод у меня списками.  Это плохо, но такое задание. Переменная filled
    # по тексту нам не требуется, поэтому я задам ей значение по умолчанию, чтобы они не мешала работе программы.
    # Насколько я помню школьную программу по математике, то две стороны в сумме должны быть больше третьей,
    # поэтому треугольник со сторонами 1, 1, 1 просто не существует.
    def __init__(self, __sides: int, __color: tuple[int, int, int], filled = True) -> None:
        self.__sides = __sides
        self.__color = list(__color)
        self.filled = filled

    def get_color(self) -> list[int]:
        return self.__color

    # PyCharm предлагает использовать декораторы для указания о статическом методе, но
    # мы декораторы не проходили ещё, поэтому оставим это как есть
    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
            return (-1 < r < 256) and (-1 < g < 256) and (-1 < b < 256)

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # PyCharm предлагает использовать декораторы для указания о статическом методе, но
    # мы декораторы не проходили ещё, поэтому оставим это как есть
    def __is_valid_sides(self, *arges) -> bool:
        count = 0
        for item in arges:
            if item < 0:
                return False
            else:
                count += 1
        if count == len(arges):
            return True
        else:
            return False


    def get_sides(self) -> list[int]:
        result = []
        for item in range(0, self.SIDES_COUNT, 1):
            result.append(self.__sides)
        return result

    def __len__(self) -> int:
        result = 0
        for item in range(0, self.SIDES_COUNT, 1):
            result += self.__sides
        return result

    def set_sides(self, *new_sides) -> None:
        upgraded_sides = list(new_sides)
        if self.SIDES_COUNT == len(upgraded_sides):
            if self.__is_valid_sides(*upgraded_sides):
                self.__sides = upgraded_sides[0]

class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, color: tuple[int, int, int], __radius: int):
        super().__init__(__radius, color)

    def get_square(self):
        return math.pi * self.get_sides()[0] ** 2

class Triangle(Figure):
    def get_square(self):
        p = 0.5 * sum(self.get_sides())
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

# Пример 3: Cube((200, 200, 100), 9), так как сторон (рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), так как сторон (рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
# Эти вызовы функций совершенно не понятны, от того что мы явно указали кол-во сторон куба,
# почему стало вдруг игнорироваться длина стороны куба.
# Я написал максимально согласующуюся со всеми указаниями в задании реализацию.
class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, __color: tuple[int, int, int], __sides:int):
        super().__init__(__sides, __color)

    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
    #Код для проверки:
    print("Код для проверки")
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    print("Проверка на изменение цветов")
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    print("Проверка на изменение сторон")
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())

    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print("Проверка периметра (круга), это и есть длина:")
    print(len(circle1))

    # Проверка объёма (куба):
    print("Проверка объёма (куба):")
    print(cube1.get_volume())
