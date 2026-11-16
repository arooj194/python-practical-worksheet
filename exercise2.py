# Exercise 2: Shopping Calculator

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 50:
    discount = total * 0.10
    final_amount = total - discount
else:
    final_amount = total

print("Original total: £{:.2f}".format(total))
print("Amount to pay: £{:.2f}".format(final_amount))