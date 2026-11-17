"""Функции для вычислений с кругом."""

import math

from geometry_validation import validate_measure


def area(radius):
    """Возвращает площадь круга по заданному радиусу."""
    validate_measure(radius, "Радиус")
    return math.pi * radius ** 2


def circumference(radius):
    """Возвращает длину окружности по заданному радиусу."""
    validate_measure(radius, "Радиус")
    return 2 * math.pi * radius
