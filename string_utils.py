def reverse_string(s: str) -> str:
    return s[::-1]

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        return 0.0
    return a / b