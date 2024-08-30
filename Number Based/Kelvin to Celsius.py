def kelvin_to_celsius(k):
    return k - 273.15

# Take input from user
kelvin = float(input("Enter temperature in Kelvin: "))
celsius = kelvin_to_celsius(kelvin)
print(f"{kelvin}K is equal to {celsius:.2f}°C.")
