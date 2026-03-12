from typing import List
from src.product import Product


class Category:
    """Класс для описания категории товаров"""

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.
        Если категория пуста, возвращает 0.
        """
        try:
            total: float = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0.0
