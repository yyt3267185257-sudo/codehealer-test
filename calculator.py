from typing import Iterable

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def safe_divide(a: float, b: float) -> float:
    """执行除法，除数为零时返回 0.0。"""
    if b == 0:
        return 0.0
    return a / b

def average(numbers: Iterable[float]) -> float:
    values = list(numbers)
    if not values:
        return 0.0
    return sum(values) / len(values)

def percentage(value: float, total: float) -> float:
    if total == 0:
        return 0.0
    return value / total * 100

def clamp(value: float, minimum: float, maximum: float) -> float:
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum")
    return max(minimum, min(value, maximum))

def calculate_discount(price: float, discount_rate: float) -> float:
    if price < 0:
        raise ValueError("price cannot be negative")
    rate = clamp(discount_rate, 0, 100)
    return round(price * (1 - rate / 100), 2)