# Домашнее задание по теме "Асинхронность на практике"
import asyncio


async def start_strongman(name:str, power:int)->None:
    """
    Функция симулирует поднятие силачом шаров
    :param name: имя силач, str
    :param power: подъёмная мощность, int
    :return: None
    """
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар № {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Вика', 15))
    task2 = asyncio.create_task(start_strongman('Маша', 12))
    task3 = asyncio.create_task(start_strongman('Даша', 13))
    await task1
    await task2
    await task3

async def main():
    await start_tournament()

asyncio.run(main())