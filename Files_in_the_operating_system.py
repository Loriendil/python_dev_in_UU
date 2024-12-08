# Домашнее задание по теме "Файлы в операционной системе"
import os
import time

# создаю переменную directory, в которой будет путь до каталога
directory = r'E:\local_repository\Python-repository\Homework\Module_7'
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory

for root, dirs, files in os.walk(directory):
  for file in files:
    # Примените os.path.join для формирования полного пути к файлам.
    filepath = os.path.join(directory, file)
    # Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    # Используйте os.path.getsize для получения размера файла.
    filesize =  os.path.getsize(file)
    # Используйте os.path.dirname для получения родительской директории файла.
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')