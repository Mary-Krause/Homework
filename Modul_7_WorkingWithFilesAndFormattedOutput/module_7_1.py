class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        # Создаём файл, если он не существует
        open(self.__file_name, 'a').close()

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read().strip()

    def add(self, *products):
        current_products = self.get_products().split('\n') if self.get_products() else []
        product_dict = {}

        # Заполняем словарь текущими продуктами
        for line in current_products:
            name, weight, category = line.split(', ')
            product_dict[(name, category)] = float(weight)

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                key = (product.name, product.category)
                if key in product_dict:
                    product_dict[key] += product.weight
                    print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_dict[key]}')
                else:
                    product_dict[key] = product.weight
                    file.write(str(product) + '\n')

        # Перезаписываем файл с актуальными данными
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for (name, category), weight in product_dict.items():
                file.write(f"{name}, {weight}, {category}\n")


# Пример работы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())

# Этот код реализует классы Product и Shop с соответствующими методами. Продукты добавляются в файл только если они отсутствуют, а если уже есть, то вес обновляется. При вызове get_products() возвращается содержимое файла.
