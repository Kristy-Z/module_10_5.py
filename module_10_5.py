import time
from multiprocessing import Pool


def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        line = file.readline().strip()

        while line:
            all_data.append(line)
            line = file.readline().strip()

    return all_data


if __name__ == "__main__":
    filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # # Линейный вызов
    # print("Линейный вызов:")
    # start_time = time.time()
    #
    # for name in filenames:
    #     data = read_info(name)
    #
    # end_time = time.time()
    # line_time = end_time - start_time
    # print(f"Время выполнения: {line_time:.6f}\n")

    # Многопроцессорный вызов
    print("Многопроцессорный вызов:")
    start_time = time.time()

    with Pool() as pool:
        results = pool.map(read_info, filenames)

    end_time = time.time()
    multiprocessing_time = end_time - start_time
    print(f"Время выполнения: {multiprocessing_time:.6f}")
