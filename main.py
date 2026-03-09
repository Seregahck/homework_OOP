from src.product import Product, Smartphone, LawnGrass
from src.category import Category


if __name__ == "__main__":
    # Создание обычных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка работы категории
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.get_products_list()))
    print(category1.category_count)
    print(category1.product_count)

    # Создание продукта в новой категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    # Вывод информации о второй категории
    print(category2.name)
    print(category2.description)
    print(len(category2.get_products_list()))
    print(category2.products)

    # Вывод счетчиков категорий и продуктов
    print(Category.category_count)
    print(Category.product_count)

    # Создание смартфона
    smartphone = Smartphone(
        "Samsung Galaxy S24 Ultra",
        "Новейший флагман Samsung",
        150000.0,
        3,
        "Snapdragon 8 Gen 3",
        "S24 Ultra",
        512,
        "Титан",
    )
    print(f"Создан смартфон: {smartphone.name}, модель: {smartphone.model}")

    # Создание газонной травы
    grass = LawnGrass(
        "Газон спортивный", "Смесь трав для спортивных газонов", 2500.0, 10, "Россия", "10-14 дней", "Зеленый"
    )
    print(f"Создана газонная трава: {grass.name}, страна производитель: {grass.country}")
