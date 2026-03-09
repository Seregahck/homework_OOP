from src.base_product import BaseProduct
from src.mixins import ReprMixin


class Product(ReprMixin, BaseProduct):
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def get_price(self) -> float:
        """Получение цены (реализация абстрактного метода)"""
        return self._price

    def set_price(self, price: float):
        """Установка цены (реализация абстрактного метода)"""
        self.price = price

    def get_quantity(self) -> int:
        """Получение количества (реализация абстрактного метода)"""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Установка количества (реализация абстрактного метода)"""
        self.quantity = quantity


class Smartphone(Product):
    """Класс для описания смартфона"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для описания газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
