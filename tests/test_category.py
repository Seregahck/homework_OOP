import pytest
from src.product import Product
from src.category import Category


def test_product_zero_quantity() -> None:
    """Тест на исключение при создании продукта с нулевым количеством"""
    with pytest.raises(ValueError) as exc_info:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_normal_quantity() -> None:
    """Тест создания продукта с нормальным количеством"""
    product = Product("Тестовый товар", "Описание", 100.0, 5)
    assert product.name == "Тестовый товар"
    assert product.quantity == 5


def test_category_middle_price_normal() -> None:
    """Тест среднего ценника для категории с товарами"""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 3)
    product3 = Product("Товар 3", "Описание 3", 300.0, 7)

    category = Category("Тестовая категория", "Описание",
                        [product1, product2, product3])

    expected_price = (100.0 + 200.0 + 300.0) / 3
    assert category.middle_price() == expected_price


def test_category_middle_price_empty() -> None:
    """Тест среднего ценника для пустой категории"""
    category = Category("Пустая категория", "Описание", [])
    assert category.middle_price() == 0.0


def test_category_middle_price_single_product() -> None:
    """Тест среднего ценника для категории с одним товаром"""
    product = Product("Товар 1", "Описание 1", 150.0, 5)
    category = Category("Категория", "Описание", [product])

    assert category.middle_price() == 150.0


def test_repr_mixin(capsys: pytest.CaptureFixture) -> None:
    """Тест миксина для вывода информации при создании"""
    Product("Тестовый товар", "Тестовое описание", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
