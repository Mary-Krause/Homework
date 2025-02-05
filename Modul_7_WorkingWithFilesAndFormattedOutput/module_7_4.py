# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %-форматирования
# 1. Количество участников первой команды
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

# 2. Количество участников в обеих командах
teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

# Использование format()
# 3. Количество задач, решённых командой 2
score2_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score2_str)

# 4. Время, за которое команда 2 решила задачи
time2_str = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(time2_str)

# Использование f-строк
# 5. Количество решённых задач по командам
scores_str = f"Команды решили {score_1} и {score_2} задач."
print(scores_str)

# 6. Исход соревнования
result_str = f"Результат битвы: {challenge_result}"
print(result_str)

# 7. Количество задач и среднее время решения
tasks_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(tasks_str)