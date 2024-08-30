def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

# Take input from user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
kelvin = fahrenheit_to_kelvin(fahrenheit)
print(f"{fahrenheit}°F is equal to {kelvin:.2f}K.")
