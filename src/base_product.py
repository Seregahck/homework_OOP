from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Абстрактный метод инициализации продукта"""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Абстрактный метод получения цены"""
        pass

    @abstractmethod
    def set_price(self, price: float):
        """Абстрактный метод установки цены"""
        pass

    @abstractmethod
    def get_quantity(self) -> int:
        """Абстрактный метод получения количества"""
        pass

    @abstractmethod
    def set_quantity(self, quantity: int):
        """Абстрактный метод установки количества"""
        pass
