from src.base_product import BaseProduct
from src.mixins import ReprMixin


class Product(ReprMixin, BaseProduct):
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity: int = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __repr__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return super().__repr__()

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def get_price(self) -> float:
        """Получение цены (реализация абстрактного метода)"""
        return self._price

    def set_price(self, price: float) -> None:
        """Установка цены (реализация абстрактного метода)"""
        self.price = price

    def get_quantity(self) -> int:
        """Получение количества (реализация абстрактного метода)"""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Установка количества (реализация абстрактного метода)"""
        self.quantity = quantity


class Smartphone(Product):
    """Класс для описания смартфона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        performance: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.performance: str = performance
        self.model: str = model
        self.memory: int = memory
        self.color: str = color

    def __repr__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return super().__repr__()

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return f"{self.name} ({self.model}), {self.price} руб. Остаток: {self.quantity} шт."


class LawnGrass(Product):
    """Класс для описания газонной травы"""

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

    def __repr__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return super().__repr__()

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return f"{self.name} ({self.country}), {self.price} руб. Остаток: {self.quantity} шт."
