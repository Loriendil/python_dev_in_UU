# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# список оценок
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# множество учеников
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#создаём пустой словарь
journal = dict()
#преобразуем множество в список
my_list= list(students)
#сортируем список
sorted_list = sorted(my_list)
#добавляем в словарь пару ключ и значение, одновременно вычисляя среднее значение из чисел в каждом
#из элементов списка оценок
journal[sorted_list[0]]=sum(grades[0])/len(grades[0])
journal[sorted_list[1]]=sum(grades[1])/len(grades[1])
journal[sorted_list[2]]=sum(grades[2])/len(grades[2])
journal[sorted_list[3]]=sum(grades[3])/len(grades[3])
journal[sorted_list[4]]=sum(grades[4])/len(grades[4])
#выводим результат
print(journal)