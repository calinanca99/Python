def choose_option():

    option = 0
    while option not in [1,2,3,4]:

        option = int(input("Please choose: "))

        if option not in [1,2,3,4]:
            print("That's not available. Please try again.")
            continue

    return option
