# Домашнее задание по теме "Генераторы"

def  all_variants(text):
    length = len(text)
    # внешний цикл пробегает по всем комбинациям букв
    for i in range(1 << length):
        # в цикле пробегаем по всей длине строки и выбираем, только те комбинации которые есть в строке
        yield ''.join(text[j] for j in range(length) if (i & (1 << j)))

a = all_variants("abc")

for i in a:
    print(i)