"""Функции для вычислений с квадратом."""

from geometry_validation import validate_measure


def area(side):
    """Возвращает площадь квадрата по заданной стороне."""
    validate_measure(side, "Сторона")
    return side ** 2


def perimeter(side):
    """Возвращает периметр квадрата по заданной стороне."""
    validate_measure(side, "Сторона")
    return 4 * side
