from src.repr_mixin import ReprMixin


class Product(ReprMixin):
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        # Вызываем миксин для вывода
        ReprMixin.__init__(self, name, description, price, quantity)

        # Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        # Инициализация атрибутов
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
