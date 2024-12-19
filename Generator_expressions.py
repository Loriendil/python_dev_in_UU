# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f_item)-len(s_item) for f_item, s_item in zip(first, second) if len(f_item) != len(s_item))
second_result = (len(first[index]) == len(second[index]) for index in range(len(first)))
print(list(first_result))
print(list(second_result))