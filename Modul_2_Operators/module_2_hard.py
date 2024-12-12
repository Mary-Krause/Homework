import random

n = random.randint(3, 20)  # Генерируем случайное число, а точнее первую вставку ключа
list = []  # Создаем пустой список, нам он понадобится для формирования набора возможных чисел
result = ''  # переменная (именно строкового типа), чтобы записывать туда постепенно итоговую вторую вставку
print(n)  # Для наглядности выводим нашу первую вставку, чтобы убедиться, что мы не дурачки и код правильно нам подбирает ключ
for i in range(1, 20):  # Цикл для перебора и поиска подходящих значений, как показало наблюдение, каждое из двух числе должно быть меньше первой вставке
    if i < n:  # Собственно само условие
        list.append(i)  # Если подходит, то записываем в наш список
print(list)  #Выводим итоговый сформировавшийся список, дабы убедиться, что там действительно все значения меньше первой вставки
for index in list:  # А теперь самое интересное, в данном цикле мы будем собирать из ранее полученных чисел пары
    t = index + 1  # Подбор пар должен начинаться со следующего элемента
    for t in list[index:]:  # Создаем цикл внутри цикла, чтобы подобрать пары, при этом начинаем перебирать мы со следующего элемента
        if n % (index + t) == 0:  # Проверка на вшивость, а именно, чтобы делилось без остатка
            result += str(index) + str(t)  # И если да, то записываем два элемента друг за другом в нашу итоговую переменну
        else:
            t += 1  # А если пара не проходит испытание, то переходим к следующей жертве
print(result)  # И выводим наш долгожданный результат...
#Спасибо, что дочитали до конца :)