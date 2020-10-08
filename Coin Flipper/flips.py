def number_of_flips():
    flips = ''

    while type(flips) != int:
        try:
            flips = int(input("How many flips do you want? Please enter a positive integer: "))

        except:
            print("That's not a positive integer.")
            continue

        finally:
            print("Thanks!")

    return flips
