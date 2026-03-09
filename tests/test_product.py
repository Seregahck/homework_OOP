import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


def test_product_creation():
    """Тест создания продукта"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_product_price_setter():
    """Тест сеттера цены"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 45000.0
    assert product.price == 45000.0


def test_product_price_setter_negative():
    """Тест сеттера цены с отрицательным значением"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = -1000
    assert product.price == 50000.0


def test_smartphone_creation():
    """Тест создания смартфона"""
    smartphone = Smartphone(
        "Samsung Galaxy S24 Ultra",
        "Флагман Samsung",
        150000.0,
        3,
        "Snapdragon 8 Gen 3",
        "S24 Ultra",
        512,
        "Титан"
    )
    assert smartphone.name == "Samsung Galaxy S24 Ultra"
    assert smartphone.price == 150000.0
    assert smartphone.performance == "Snapdragon 8 Gen 3"
    assert smartphone.model == "S24 Ultra"
    assert smartphone.memory == 512
    assert smartphone.color == "Титан"


def test_lawn_grass_creation():
    """Тест создания газонной травы"""
    grass = LawnGrass(
        "Газон спортивный",
        "Смесь трав",
        2500.0,
        10,
        "Россия",
        "10-14 дней",
        "Зеленый"
    )
    assert grass.name == "Газон спортивный"
    assert grass.price == 2500.0
    assert grass.country == "Россия"
    assert grass.germination_period == "10-14 дней"
    assert grass.color == "Зеленый"


def test_category_creation():
    """Тест создания категории"""
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 10)

    category = Category("Категория1", "Описание категории", [product1, product2])

    assert category.name == "Категория1"
    assert category.description == "Описание категории"
    assert len(category.get_products_list()) == 2


def test_category_add_product():
    """Тест добавления продукта в категорию"""
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    category = Category("Категория1", "Описание категории", [product1])

    product2 = Product("Товар2", "Описание2", 200.0, 10)
    category.add_product(product2)

    assert len(category.get_products_list()) == 2


def test_category_count():
    """Тест подсчета категорий"""
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Категория1", "Описание", [])
    category2 = Category("Категория2", "Описание", [])

    assert Category.category_count == 2


def test_product_count():
    """Тест подсчета продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 10)

    category1 = Category("Категория1", "Описание", [product1, product2])

    assert Category.product_count == 2


def test_abstract_methods():
    """Тест абстрактных методов"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    assert product.get_price() == 50000.0
    assert product.get_quantity() == 10

    product.set_price(45000.0)
    product.set_quantity(15)

    assert product.get_price() == 45000.0
    assert product.get_quantity() == 15
