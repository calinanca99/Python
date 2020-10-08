from account import Account
from func_choose import choose_option

account = Account()

print(f"Welcome to the ATM, Mr. {account.first_name}!")
print("How can I help you today?")

while True:
    print("\n1.Check account.\n2.Deposit.\n3.Withdrawal\n4.Change PIN.")

    option = choose_option()

    if option == 1:
        print(f"Your balance stands at: {account.balance}")

    elif option == 2:
        current_pin = ""

        while current_pin != account.pin:
            current_pin = input("What is your PIN? ")

            if current_pin == account.pin:
                account.deposit()

            else:
                print("Try again.")
                continue

    elif option == 3:
        current_pin = ""

        while current_pin != account.pin:
            current_pin = input("What is your PIN? ")

            if current_pin == account.pin:
                account.withdraw()

            else:
                print("Try again.")
                continue

    elif option == 4:
        account.change_pin()

    anything_else = input(f"Anything else, Mr. {account.last_name}? ")

    if anything_else.lower()[0] == "y":
        continue

    else:
        print("Have a good day!")
        break
