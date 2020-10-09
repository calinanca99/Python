from roll import *

while True:
    while True:
        try:
            inpt = int(input("How many rolls?: "))

        except ValueError:
            print("Please enter an integer!")
            continue

        if inpt <= 0:
            print("Please enter a positive integer!")
            continue

        else:
            break

    roll(inpt)

    if input("Try again? (Y)es or (N)o: ").lower()[0] == 'y':
        continue

    else:
        print("Bye!")
        break
