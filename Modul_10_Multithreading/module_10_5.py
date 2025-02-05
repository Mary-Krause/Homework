import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


def linear_execution(filenames):
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f'Линейное выполнение: {end_time - start_time:.6f} сек')


def multiprocessing_execution(filenames):
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'Многопроцессное выполнение: {end_time - start_time:.6f} сек')


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейное выполнение
    linear_execution(filenames)

    # Многопроцессное выполнение
    multiprocessing_execution(filenames)
