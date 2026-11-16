
#Password Attempts

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password.")
        print("Attempts remaining:", max_attempts - attempts)

if attempts == max_attempts and password != correct_password:
    print("Access denied!")
