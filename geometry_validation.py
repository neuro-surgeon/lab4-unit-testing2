"""Общие правила проверки размеров геометрических фигур."""

import math


def validate_measure(value, parameter_name):
    """Проверяет, что размер — конечное неотрицательное число."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} должен быть числом int или float")

    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{parameter_name} должен быть конечным числом")

    if value < 0:
        raise ValueError(f"{parameter_name} не может быть отрицательным")
