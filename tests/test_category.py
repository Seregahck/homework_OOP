import pytest
from src.product import Product
from src.category import Category


class TestCategory:
    """Тесты для класса Category"""

    @pytest.fixture
    def sample_products(self):
        """Фикстура для создания тестовых продуктов"""
        return [
            Product("Samsung Galaxy S23 Ultra", "desc1", 180000.0, 5),
            Product("Iphone 15", "desc2", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "desc3", 31000.0, 14)
        ]

    @pytest.fixture
    def electronics_category(self, sample_products):
        """Фикстура для создания тестовой категории"""
        return Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            sample_products
        )

    def test_category_creation(self, sample_products):
        """Тест создания категории"""
        category = Category(
            "Смартфоны",
            "Описание смартфонов",
            sample_products
        )
        assert category.name == "Смартфоны"
        assert category.description == "Описание смартфонов"
        assert len(category.products) == 3

    def test_category_creation_without_products(self):
        """Тест создания категории без продуктов"""
        category = Category("Книги", "Описание книг")
        assert category.name == "Книги"
        assert category.description == "Описание книг"
        assert len(category.products) == 0

    def test_add_product(self, electronics_category):
        """Тест добавления продукта"""
        initial_count = len(electronics_category.products)
        new_product = Product("Test", "Desc", 100, 1)
        electronics_category.add_product(new_product)
        assert len(electronics_category.products) == initial_count + 1

    def test_category_str(self, electronics_category):
        """Тест строкового представления категории"""
        # 5 + 8 + 14 = 27
        expected = "Смартфоны, количество продуктов: 27 шт."
        result = str(electronics_category)
        print(f"Actual result: '{result}'")  # Для отладки
        assert result == expected

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории"""
        category = Category("Пустая", "Описание")
        assert str(category) == "Пустая, количество продуктов: 0 шт."

    def test_products_property_returns_strings(self, electronics_category):
        """Тест, что свойство products возвращает строки, а не объекты"""
        products_list = electronics_category.products
        assert isinstance(products_list, list)
        print(f"Products list: {products_list}")  # Для отладки
        for product_str in products_list:
            assert isinstance(product_str, str), f"Expected str, got {type(product_str)}"

    def test_products_property_content(self, electronics_category):
        """Тест содержимого свойства products"""
        products_list = electronics_category.products
        print(f"Products list: {products_list}")  # Для отладки

        expected = [
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        ]

        assert products_list == expected

    def test_products_objects_property(self, electronics_category):
        """Тест свойства products_objects (возвращает исходные объекты)"""
        objects_list = electronics_category.products_objects
        assert isinstance(objects_list, list)
        assert len(objects_list) == 3
        for obj in objects_list:
            assert isinstance(obj, Product)

    def test_products_property_updates_after_add(self, electronics_category):
        """Тест обновления свойства products после добавления продукта"""
        initial_count = len(electronics_category.products)
        assert initial_count == 3

        new_product = Product("Test Product", "Test Description", 1000.0, 2)
        electronics_category.add_product(new_product)

        updated_products = electronics_category.products
        assert len(updated_products) == 4
        assert updated_products[-1] == "Test Product, 1000.0 руб. Остаток: 2 шт."
