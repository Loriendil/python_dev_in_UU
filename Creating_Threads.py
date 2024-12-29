# Домашнее задание по теме "Создание потоков"
import threading
import time

def write_words(words_count:int, file_name:str)->None:
    word = "Какое-то слово"
    with open(file_name, "w", encoding="utf-8") as file_name:
        for item in range(words_count):
            string:str = f"{word} № {item}\n"
            file_name.write(string)
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

# 4 вызова функции write_words()
start_time_0 = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time_0 = time.time()
print(f"Работа потоков {end_time_0 - start_time_0}")
# 4 потока для вызова функции write_words()
thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

# запускаем каждый поток последовательно и замеряем время
start_time_1 = time.time()
thread1.start()
thread1.join()

thread2.start()
thread2.join()

thread3.start()
thread3.join()

thread4.start()
thread4.join()
end_time_1 = time.time()
print(f"Работа потоков {end_time_1 - start_time_1}")