from heads_tails import heads_tails
from flips import number_of_flips

print("Welcome to the tossing game!")

while True:
    N = number_of_flips()
    tosses = heads_tails(N)
    heads = sum(tosses)
    tails = N - heads

    print("You've got {} ({}%) heads and {} ({}%) tails!".format(heads, round(heads/N*100,2), tails, round(tails/N*100,2)))

    play_again = input("Do you want to play again? ")

    if play_again.lower()[0] == "y":
        print("Cool!")
        continue
    else:
        print("Thanks for playing.")
        break
