from typing import Optional, List, Dict, Union


class Product:
    """
    Класс для описания товара
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price  # Приватный атрибут цены
        self.quantity: int = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой на положительное значение"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]]) -> "Product":
        """
        Класс-метод для создания продукта из словаря
        """
        return cls(
            str(product_data["name"]),
            str(product_data["description"]),
            float(product_data["price"]),
            int(product_data["quantity"]),
        )


class Category:
    """
    Класс для описания категории товаров
    """

    category_count: int = 0  # Счетчик категорий
    product_count: int = 0  # Счетчик продуктов

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products else []  # Приватный атрибут списка товаров
        Category.category_count += 1
        if products:
            Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления продукта в категорию
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения списка продуктов в виде строки
        Формат: "Название продукта, X руб. Остаток: X шт.\n"
        """
        result: str = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


if __name__ == "__main__":
    # Создаем продукты
    product1: Product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3: Product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию с продуктами
    category1: Category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Выводим продукты через геттер
    print("Продукты в категории:")
    print(category1.products)

    # Добавляем новый продукт
    product4: Product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\nПосле добавления нового продукта:")
    print(category1.products)

    # Выводим общее количество продуктов во всех категориях
    print(f"Общее количество продуктов во всех категориях: {Category.product_count}")

    # Создаем новый продукт через класс-метод
    new_product: Product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print("\nНовый продукт, созданный через класс-метод:")
    print(f"Название: {new_product.name}")
    print(f"Описание: {new_product.description}")
    print(f"Цена: {new_product.price}")
    print(f"Количество: {new_product.quantity}")

    # Тестируем сеттер цены
    print("\nТестирование сеттера цены:")
    new_product.price = 800
    print(f"Цена после изменения: {new_product.price}")

    # Попытка установить отрицательную цену
    print("\nПопытка установить отрицательную цену -100:")
    new_product.price = -100
    print(f"Цена после попытки: {new_product.price}")

    # Попытка установить нулевую цену
    print("\nПопытка установить нулевую цену:")
    new_product.price = 0
    print(f"Цена после попытки: {new_product.price}")
