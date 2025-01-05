# Домашнее задание по теме "Многопроцессное программирование"
import time
from multiprocessing import Pool

def read_info(name:str)->None:
    all_data:str = ""
    with open(name, "r", encoding='utf-8') as fl:
        fl.seek(0)
        while True:
            line = fl.readline()
            if not line:
                break
            else:
                all_data += line
    return None

if __name__ == '__main__':
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    ex_mode = int(input("Выберете режим работы программы:"
            " (1) для запуска в однопроцессорном режиме, (4) для запуска в многопроцессорном режиме: \n"))

    match ex_mode:
        case 1:
            start_time_sp = time.time()
            for file in files:
                read_info(file)
            end_time_sp = time.time()

            print(f"Время линейного выполнения задачи: {end_time_sp - start_time_sp:.8f} секунд")
        case 4:
            start_time_mp = time.time()
            with Pool(processes=len(files)) as pool:
                results = pool.map(read_info, files)
            end_time_mp = time.time()

            print(f"Время многопроцессорного выполнения задачи: {end_time_mp - start_time_mp:.8f} секунд")
        case _:
            print("Error input!")