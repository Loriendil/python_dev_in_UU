# Домашнее задание по теме "Режимы открытия файлов"

class Product:
    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
# Сделаем название файла максимально сокрытым и максимально приватным.
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self)->list[str]:
        products = []
        with open(self.__file_name, 'r') as file:
            arrows = file.readlines()
            if len(arrows) == 0:
                return []
            else:
                for arrow in arrows:
                    name, weight, category = arrow.strip().split(',')
                    record = f'{name.strip()},{float(weight.strip())},{category.strip()}'
                    products.append(record)
                    products.append('\n')
            return products

    def add(self, *products: Product) -> None:
        # В этом руководстве: https://realpython.com/read-write-files-python/
        # так же в этом: https://pythonist.ru/chtenie-i-zapis-fajlov-s-pomoshhyu-python/
        # советуют открывать файл не так, как дано в лекции и мне как-то этот подход ближе.
        # Если у нас файл не пустой, то безопаснее всего его открывать на дополнение данных,
        # без обрезания данных. По этой причине, лучший режим это "а+" и только он.
        with open(self.__file_name, 'a+') as file:
            file.seek(0)  # устанавливаем курсор в начало файла
            existing_products = file.readlines()  # собираем все ранее внесённые товары в переменную
            for existing_product in existing_products:
                # Если есть уже строка, то она будет вида {product.name}, {product.weight}, {product.category},
                # поэтому нужно по запятой разделить строку на подстроки.
                # Деление на подстроки с помощью метода split(''). Метод split() возвращает список строк, а
                # не строку и также я знаю, что в моих записях в файл продукт всегда на первом месте, поэтому
                # я смело могу прописать нулевой индекс списка. Методом strip() я очищаю от пробелов.
                existing_product.split(',')[0].strip()

            for product in products:
                record = f'{product.name}, {product.weight}, {product.category}\n'
                if record in existing_products:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(record)

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(*s1.get_products()) # Для того чтобы соблюсти вид вывода в терминал как на снимке экрана к заданию,
                       # необходимо тут изменить код, который по идее не должен меняться, так как это тестовый код,
                       # но либо снимок экрана не корректный, либо код вывода с аналогом yield return из C#
