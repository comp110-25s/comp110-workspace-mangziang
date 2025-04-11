def celsius_to_fahrenheit(degrees: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit."""
    return (degrees * 9 / 5) + 32


celsius_to_fahrenheit(degrees=0)
celsius_to_fahrenheit(degrees=10)


def perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle"""
    return (length + width) * 2


perimeter(length=10.0, width=8.0)
print(perimeter(length=10.0, width=8.0))
