from typing import List
from src.product import Product


class Category:
    """Класс для описания категории товаров"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Геттер для списка продуктов"""
        products_str: str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self) -> List[Product]:
        """Метод для получения списка продуктов"""
        return self.__products
