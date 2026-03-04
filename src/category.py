from typing import List, Optional

from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    # Атрибуты класса для подсчета статистики
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализация категории
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products is not None else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1
        # Увеличиваем счетчик продуктов
        Category.product_count += len(self.products)

    def __str__(self) -> str:
        """
        Строковое представление категории
        Формат: Название категории, количество продуктов: X шт.
        """
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию
        :param product: Продукт для добавления
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        self.products.append(product)
        Category.product_count += 1

    def remove_product(self, product: Product) -> None:
        """
        Удаление продукта из категории
        :param product: Продукт для удаления
        """
        if product in self.products:
            self.products.remove(product)
            Category.product_count -= 1
