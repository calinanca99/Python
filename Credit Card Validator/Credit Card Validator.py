from check_card import check_card
from get_card import get_card


print("----------CREDIT CARD VALIDATOR----------")


while True:
    my_card = []
    while len(my_card) != 16:
        my_card = get_card()
        if len(my_card) == 16:
            print("Thank you!")
            break

        else:
            print("The length of the card number must be 16!")
            continue

    check_card(my_card)

    ans = input("Do you want to check another card? (Y)es or (N)o: ")
    if ans.lower()[0] == "y":
        continue

    else:
        print("Bye!")
        break
