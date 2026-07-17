# ---------------- LOGIN AUTHENTICATION ----------------

USERNAME = "geethu"
PASSWORD = "geethu143"

print("=" * 50)
print("        BANK MANAGEMENT SYSTEM")
print("=" * 50)

attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!\n")
        break
    else:
        attempts -= 1
        print("Invalid Username or Password.")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Access Denied!")
    exit()

# ---------------- BANK DATABASE ----------------

accounts = {}

while True:

    print("\n========== BANK MENU ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Create Account
    if choice == "1":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account already exists!")

        else:
            name = input("Enter Customer Name: ")
            balance = float(input("Enter Initial Deposit: "))

            accounts[acc_no] = {
                "Name": name,
                "Balance": balance
            }

            print("Account Created Successfully!")

    # Deposit
    elif choice == "2":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            amount = float(input("Enter Deposit Amount: "))
            accounts[acc_no]["Balance"] += amount

            print("Money Deposited Successfully!")

        else:
            print("Account Not Found!")

    # Withdraw
    elif choice == "3":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            amount = float(input("Enter Withdrawal Amount: "))

            if amount <= accounts[acc_no]["Balance"]:
                accounts[acc_no]["Balance"] -= amount
                print("Withdrawal Successful!")
            else:
                print("Insufficient Balance!")

        else:
            print("Account Not Found!")

    # Check Balance
    elif choice == "4":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            print("\nCustomer Name :", accounts[acc_no]["Name"])
            print("Available Balance :", accounts[acc_no]["Balance"])

        else:
            print("Account Not Found!")

    # View All Accounts
    elif choice == "5":

        if len(accounts) == 0:
            print("No Accounts Available!")

        else:

            print("\n========== ACCOUNT DETAILS ==========")

            for acc_no, details in accounts.items():

                print("Account Number :", acc_no)
                print("Customer Name  :", details["Name"])
                print("Balance        :", details["Balance"])
                print("-" * 35)

    # Exit
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")