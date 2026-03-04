from typing import List, Optional
from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов (опционально)
        """
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products is not None else []

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию"""
        self.__products.append(product)

    @property
    def products(self) -> List[str]:
        """
        Геттер для получения списка продуктов
        В соответствии с заданием должен возвращать список строковых представлений продуктов
        """
        # Возвращаем список строк, а не объектов
        return [str(product) for product in self.__products]

    @property
    def products_objects(self) -> List[Product]:
        """
        Дополнительное свойство для получения исходных объектов (если нужно)
        """
        return self.__products.copy()

    def __str__(self) -> str:
        """
        Строковое представление категории
        Рассчитывает общее количество товаров на складе по всем продуктам
        Формат: Название категории, количество продуктов: X шт.
        """
        total_quantity: int = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
