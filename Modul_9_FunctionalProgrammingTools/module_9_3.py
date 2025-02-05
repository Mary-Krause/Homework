# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая генераторная сборка: разница длин строк, если длины не равны
first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))

# Вторая генераторная сборка: сравнение длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))