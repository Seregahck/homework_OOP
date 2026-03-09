class Category:
    """Класс для описания категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        """Геттер для списка продуктов"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self):
        """Метод для получения списка продуктов"""
        return self.__products
