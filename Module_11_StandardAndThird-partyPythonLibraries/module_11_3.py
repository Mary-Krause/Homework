import inspect


def introspection_info(obj):
    """Функция для получения информации об объекте."""
    info = {
        "type": type(obj).__name__,
        "attributes": [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],
        "methods": [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")],
        "module": inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else "Built-in"
    }
    return info


# Пример с числом
number_info = introspection_info(42)
print(number_info)


# Пример с пользовательским классом
class SampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Hello, {self.name}!"


test_obj = SampleClass("Alice", 100)
obj_info = introspection_info(test_obj)
print(obj_info)