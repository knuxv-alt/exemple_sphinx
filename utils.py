def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convertit une température de Fahrenheit à Celsius.

    Args:
        fahrenheit: La température en Fahrenheit.

    Returns:
        La température convertie en Celsius.
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convertit une température de Celsius à Fahrenheit.

    Args:
        celsius: La température en Celsius.

    Returns:
        La température convertie en Fahrenheit.
    """
    return (celsius * 9.0 / 5.0) + 32

def kelvin_to_celsius(kelvin: float) -> float:
    """
    Convertit une température de Kelvin à Celsius.

    Args:
        kelvin: La température en Kelvin.

    Returns:
        La température convertie en Celsius.
    """
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    """
    Convertit une température de Celsius à Kelvin.

    Args:
        celsius: La température en Celsius.

    Returns:
        La température convertie en Kelvin.
    """
    return celsius + 273.15
