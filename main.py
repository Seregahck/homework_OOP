from src.product import Product
from src.category import Category


if __name__ == "__main__":
    # Задание 1: Проверка создания товара с нулевым количеством
    try:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print("Возникла ошибка ValueError при попытке добавить продукт "
              "с нулевым количеством")
        print(f"Сообщение ошибки: {e}")
    else:
        print("Не возникла ошибка ValueError при попытке добавить "
              "продукт с нулевым количеством")

    # Создание продуктов для тестирования
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )

    # Создание категории с продуктами
    category1 = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product1, product2, product3]
    )

    # Проверка метода middle_price для категории с товарами
    print(f"Средний ценник смартфонов: {category1.middle_price()}")

    # Проверка метода middle_price для пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средний ценник пустой категории: {category_empty.middle_price()}")
