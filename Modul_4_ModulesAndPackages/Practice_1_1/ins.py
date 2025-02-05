from os.path import split
from sort.SortFunc import *

data_1 = list(map(int, input('Введите числа через пробел').split()))  # 1 2 3 4 5
data_2 = list(map(int, input('Введите числа через пробел').split()))  # 1 2 3 4 5
data_3 = list(map(int, input('Введите числа через пробел').split()))  # 1 2 3 4 5

print(data_1)
print(data_2)
print(data_3)

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print('Пузырьковая сортировка: ', data_1)
print('Сортировка выбором: ', data_2)
print('Сортировка вставкой: ', data_3)
