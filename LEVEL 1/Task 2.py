temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit == "C":
    converted = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit:", converted)

elif unit == "F":
    converted = (temperature - 32) * 5/9
    print("Temperature in Celsius:", converted)

else:
    print("Invalid unit entered")
