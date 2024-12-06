# Домашнее задание по теме "Оператор "with"

class WordsFinder:
    def __init__(self, *file_names: str) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict[str, list[str]]:
# Создаю пустой словарь all_words
        all_words = dict()
        restricted_symbols = [',', '.', '=', '!', '?', ';', ':', '-']
# Перебираю названия файлов и открывайте каждый из них, используя оператор with
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                buffer_4_chars = []
                for line in lines:
# Для каждого файла считываю единые строки, переводя их в нижний регистр (метод lower()).
                    line:str = line.lower()
                    for char in line:
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', '-'] в строке.
# (тире обособлено пробелами, это не дефис в слове).
                        if char not in restricted_symbols:
                            buffer_4_chars.append(char)
# Метод join() обратный методы split()
                    cleaned_line:list[str] = ''.join(
                        buffer_4_chars).split()
# без разделяющего символа .split() делить по пробелам!
# удобно! См. тех. документацию на язык!
# Цитирую: "f sep is not specified or is None, a different splitting algorithm is applied:
# runs of consecutive whitespace are regarded as a single separator, and the result will
# contain no empty strings at the start or end if the string has leading or trailing whitespace."
# Ссылка: https://docs.python.org/3/library/stdtypes.html#str.split
# внимательность МОЙ конёк, да! В задании.
 # Цитата: "Разбейте эту строку на элементы списка методом split().
 # (разбивается по умолчанию по пробелу)"
                    all_words[file_name] = cleaned_line
                # альтернативно del buffer[:] (везде), buffer.clear() (Python 3 и выше)
                # ещё можно написать while buffer: buffer.pop()
                # ссылка: https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
        return all_words

    def find(self, word: str) -> dict[str, int]:
        w:str = word.lower()
        for name, words in self.get_all_words().items():
            for wo in words:
                if w == wo:
                    return {name: words.index(w)+1}
# Учусь задавать вопросы.
# https://www.pythontutorial.net/python-basics/python-find-index-of-element-in-list/
# Возвращаю анонимный словарь, где ключ - название файла,
# значение - позиция первого такого слова в списке слов этого файла
        return {'Error: find()': 404}

    def count(self, word: str) -> dict[str, int]:
        w: str = word.lower()
        count:int = 0
        file_name:str = ''
        for name, words in self.get_all_words().items():
            for wo in words:
                if w == wo:
                    file_name = name
                    count += 1
        if count > 0:
# Возвращаю словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
            return {file_name: count}
        elif count == 0:
            return {'Nothing found by count()': 0}
        else:
            return {'Error in count()': 404}

wf = WordsFinder('text1.txt', 'text2.txt','text3.txt')
print(wf.get_all_words())

print('Mother Goose - Monday’s Child')
print(wf.find('Child'))
print(wf.count('Child'))

print("Rudyard Kipling - If")
print(wf.find('if'))
print(wf.count('if'))

print("Walt Whitman - O Captain! My Captain!")
print(wf.find('Captain'))
print(wf.count('Captain'))