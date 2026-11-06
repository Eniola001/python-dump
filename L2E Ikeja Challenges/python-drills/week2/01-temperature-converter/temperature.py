def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convert_temperature(value, from_unit, to_unit):
    import math

    # Validate the temperature value
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number.")

    if not math.isfinite(value):
        raise ValueError("Temperature must be finite.")

    # Validate the units
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError("Units must be strings.")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = ("celsius", "fahrenheit", "kelvin")

    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Unsupported temperature unit.")

    # Convert the input to Celsius
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(value)
    else:
        celsius = value - 273.15

    # Validate absolute zero
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero.")

    # Convert Celsius to the target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "kelvin":
        return celsius_to_kelvin(celsius)