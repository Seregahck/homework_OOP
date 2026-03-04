import pytest
from src.product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5
        )
        assert product.name == "Samsung Galaxy S23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

    @pytest.mark.parametrize("name, description, price, quantity, expected", [
        (
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
                "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        ),
        (
                "Iphone 15",
                "512GB, Gray space",
                210000.0,
                8,
                "Iphone 15, 210000.0 руб. Остаток: 8 шт."
        ),
        (
                "Xiaomi Redmi Note 11",
                "1024GB, Синий",
                31000.0,
                14,
                "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        ),
    ])
    def test_product_str(self, name, description, price, quantity, expected):
        """Тест строкового представления продукта"""
        product = Product(name, description, price, quantity)
        assert str(product) == expected

    def test_product_addition(self):
        """Тест сложения двух продуктов"""
        product1 = Product("A", "Desc1", 100, 10)  # 1000
        product2 = Product("B", "Desc2", 200, 2)  # 400
        result = product1 + product2
        assert result == 1400  # 1000 + 400

    def test_product_addition_with_main_example(self):
        """Тест сложения продуктов из примера в main.py"""
        product1 = Product("Samsung Galaxy S23 Ultra", "desc", 180000.0, 5)
        product2 = Product("Iphone 15", "desc", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "desc", 31000.0, 14)

        # 180000*5 + 210000*8 = 900000 + 1680000 = 2580000
        assert product1 + product2 == 2580000

        # 180000*5 + 31000*14 = 900000 + 434000 = 1334000
        assert product1 + product3 == 1334000

        # 210000*8 + 31000*14 = 1680000 + 434000 = 2114000
        assert product2 + product3 == 2114000

    def test_product_addition_with_zero_quantity(self):
        """Тест сложения с продуктом, у которого нулевое количество"""
        product1 = Product("A", "Desc", 100, 10)  # 1000
        product2 = Product("B", "Desc", 200, 0)  # 0
        result = product1 + product2
        assert result == 1000

    def test_product_addition_with_non_product(self):
        """Тест сложения с объектом другого типа"""
        product = Product("A", "Desc", 100, 10)

        with pytest.raises(TypeError):
            result = product + 100

        with pytest.raises(TypeError):
            result = product + "строка"
