import pytest
from typing import List
from main import Product, Category


def test_product_creation() -> None:
    """Тест создания продукта"""
    product: Product = Product("Test", "Description", 100, 10)
    assert product.name == "Test"
    assert product.description == "Description"
    assert product.price == 100
    assert product.quantity == 10


def test_product_price_getter() -> None:
    """Тест геттера цены"""
    product: Product = Product("Test", "Description", 100, 10)
    assert product.price == 100


def test_product_price_setter_positive() -> None:
    """Тест сеттера цены с положительным значением"""
    product: Product = Product("Test", "Description", 100, 10)
    product.price = 150
    assert product.price == 150


def test_product_price_setter_negative(capsys) -> None:
    """Тест сеттера цены с отрицательным значением"""
    product: Product = Product("Test", "Description", 100, 10)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100  # Цена не изменилась


def test_product_price_setter_zero(capsys) -> None:
    """Тест сеттера цены с нулевым значением"""
    product: Product = Product("Test", "Description", 100, 10)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100  # Цена не изменилась


def test_product_new_product_classmethod() -> None:
    """Тест класс-метода new_product"""
    data: dict = {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 100,
        'quantity': 10
    }
    product: Product = Product.new_product(data)
    assert product.name == 'Test Product'
    assert product.description == 'Test Description'
    assert product.price == 100
    assert product.quantity == 10


def test_category_creation() -> None:
    """Тест создания категории"""
    category: Category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == ""  # Пустая строка через геттер


def test_category_with_products() -> None:
    """Тест создания категории с продуктами"""
    product1: Product = Product("Product 1", "Desc 1", 100, 5)
    product2: Product = Product("Product 2", "Desc 2", 200, 10)
    category: Category = Category("Test", "Desc", [product1, product2])

    expected: str = "Product 1, 100 руб. Остаток: 5 шт.\nProduct 2, 200 руб. Остаток: 10 шт.\n"
    assert category.products == expected


def test_add_product_to_category() -> None:
    """Тест добавления продукта в категорию"""
    category: Category = Category("Test", "Desc")
    product: Product = Product("New Product", "Desc", 300, 7)

    category.add_product(product)
    expected: str = "New Product, 300 руб. Остаток: 7 шт.\n"
    assert category.products == expected


def test_category_counters() -> None:
    """Тест счетчиков категорий и продуктов"""
    initial_category_count: int = Category.category_count
    initial_product_count: int = Category.product_count

    category1: Category = Category("Category 1", "Desc")
    category2: Category = Category("Category 2", "Desc")

    product1: Product = Product("Product 1", "Desc", 100, 5)
    product2: Product = Product("Product 2", "Desc", 200, 10)

    category1.add_product(product1)
    category1.add_product(product2)

    assert Category.category_count == initial_category_count + 2
    assert Category.product_count == initial_product_count + 2


def test_product_private_attribute() -> None:
    """Тест приватности атрибута цены"""
    product: Product = Product("Test", "Desc", 100, 10)
    with pytest.raises(AttributeError):
        product.__price  # Должно вызывать ошибку


def test_category_private_attribute() -> None:
    """Тест приватности атрибута products"""
    category: Category = Category("Test", "Desc")
    with pytest.raises(AttributeError):
        category.__products  # Должно вызывать ошибку


def test_products_format() -> None:
    """Тест формата вывода продуктов"""
    product: Product = Product("Test Product", "Desc", 1500, 3)
    category: Category = Category("Test", "Desc")
    category.add_product(product)

    expected: str = "Test Product, 1500 руб. Остаток: 3 шт.\n"
    assert category.products == expected


def test_add_product_returns_none() -> None:
    """Тест что add_product не возвращает значение"""
    category: Category = Category("Test", "Desc")
    product: Product = Product("Test", "Desc", 100, 5)
    result = category.add_product(product)
    assert result is None


def test_category_product_count_with_initial_products() -> None:
    """Тест счетчика продуктов при создании категории с продуктами"""
    initial_count: int = Category.product_count

    product1: Product = Product("Product 1", "Desc", 100, 5)
    product2: Product = Product("Product 2", "Desc", 200, 10)
    category: Category = Category("Test", "Desc", [product1, product2])

    assert Category.product_count == initial_count + 2


def test_multiple_categories_product_count() -> None:
    """Тест счетчика продуктов при нескольких категориях"""
    initial_count: int = Category.product_count

    category1: Category = Category("Category 1", "Desc")
    category2: Category = Category("Category 2", "Desc")

    product1: Product = Product("Product 1", "Desc", 100, 5)
    product2: Product = Product("Product 2", "Desc", 200, 10)
    product3: Product = Product("Product 3", "Desc", 300, 15)

    category1.add_product(product1)
    category1.add_product(product2)
    category2.add_product(product3)

    assert Category.product_count == initial_count + 3