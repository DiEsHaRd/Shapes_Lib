from shapes import Circle, Triangle, ShapeCalculator
from abc import ABC
import math


# 1. Демонстрация добавления новой фигуры (прямоугольник)
class Rectangle(ShapeCalculator, ABC):
    #Новая фигура - прямоугольник

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        if not self.is_valid():
            raise ValueError("Невозможно вычислить площадь невалидного прямоугольника")
        return self.width * self.height

    def is_valid(self) -> bool:
        return self.width > 0 and self.height > 0

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# 2. Добавляем поддержку прямоугольника в калькулятор
class ExtendedShapeCalculator(ShapeCalculator):
#  Расширенный калькулятор с поддержкой прямоугольника

    @staticmethod
    def create_rectangle(width: float, height: float) -> Rectangle:
        return Rectangle(width, height)

    @staticmethod
    def calculate_area(shape):
        #Переопределяем метод для поддержки новых фигур
        if not shape.is_valid():
            raise ValueError("Фигура невалидна")
        return shape.area()


# 3. Добавим еще одну фигуру - квадрат
class Square(Rectangle):
    # Квадрат как частный случай прямоугольника

    def __init__(self, side: float):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"


class UltimateShapeCalculator(ExtendedShapeCalculator):
    #Калькулятор с поддержкой всех фигур

    @staticmethod
    def create_square(side: float) -> Square:
        return Square(side)


def main():
    print("-_- Демонстрация библиотеки для вычисления площадей фигур -_-\n")

    # Создаем экземпляр калькулятора
    calculator = UltimateShapeCalculator()

    # 4. Создаем различные фигуры
    shapes = [
        calculator.create_circle(5),  # Круг радиусом 5
        calculator.create_triangle(3, 4, 5),  # Прямоугольный треугольник
        calculator.create_triangle(5, 5, 5),  # Равносторонний треугольник
        calculator.create_rectangle(4, 6),  # Прямоугольник 4x6
        calculator.create_square(5),  # Квадрат со стороной 5
        calculator.create_circle(2.5),  # Круг радиусом 2.5
        calculator.create_triangle(6, 8, 10),  # Еще один прямоугольный треугольник
    ]

    # 5. Вычисляем площади всех фигур (полиморфизм в действии)
    print("Расчет площадей всех фигур:")
    print("-" * 50)

    total_area = 0
    for i, shape in enumerate(shapes, 1):
        try:
            area = calculator.calculate_area(shape)
            total_area += area

            # Выводим информацию о фигуре
            print(f"{i}. {shape}")
            print(f"   Площадь: {area:.2f}")

            # Для треугольника дополнительно проверяем прямоугольность
            if isinstance(shape, Triangle):
                is_right = shape.is_right_triangle()
                print(f"   Прямоугольный: {'Да' if is_right else 'Нет'}")

            # Для круга выводим дополнительную информацию
            if isinstance(shape, Circle):
                diameter = 2 * shape.radius
                print(f"   Диаметр: {diameter:.2f}")

            print()

        except ValueError as e:
            print(f"{i}. {shape} - ОШИБКА: {e}\n")

    print(f"Общая площадь всех фигур: {total_area:.2f}")
    print("-" * 50)

    # 6. Демонстрация работы с невалидными фигурами
    print("\n-_- Демонстрация обработки невалидных фигур -_-")

    invalid_shapes = [
        Circle(-1),  # Отрицательный радиус
        Triangle(1, 1, 3),  # Несуществующий треугольник
        Rectangle(0, 5),  # Нулевая ширина
        Triangle(-2, 3, 4),  # Отрицательная сторона
    ]

    for i, shape in enumerate(invalid_shapes, 1):
        print(f"{i}. {shape}")
        print(f"   Валидна: {'Да' if shape.is_valid() else 'Нет'}")

        try:
            area = calculator.calculate_area(shape)
            print(f"   Площадь: {area:.2f}")
        except ValueError as e:
            print(f"   Ошибка при вычислении площади: {e}")
        print()

    # 7. Демонстрация легкости добавления новых фигур
    print("\n-_- Демонстрация расширяемости -_-")

    # Добавим еще одну фигуру на лету
    class Ellipse:
      #  Новая фигура - эллипс

        def __init__(self, a: float, b: float):
            self.a = a  # большая полуось
            self.b = b  # малая полуось

        def area(self) -> float:
            if not self.is_valid():
                raise ValueError("Невозможно вычислить площадь невалидного эллипса")
            return math.pi * self.a * self.b

        def is_valid(self) -> bool:
            return self.a > 0 and self.b > 0

        def __repr__(self):
            return f"Ellipse(a={self.a}, b={self.b})"

    # Теперь эллипс можно использовать вместе с другими фигурами
    ellipse = Ellipse(3, 2)
    print(f"Новая фигура: {ellipse}")
    print(f"Площадь эллипса: {ellipse.area():.2f}")
    print(f"Валидна: {'Да' if ellipse.is_valid() else 'Нет'}")


if __name__ == "__main__":
    main()