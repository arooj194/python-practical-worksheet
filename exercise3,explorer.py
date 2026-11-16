
# Explorer

n = int(input("Enter a positive number: "))

count = 0
total = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)
        count += 1
        total += number

print("Total even numbers:", count)
print("Sum of even numbers:", total)
