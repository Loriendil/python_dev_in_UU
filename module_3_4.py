# Самостоятельная работа по уроку "Произвольное число параметров"
# Создаю функцию, которая находит слово в списке слов

# Создаю функцию, которая использует как сказано в примечании ключевое слово in
def single_root_words_in(root_word, *other_words):
# Создаю внутри функции пустой список same_words. Туда будем класть подходящие слова
    same_words = []
# При помощи цикла for пробегаю по кортежу слов, получаемых из other_words
    for item in other_words:
# левая часть выражения ИЛИ проверяет входит ли искомое слово в рассматриваемое, а правая - наоборот
        if root_word.lower() in item.lower() or item.lower() in root_word.lower():
# добавляем в список
            same_words.append(item)
    return same_words

# Создаю функцию, которая использует как сказано в примечании ключевое слово in
def single_root_words_count(root_word, *other_words):
 # Создаю внутри функции пустой список same_words. Туда будем класть подходящие слова
    same_words = []
 # я не стал устраивать цепочку вызовов через оператор ".", поэтому решил выполнить отдельно преобразование
    root_word = root_word.upper()
 # При помощи цикла for пробегаю по кортежу слов, получаемых из other_words
    for item in other_words:
# item каждый раз новое слово, поэтому приводим к виду в теле цикла
        s = item.upper()
# Левая часть выражения ИЛИ определяет количество символов в рассматриваемом слове искомого, а
# правая часть выражения определяет количество символов в искомом слове рассматриваемого.
# Условие if выполняется когда количество символов одного слова больше нуля в другом.
        if s.count(root_word) > 0 or root_word.count(s) > 0:
            same_words.append(item)
 # добавляем в список
    return same_words

# этот текст из примера результата выполнения программы
print('---------------------------------------------IN---------------------------------------------------')
result1 = single_root_words_in('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_in('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
print('---------------------------------------------COUNT------------------------------------------------')
result3 = single_root_words_count('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result4 = single_root_words_count('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result3)
print(result4)