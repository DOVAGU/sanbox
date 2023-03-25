def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

temperature_str = input("Enter a temperature: ")
unit_str = input("Enter the unit of measure (F/C): ")

temperature = float(temperature_str)

if unit_str.upper() == "F":
    celsius = fahrenheit_to_celsius(temperature)
    print(f"{temperature:.1f} degrees Fahrenheit is {celsius:.1f} degrees Celsius")
elif unit_str.upper() == "C":
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"{temperature:.1f} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit")
else:
    print("Invalid unit of measure. Please enter 'F' or 'C'.")
