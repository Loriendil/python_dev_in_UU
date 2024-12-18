# Домашнее задание по теме "Списковые, словарные сборки"

first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(item) for item in first_string if len(item) >= 5]
second_result = [(f_item, s_item) for f_item in first_string for s_item in second_string if len(f_item) == len(s_item)]
# Тут в одну строку не получится, поэтому сделаем в 2 шага.
# Сначала создадим объединённый список, а затем сделаем выборку и создадим словарь.
merged_list = [item for sublist in [first_string, second_string] for item in sublist]
third_result = {item: len(item) for item in merged_list if len(item) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)