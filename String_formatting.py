# Домашнее задание по теме "Форматирование строк"

# Использование %
team1_num:int = 5
print("В команде Мастера кода участников: %s!" % team1_num)
team2_num:int = 6
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num': team1_num, 'team2_num':team2_num})
# Использование format()
score_2:int = 42
print("Команда Волшебники данных решила задач: {0}!".format(score_2))
team1_time:float = 18015.2
print("Волшебники данных решили задачи за {time}!".format(time = team1_time))
# Использование f-строк
score_1:int = 40
print(f"Команды решили {score_1} и {score_2} задача.")
team2_time:float = 15000.7
if score_1 > score_2 or score_1 == score_2  and team1_time > team2_time:
    challenge_result = "победа команды Мастера кода"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "победа команды Волшебники данных"
else:
    challenge_result = "Ничья!"
print(f"Результат битвы: {challenge_result}!")
time_avg:float = (team1_time + team2_time)/2
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!")