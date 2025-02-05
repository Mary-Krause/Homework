# 1. Lambda-функция
# Создадим lambda-функцию для сравнения символов двух строк на одинаковых позициях.
# Исходные строки
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов
result = list(map(lambda x, y: x == y, first, second))

# Вывод результата
print(result)


# 2. Замыкание
# Реализуем функцию get_advanced_writer, которая возвращает функцию write_everything для записи данных в файл.
def get_advanced_writer(file_name):
    # Внутренняя функция для записи данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')  # Записываем данные в файл

    # Возвращаем функцию write_everything
    return write_everything


# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3. Класс с методом __call__
# Создадим класс MysticBall, который случайным образом выбирает слово из коллекции.
from random import choice


class MysticBall:
    def __init__(self, *words):
        # Инициализируем коллекцию слов
        self.words = words

    def __call__(self):
        # Случайным образом выбираем слово из коллекции
        return choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


