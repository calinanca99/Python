def get_card():
    """
    Gets the number of the card, creates a list with all the digits and reverses the order. The card number must have length 16.
    """
    num = input("Insert card number: ")
    digits = []
    for i in num:
        digits.append(i)

    return digits
