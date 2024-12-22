# Домашнее задание по теме "Создание функций на лету"
# Задача "Функциональное разнообразие"

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result1 = list(map(lambda x, y: x == y, first, second))
print(result1)

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            for data in data_set:
                if isinstance(data, str):
                    file.write(data + '\n')
                else:
                    file.writelines(str(item) for item in data)
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        random_element = choice(self.words)
        return random_element


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
