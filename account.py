class Account:

    def __init__(self):
        self.balance = 1500
        self.first_name = 'Anca'
        self.last_name = 'Calin'
        self.pin = '1234'

    def withdraw(self):

        while True:
            try:
                amount = int(input("What sum do you want to withdraw? "))

            except ValueError:
                print("That's not an integer!")

            else:
                if amount > self.balance:
                    print("Insufficient funds!")

                else:
                    self.balance -= amount
                    print(f"Current balance stands at: {self.balance}")
                    break

    def deposit(self):

        while True:
            try:
                deposit = int(input("What sum do you want to deposit? "))

            except ValueError:
                print("That's not an integer!")

            else:
                if deposit <= 0:
                    print("Please try again!")

                else:
                    self.balance += deposit
                    print(f"Current balance stands at: {self.balance}")
                    break

    def change_pin(self):

        current_pin = ""

        while current_pin != self.pin:

            current_pin = input("What is your PIN? ")

            if current_pin == self.pin:
                new_pin = input("What is your new PIN? ")
                self.pin = new_pin
                print("Your PIN has been updated.")
                break
            else:
                print("That's incorrect. Try again!")
