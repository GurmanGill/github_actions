def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def classify_number(value: int) -> str:
    if value > 0:
        return "positive"

    if value < 0:
        return "negative"

    return "zero"