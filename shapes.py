import math
from abc import ABC, abstractmethod
from typing import Type, Dict


class Shape(ABC):
   # Абстрактный базовый класс для всех фигур

    @abstractmethod
    def area(self) -> float:
        # Вычисляет площадь фигуры
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        # Проверяет, может ли фигура существовать с заданными параметрами
        pass


class Circle(Shape):
    # Класс для представления круга

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        # Вычисляет площадь круга
        if not self.is_valid():
            raise ValueError("Невозможно вычислить площадь невалидного круга")
        return math.pi * self.radius ** 2

    def is_valid(self) -> bool:
        # Круг valid если радиус неотрицательный
        return self.radius >= 0

    def __repr__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    # Класс для представления треугольника

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
       # Вычисляет площадь треугольника по формуле Герона
        if not self.is_valid():
            raise ValueError("Невозможно вычислить площадь невалидного треугольника")

        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self) -> float:
       # Вычисляет периметр треугольника
        return self.side_a + self.side_b + self.side_c

    def is_valid(self) -> bool:
       # Проверяет, может ли треугольник существовать
        # Все стороны должны быть положительными
        if any(side <= 0 for side in [self.side_a, self.side_b, self.side_c]):
            return False

        # Должно выполняться неравенство треугольника
        a, b, c = self.side_a, self.side_b, self.side_c
        return (a + b > c) and (a + c > b) and (b + c > a)

    def is_right_triangle(self, tolerance: float = 1e-10) -> bool:
        #Проверяет, является ли треугольник прямоугольным
        if not self.is_valid():
            raise ValueError("Невозможно проверить прямоугольность невалидного треугольника")

        sides = sorted([self.side_a, self.side_b, self.side_c])
        # Теорема Пифагора: a² + b² = c²
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance

    def __repr__(self):
        return f"Triangle(a={self.side_a}, b={self.side_b}, c={self.side_c})"


class ShapeCalculator:
    #Фабрика для вычисления площади фигур без знания типа в compile-time

    @staticmethod
    def calculate_area(shape: Shape) -> float:
        # Вычисляет площадь любой фигуры, наследующей от Shape
        if not shape.is_valid():
            raise ValueError("Фигура невалидна")
        return shape.area()

    @staticmethod
    def create_circle(radius: float) -> Circle:
        # Создает круг
        return Circle(radius)

    @staticmethod
    def create_triangle(a: float, b: float, c: float) -> Triangle:
        # Создает треугольник
        return Triangle(a, b, c)