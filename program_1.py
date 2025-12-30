# Stored correct credentials
correct_user = "admin"
correct_pass = "1011"

# Maximum allowed attempts(3 attempts total)
max_attempts = 3
attempts = 0

while max_attempts > attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Validation checks:
    # Empty input condition
    if username == "" or password == "":
        print("Username and password cannot be empty.")

    # Correct credentials condition
    elif username == correct_user and password == correct_pass:
        print("Login successful!")
        break

    # Incorrect credentials condition
    else:
        attempts += 1
        print("Invalid username or password.")
        print("Attempts left:", max_attempts - attempts)

# If maximum attempts reached account is locked
if attempts == max_attempts:
    print("Maximum attempts exceeded, Account is locked.")
