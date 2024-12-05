# Домашнее задание по теме "Оператор "with"

class WordsFinder:
    def __init__(self, *files:str) -> None:
        self.file_names = files

    def get_all_words(self) -> dict[str, list[str]]:
        all_words = dict()
        restricted_symbols = [',', '.', '=', '!', '?', ';', ':', '-']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                buffer = []
                for line in lines:
                    line = line.strip().lower()
                    for char in line:
                            if char not in restricted_symbols:
                                buffer.append(char)
                    cleaned_line = ''.join(buffer).split() # без разделяющего символа .split() делить по пробелам!
                    # удобно! См. тех. документацию на язык!
                    # Цитирую: "f sep is not specified or is None, a different splitting algorithm is applied:
                    # runs of consecutive whitespace are regarded as a single separator, and the result will
                    # contain no empty strings at the start or end if the string has leading or trailing whitespace."
                    # Ссылка: https://docs.python.org/3/library/stdtypes.html#str.split
                    # внимательность МОЙ конёк, да! В задании.
                    # Цитата: "Разбейте эту строку на элементы списка методом split().
                    # (разбивается по умолчанию по пробелу)"
                    all_words[file_name] = cleaned_line
                    del buffer[:]
                # альтернативно del buffer[:] (везде), buffer.clear() (Python 3 и выше)
                # ещё можно написать while buffer: buffer.pop()
                # ссылка: https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/
        return all_words


    def find(self, word: str) -> dict[str, int]:
        word = word.lower()
        count = 1
        for name, words in self.get_all_words().items():
            for item in words:
                if word == item:
                    return {name: count}
                count += 1
        return {}

    def count(self, word: str) -> dict[str, int]:
        word = word.lower()
        count = 0
        for name, words in self.get_all_words().items():
            for item in words:
                if word == item:
                    count += 1
        return {name: count}

wf = WordsFinder('text1.txt', 'text2.txt')
print(wf.get_all_words()) # Все слова
print(wf.find('REMEMBER')) # 2 слово по счёту
print(wf.count('Aurora')) # 1 слово Aurora в тексте всего