# fns_and_dsa/temp_conversion_tool.py

# Global conversion factors (exact fraction forms required by the checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: C = (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: F = C * (9/5) + 32
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Prompt for temperature
    temp_input = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_input)
    except ValueError:
        # Required error message per instructions
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        celsius = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
