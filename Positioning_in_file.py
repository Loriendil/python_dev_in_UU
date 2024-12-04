# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name:str, strings:list[str])->dict[tuple[int, int], str]:
# Словарь содержит кортеж в качестве ключа, и строку в качестве значения.
# Кортеж представляет собой <номер строки>, <байт начала строки>.
    res = dict()
    line_number:int = 0 # Номер строки в файле. Поскольку я вывожу по строчно из списка входящих значений.
# Простой счёт будет вполне отражать действительность.
# Для чтения и записи использую кодировку utf-8.
    with open(file_name, 'a+', encoding='utf-8') as file:
        for string in strings:
            line = string + '\n'
# Для получения номера байта начала строки использую метод tell() перед записью.
            start_byte = file.tell()
            file.write(line)
            line_number += 1
            res[(line_number, start_byte)] = string
    return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
