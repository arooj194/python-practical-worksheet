# I used if, elif and else to check the temperature.
# The program displays Cold, Mild or Warm based on the input.
# Exercise 1: Temperature Adviser

temperature = float(input("Temperature: "))

if temperature < 10:
    print("Result: Cold")
elif temperature < 25:
    print("Result: Mild")
else:
    print("Result: Warm")

if temperature < 0:
    print("Freezing temperature!")

