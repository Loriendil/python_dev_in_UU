# Домашнее задание по теме "Обзор сторонних библиотек Python"

import requests # для запроса данных с веб-сайта:
import json # для записи полученных данных с веб-сайта
import os # для загрузки файла с жёсткого диска
import numpy as np # для расчёта среднесуточного,
                   # стандартного отклонения показателей температуры, влажности и скорости ветра,
                   # а также установить зависимость облачности и термодинамических показателей погоды
import matplotlib.pyplot as plt # для визуализации данных

ACCESS_TOKEN = "W2VMKBK8633ZXFZC56D8PDH7H"

def fetch_url(_country, _location, st_date, ed_date):
    return (f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{_location}"
        f"%2C{_country}/{st_date}/{ed_date}?unitGroup=metric&include=days%2Chours&key={ACCESS_TOKEN}&contentType=json")

def connect_to_site(base_url):
    with requests.Session() as s:
        # Отправляем GET запрос к созданному URL
        res = s.get(base_url)
        # Проверяем если запрос удачный или нет
        if res.status_code == 200:
            print('Соединение установлено успешно')
            write_json_on_ssd(res.json())
        else:
            print(f'Код ошибки: {res.status_code}, Описание ошибки: {res.text}')

def write_json_on_ssd(data):
    with open("climate_data(MS,RS).json", "w", encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def read_json_from_ssd(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

if __name__ == '__main__':
    # исходя из документации на сайте https://www.visualcrossing.com/weather/weather-data-services#
    # составим URl для получения ответа от сервера в виде json об изменении климатических данных за заданный период
    location = "Moscow"
    country = "Russia"
    start_date = "2010-08-01"
    end_date = "2010-08-31"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    current_directory += '\\climate_data(MS,RS).json'
    address = (fetch_url(country, location, start_date, end_date))
    connect_to_site(address)
    dt = read_json_from_ssd(current_directory)
    tempmax = list() # максимальная температура
    tempmin = list() # минимальная температура
    day_num = list() # список дней

    lst_days = dt.get('days')
    for lst_day in lst_days:
        tempmax.append(lst_day.get('tempmax'))
        tempmin.append(lst_day.get('tempmin'))
        day_num.append(lst_day.get('datetime'))

    # извлекаем данные в список, для последующего нахождения среднего арифметического и стандартного отклонения
    max_temperatures = np.array(tempmax)
    min_temperatures = np.array(tempmin)
    # поскольку matplotlib.pyplot использует для построения графиков типы данных NumPy,
    # то заблаговременно подготовим даты в этом формате
    dates = np.array([np.datetime64(day) for day in day_num])

    # вычисление среднего арифметического
    mean_tempmax = np.mean(max_temperatures)
    mean_tempmin = np.mean(min_temperatures)
    print(f'Среднее значение минимальной температуры за наблюдаемый период: {mean_tempmin:.2f}')
    print(f'Среднее значение максимальной температуры за наблюдаемый период: {mean_tempmax:.2f}')

    # вычисление стандартного отклонения
    std_dev_tempmax = np.std(max_temperatures)
    std_dev_tempmin = np.std(min_temperatures)

    print(f'Значение стандартного отклонения минимальной температуры за наблюдаемый период: {std_dev_tempmin:.2f}')
    print(f'Значение стандартного отклонения максимальной температуры за наблюдаемый период: {std_dev_tempmax:.2f}')

    # Собираем и готовим данные
    plt.figure(figsize=(10, 5))
    plt.plot(dates, max_temperatures, label='Макс. температура', color='red', marker='o')
    plt.plot(dates, min_temperatures, label='Мин. температура', color='blue', marker='o')
    plt.fill_between(dates, max_temperatures, min_temperatures, color='lightgray', alpha=0.5)

    # Добавляем заголовки и подписи
    plt.title('Максимальная и Минимальные температуры отнесённые к датам')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Показываем наш график
    plt.show()