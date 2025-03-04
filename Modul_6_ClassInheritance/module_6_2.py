class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color.lower() if color.lower() in self.__COLOR_VARIANTS else 'unknown'
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Тестирование работы классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')  # Недопустимый цвет
vehicle1.set_color('BLACK')  # Допустимый цвет
vehicle1.owner = 'Vasyok'  # Меняем владельца

# Проверяем изменения
vehicle1.print_info()
