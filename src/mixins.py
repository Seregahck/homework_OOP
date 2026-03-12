class ReprMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        """Выводит информацию о создании объекта"""
        args_str = self._format_args(*args)
        kwargs_str = self._format_kwargs(**kwargs)
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args_str}{kwargs_str}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Возвращает строковое представление объекта"""
        attrs = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                attrs.append(f"{key}='{value}'")
            else:
                attrs.append(f"{key}={value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def _format_args(self, *args):
        """Форматирует позиционные аргументы для вывода"""
        if not args:
            return ""
        return f"{', '.join(repr(arg) for arg in args)}"

    def _format_kwargs(self, **kwargs):
        """Форматирует именованные аргументы для вывода"""
        if not kwargs:
            return ""
        if self._format_args():
            return f", {', '.join(f'{k}={repr(v)}' for k, v in kwargs.items())}"
        return f"{', '.join(f'{k}={repr(v)}' for k, v in kwargs.items())}"
