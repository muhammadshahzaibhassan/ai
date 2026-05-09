def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp = float(input("Enter temperature: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()
if unit == "C":
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {result}°F")
elif unit == "F":
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {result}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")