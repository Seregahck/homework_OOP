from typing import Any, List


class ReprMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Выводит информацию о создании объекта"""
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        # Не вызываем super().__init__, так как это может вызвать проблемы

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        attrs: List[str] = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                attrs.append(f"{key}='{value}'")
            else:
                attrs.append(f"{key}={value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"
