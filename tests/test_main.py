import pytest
from main import Product, Category


def test_product_creation():
    """Тест создания продукта"""
    product = Product("Test", "Description", 100, 10)
    assert product.name == "Test"
    assert product.description == "Description"
    assert product.price == 100
    assert product.quantity == 10


def test_product_price_getter():
    """Тест геттера цены"""
    product = Product("Test", "Description", 100, 10)
    assert product.price == 100


def test_product_price_setter_positive():
    """Тест сеттера цены с положительным значением"""
    product = Product("Test", "Description", 100, 10)
    product.price = 150
    assert product.price == 150


def test_product_price_setter_negative(capsys):
    """Тест сеттера цены с отрицательным значением"""
    product = Product("Test", "Description", 100, 10)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100  # Цена не изменилась


def test_product_price_setter_zero(capsys):
    """Тест сеттера цены с нулевым значением"""
    product = Product("Test", "Description", 100, 10)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100  # Цена не изменилась


def test_product_new_product_classmethod():
    """Тест класс-метода new_product"""
    data = {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 100,
        'quantity': 10
    }
    product = Product.new_product(data)
    assert product.name == 'Test Product'
    assert product.description == 'Test Description'
    assert product.price == 100
    assert product.quantity == 10


def test_category_creation():
    """Тест создания категории"""
    category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == ""  # Пустая строка через геттер


def test_category_with_products():
    """Тест создания категории с продуктами"""
    product1 = Product("Product 1", "Desc 1", 100, 5)
    product2 = Product("Product 2", "Desc 2", 200, 10)
    category = Category("Test", "Desc", [product1, product2])
    
    expected = "Product 1, 100 руб. Остаток: 5 шт.\nProduct 2, 200 руб. Остаток: 10 шт.\n"
    assert category.products == expected


def test_add_product_to_category():
    """Тест добавления продукта в категорию"""
    category = Category("Test", "Desc")
    product = Product("New Product", "Desc", 300, 7)
    
    category.add_product(product)
    expected = "New Product, 300 руб. Остаток: 7 шт.\n"
    assert category.products == expected


def test_category_counters():
    """Тест счетчиков категорий и продуктов"""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    category1 = Category("Category 1", "Desc")
    category2 = Category("Category 2", "Desc")
    
    product1 = Product("Product 1", "Desc", 100, 5)
    product2 = Product("Product 2", "Desc", 200, 10)
    
    category1.add_product(product1)
    category1.add_product(product2)
    
    assert Category.category_count == initial_category_count + 2
    assert Category.product_count == initial_product_count + 2


def test_product_private_attribute():
    """Тест приватности атрибута цены"""
    product = Product("Test", "Desc", 100, 10)
    with pytest.raises(AttributeError):
        product.__price  # Должно вызывать ошибку


def test_category_private_attribute():
    """Тест приватности атрибута products"""
    category = Category("Test", "Desc")
    with pytest.raises(AttributeError):
        category.__products  # Должно вызывать ошибку


def test_products_format():
    """Тест формата вывода продуктов"""
    product = Product("Test Product", "Desc", 1500, 3)
    category = Category("Test", "Desc")
    category.add_product(product)
    
    expected = "Test Product, 1500 руб. Остаток: 3 шт.\n"
    assert category.products == expected


def test_add_product_returns_none():
    """Тест что add_product не возвращает значение"""
    category = Category("Test", "Desc")
    product = Product("Test", "Desc", 100, 5)
    result = category.add_product(product)
    assert result is None


def test_category_product_count_with_initial_products():
    """Тест счетчика продуктов при создании категории с продуктами"""
    initial_count = Category.product_count
    
    product1 = Product("Product 1", "Desc", 100, 5)
    product2 = Product("Product 2", "Desc", 200, 10)
    category = Category("Test", "Desc", [product1, product2])
    
    assert Category.product_count == initial_count + 2


def test_multiple_categories_product_count():
    """Тест счетчика продуктов при нескольких категориях"""
    initial_count = Category.product_count
    
    category1 = Category("Category 1", "Desc")
    category2 = Category("Category 2", "Desc")
    
    product1 = Product("Product 1", "Desc", 100, 5)
    product2 = Product("Product 2", "Desc", 200, 10)
    product3 = Product("Product 3", "Desc", 300, 15)
    
    category1.add_product(product1)
    category1.add_product(product2)
    category2.add_product(product3)
    
    assert Category.product_count == initial_count + 3