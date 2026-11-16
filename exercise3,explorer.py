# I used a for loop to check numbers from 1 to n.
# I used the modulus operator to find even numbers and count their sum.
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
