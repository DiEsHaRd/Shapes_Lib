import unittest
import math
from shapes import Circle, Triangle, ShapeCalculator


class TestCircle(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25, places=7)

    def test_circle_negative_radius(self):
        circle = Circle(-1)
        self.assertFalse(circle.is_valid())
        with self.assertRaises(ValueError):
            circle.area()

    def test_circle_zero_radius(self):
        circle = Circle(0)
        self.assertEqual(circle.area(), 0)
        self.assertTrue(circle.is_valid())

    def test_circle_validity(self):
        self.assertTrue(Circle(1).is_valid())
        self.assertTrue(Circle(0).is_valid())
        self.assertFalse(Circle(-1).is_valid())


class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=7)

    def test_triangle_equilateral_area(self):
        triangle = Triangle(2, 2, 2)
        expected_area = (math.sqrt(3) / 4) * 4  # Формула для равностороннего треугольника
        self.assertAlmostEqual(triangle.area(), expected_area, places=7)

    def test_triangle_invalid_sides(self):
        # Треугольник, который не может существовать
        triangle = Triangle(1, 2, 10)
        self.assertFalse(triangle.is_valid())
        with self.assertRaises(ValueError):
            triangle.area()

    def test_triangle_negative_sides(self):
        triangle = Triangle(-1, 2, 3)
        self.assertFalse(triangle.is_valid())
        with self.assertRaises(ValueError):
            triangle.area()

    def test_triangle_zero_side(self):
        triangle = Triangle(0, 2, 3)
        self.assertFalse(triangle.is_valid())
        with self.assertRaises(ValueError):
            triangle.area()

    def test_triangle_right_angle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())
        self.assertTrue(Triangle(5, 12, 13).is_right_triangle())
        self.assertFalse(Triangle(2, 3, 4).is_right_triangle())

    def test_triangle_right_angle_invalid(self):
        triangle = Triangle(1, 1, 3)  # Невалидный треугольник
        with self.assertRaises(ValueError):
            triangle.is_right_triangle()

    def test_triangle_validity(self):
        self.assertTrue(Triangle(3, 4, 5).is_valid())
        self.assertTrue(Triangle(5, 5, 5).is_valid())
        self.assertFalse(Triangle(1, 1, 3).is_valid())
        self.assertFalse(Triangle(-1, 2, 3).is_valid())
        self.assertFalse(Triangle(0, 2, 3).is_valid())


class TestShapeCalculator(unittest.TestCase):

    def test_calculate_area_polymorphism(self):
        calculator = ShapeCalculator()

        circle = Circle(2)
        triangle = Triangle(3, 4, 5)

        # Вычисление площади без знания конкретного типа
        circle_area = calculator.calculate_area(circle)
        triangle_area = calculator.calculate_area(triangle)

        self.assertAlmostEqual(circle_area, math.pi * 4, places=7)
        self.assertAlmostEqual(triangle_area, 6.0, places=7)

    def test_calculate_area_invalid_shape(self):
        calculator = ShapeCalculator()
        invalid_circle = Circle(-1)
        invalid_triangle = Triangle(1, 1, 3)

        with self.assertRaises(ValueError):
            calculator.calculate_area(invalid_circle)

        with self.assertRaises(ValueError):
            calculator.calculate_area(invalid_triangle)

    def test_factory_methods(self):
        calculator = ShapeCalculator()

        circle = calculator.create_circle(3)
        triangle = calculator.create_triangle(6, 8, 10)

        self.assertIsInstance(circle, Circle)
        self.assertIsInstance(triangle, Triangle)

        self.assertAlmostEqual(circle.area(), math.pi * 9, places=7)
        self.assertAlmostEqual(triangle.area(), 24.0, places=7)
        self.assertTrue(triangle.is_right_triangle())


class TestIntegration(unittest.TestCase):

    def test_multiple_shapes_processing(self):
        calculator = ShapeCalculator()

        shapes = [
            Circle(1),
            Triangle(3, 4, 5),
            Circle(2),
            Triangle(5, 5, 5)
        ]

        areas = [calculator.calculate_area(shape) for shape in shapes]

        expected_areas = [
            math.pi,
            6.0,
            math.pi * 4,
            (math.sqrt(3) / 4) * 25  # Площадь равностороннего треугольника
        ]

        for actual, expected in zip(areas, expected_areas):
            self.assertAlmostEqual(actual, expected, places=7)


if __name__ == '__main__':
    unittest.main()