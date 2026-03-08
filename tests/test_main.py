import pytest
from main import Product, Smartphone, LawnGrass, Category


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product("Тестовый продукт", "Описание", 1000.0, 10)
        assert product.name == "Тестовый продукт"
        assert product.description == "Описание"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_price_setter_positive(self):
        """Тест установки положительной цены"""
        product = Product("Тест", "Описание", 1000.0, 10)
        product.price = 1500.0
        assert product.price == 1500.0

    def test_price_setter_negative(self):
        """Тест установки отрицательной цены"""
        product = Product("Тест", "Описание", 1000.0, 10)
        with pytest.raises(ValueError):
            product.price = -100

    def test_price_setter_zero(self):
        """Тест установки нулевой цены"""
        product = Product("Тест", "Описание", 1000.0, 10)
        with pytest.raises(ValueError):
            product.price = 0

    def test_add_same_class(self):
        """Тест сложения продуктов одного класса"""
        product1 = Product("Товар 1", "Описание", 100.0, 2)
        product2 = Product("Товар 2", "Описание", 200.0, 3)
        assert (product1 + product2) == (100 * 2 + 200 * 3)


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        smartphone = Smartphone("iPhone 15", "512GB", 120000.0, 3, 98.5, "15", 512, "Black")

        assert smartphone.name == "iPhone 15"
        assert smartphone.description == "512GB"
        assert smartphone.price == 120000.0
        assert smartphone.quantity == 3
        assert smartphone.efficiency == 98.5
        assert smartphone.model == "15"
        assert smartphone.memory == 512
        assert smartphone.color == "Black"

    def test_smartphone_addition(self):
        """Тест сложения смартфонов"""
        s1 = Smartphone("S23", "256GB", 80000.0, 2, 95.0, "S23", 256, "Gray")
        s2 = Smartphone("S23+", "512GB", 100000.0, 1, 96.0, "S23+", 512, "Black")

        assert (s1 + s2) == (80000 * 2 + 100000 * 1)


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass("Трава", "Для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        assert grass.name == "Трава"
        assert grass.description == "Для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_grass_addition(self):
        """Тест сложения газонной травы"""
        g1 = LawnGrass("Трава 1", "Описание", 500.0, 10, "Россия", "7 дней", "Зеленый")
        g2 = LawnGrass("Трава 2", "Описание", 600.0, 5, "США", "5 дней", "Темно-зеленый")

        assert (g1 + g2) == (500 * 10 + 600 * 5)


    def test_add_product_invalid(self):
        """Тест добавления невалидного продукта"""
        category = Category("Смартфоны", "Описание")

        with pytest.raises(TypeError):
            category.add_product("Это не продукт")

        with pytest.raises(TypeError):
            category.add_product(123)

    def test_products_property(self):
        """Тест свойства products"""
        product = Product("Тестовый товар", "Описание", 1500.0, 5)
        category = Category("Категория", "Описание", [product])

        expected_output = "Тестовый товар, 1500.0 руб. Остаток: 5 шт.\n"
        assert category.products == expected_output

    def test_product_count(self):
        """Тест счетчика продуктов"""
        initial_count = Category.product_count

        product1 = Product("Товар 1", "Описание", 100.0, 1)
        product2 = Product("Товар 2", "Описание", 200.0, 2)

        Category("Категория 1", "Описание", [product1])
        Category("Категория 2", "Описание", [product2])

        assert Category.product_count == initial_count + 2
