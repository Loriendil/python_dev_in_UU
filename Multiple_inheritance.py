# Домашнее задание по теме "Множественное наследование"
import random
# Описанную заданную структуру класса Animal согласно ТЗ
class Animal:
    _DEGREE_OF_DANGER = 0
# подсмотрел классную фишку на других ресурсах ставить подсказки о типе данных для переменных и методов
    def __init__(self, speed: int, live=True, sound=None, _cords=None) -> None:
        if _cords is None:
            _cords = [0, 0, 0]
        self._cords = _cords
        self.live = live
        self.sound = sound
        self.speed = speed

    def move(self, dx:int, dy:int, dz:int) -> None:
        list_buffer = [dx, dy, dz]
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return

        for i in range(len(self._cords)):
            self._cords[i] = list_buffer[i] * self.speed

    def get_cords(self) -> None:
        # Ещё одна прикольная фишечка из мануалов. Распаковка кортежа с множественным присвоением.
        # Мелочь, а приятно.
        # Оставлю на себе: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        x, y, z = self._cords
        print(f'X: {x}, Y: {y}, Z: {z}')

    def attack(self) -> None:
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self) -> None:
        print(f'{self.sound}')

class Bird(Animal):
# В лекции это как-то я не подхватил, но методом тыка осознал, что раньше делал больше по инерции потому, что
# так написано в умных книжках. Все мной желаемые атрибуты класса делятся на два типа.
# Первый тип это те которые лежат в коробке с табличкой родительный класс и
# за ним нужно сходить нашей здоворенной белке, она же интерпретатор.
# Второй тип это те, которые лежат прямо тут - в коробке с надписью этой (дочерний) класс. Белке не нужно никуда бегать.
# Так вот.
# Где искать первый тип я подсказываю белке на её языке - super().__init__(speed),
# а где второй с помощью self.beak = beak.
# В классе Duckbill то же самое.
    def __init__(self, speed: int, beak=True) -> None:
        super().__init__(speed)
        self.beak = beak

    def lay_eggs(self) -> None:
# Не помню в какой конкретно лекции говорилось, что допускается импорт сторонних ресурсов в точке,
# но лучше так не делать, по моему скромному мнению.
        rnd = random.randint(1, 4)
        print(f"Here are(is) {rnd} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
# Самый сложный метод для меня. История почему это правильный код. Читать в условиях невнимательности нужно по слогам.
# Итак. Первое предложение: "Этот метод должен всегда уменьшать координату z в _coords".
# Координата Z должна вычитать сама из себя значение, тогда мы будем двигаться вниз.
# Второе предложение: "Чтобы сделать dz положительным, берите его значение по модулю (функция abs)".
# Глубину могут задать заведомо как положительное значение (глубина это всё ещё длина отрезка), и как
# отрицательное значение (глубина это же ещё относительная высотная отметка может быть по отношению к уровню моря).
# Для исключения зависимости от ввода пользователя принудительно использую метод abs()
# и тогда у меня dz будет предсказуемой. Это хорошо. Предсказуемое поведение это цель. Это благо.
# Третье предложение: "Скорость движения при нырянии должна уменьшаться в 2 раза,
# в отличие от обычного движения. (speed / 2)". Тут всё просто.
# Кроме того, что нам не нужны лишнее превращение из int во float, поэтому использую целочисленное деление.
    def dive_in(self, dz) -> None:
        self._cords[2] -= abs(dz) * (self.speed // 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed: int, sound="Click-click-click") -> None:
        super().__init__(speed)
        self.sound = sound
# отладочный вызов для сопоставления выдачи в теле задачи и иерархии наследование между классами
# print(Duckbill.mro())

# Вызовы из ТЗ:
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
