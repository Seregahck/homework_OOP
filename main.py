from typing import List, Optional, Union


class Product:
    """Базовый класс для всех товаров"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией"""
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля")
        self.__price = value

    def __add__(self, other: "Product") -> float:
        """Сложение товаров по цене * количество"""
        # Используем type() для проверки типов
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency: float = efficiency
        self.model: str = model
        self.memory: int = memory
        self.color: str = color


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country: str = country
        self.germination_period: str = germination_period
        self.color: str = color


class Category:
    """Класс для категорий товаров"""

    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products else []
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        """Геттер для списка продуктов в строковом формате"""
        product_list: str = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list

    def get_products_list(self) -> List[Product]:
        """Метод для получения списка продуктов"""
        return self.__products

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию"""
        # Используем type() для проверки, является ли объект экземпляром Product или его наследников
        # Для проверки на принадлежность к классу или его наследникам используем issubclass()
        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1


# Тестирование функциональности
if __name__ == "__main__":
    # Создание смартфонов
    smartphone1: Smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2: Smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3: Smartphone = Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий"
    )

    # Вывод информации о смартфонах
    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)
    print()

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)
    print()

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)
    print()

    # Создание травы
    grass1: LawnGrass = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )
    grass2: LawnGrass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    # Вывод информации о траве
    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)
    print()

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)
    print()

    # Тестирование сложения
    smartphone_sum: float = smartphone1 + smartphone2
    print(f"Сумма смартфонов: {smartphone_sum}")

    grass_sum: float = grass1 + grass2
    print(f"Сумма травы: {grass_sum}")

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")
    print()

    # Создание категорий
    category_smartphones: Category = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass: Category = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    # Добавление продукта
    category_smartphones.add_product(smartphone3)

    # Вывод продуктов категории
    print("Продукты категории смартфоны:")
    print(category_smartphones.products)

    print(f"Общее количество продуктов: {Category.product_count}")

    # Тестирование добавления не-продукта
    try:
        category_smartphones.add_product("Not a product")  # type: ignore
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")

    # Демонстрация работы get_products_list
    print(f"\nКоличество смартфонов в категории: {len(category_smartphones.get_products_list())}")
