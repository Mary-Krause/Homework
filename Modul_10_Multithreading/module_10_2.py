import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов
    lock = threading.Lock()  # Блокировка для синхронизации потоков

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while True:
            with Knight.lock:
                if Knight.total_enemies <= 0:
                    break
                Knight.total_enemies -= self.power
                if Knight.total_enemies < 0:
                    Knight.total_enemies = 0

            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {Knight.total_enemies} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
