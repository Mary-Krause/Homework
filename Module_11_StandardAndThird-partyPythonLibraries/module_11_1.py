import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# 1. requests - Получение данных с сайта
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print("Полученные данные:", response.json())
else:
    print("Ошибка запроса")

# 2. pandas - Чтение CSV-файла и анализ данных
csv_data = "data.csv"  # Укажите путь к CSV-файлу
try:
    df = pd.read_csv(csv_data)
    print("\nПервые 5 строк таблицы:")
    print(df.head())
    print("\nОписание данных:")
    print(df.describe())
except FileNotFoundError:
    print("Файл CSV не найден!")

# 3. numpy - Создание массива и математические операции
arr = np.array([1, 2, 3, 4, 5])
print("\nИсходный массив:", arr)
print("Массив после умножения на 2:", arr * 2)
print("Среднее значение массива:", np.mean(arr))
print("Стандартное отклонение массива:", np.std(arr))

# 4. matplotlib - Визуализация данных
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции sin(x)")
plt.legend()
plt.show()

# 5. pillow - Обработка изображения
try:
    img = Image.open("input.jpg")
    img_resized = img.resize((200, 200))
    img_filtered = img.filter(ImageFilter.CONTOUR)
    img_resized.save("resized_output.png")
    img_filtered.save("filtered_output.png")
    print("Изображения обработаны и сохранены!")
except FileNotFoundError:
    print("Файл изображения не найден!")


# Этот код демонстрирует работу с каждой библиотекой:
#
# requests – получение данных из API.
# pandas – загрузка данных из CSV и анализ.
# numpy – создание массива и выполнение математических операций.
# matplotlib – построение графика.
# Pillow – обработка изображения.