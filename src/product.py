class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта
        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        """
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

    def __str__(self) -> str:
        """
        Строковое представление продукта
        Формат: Название продукта, X руб. Остаток: X шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение продуктов для получения общей стоимости всех товаров
        Возвращает: price1 * quantity1 + price2 * quantity2
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")

        return (self.price * self.quantity) + (other.price * other.quantity)
