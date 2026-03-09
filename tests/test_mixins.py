import pytest
from src.product import Product


def test_repr_mixin(capsys):
    """Тест миксина для вывода информации при создании"""
    product = Product("Тестовый товар", "Тестовое описание", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out

