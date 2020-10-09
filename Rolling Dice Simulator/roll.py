import random

def roll(n):
    rolls = dict.fromkeys([1,2,3,4,5,6])

    for i in range(1,7):
        rolls[i] = 0

    mean = []
    diff = []

    for i in range(1,n+1):
        roll = random.randrange(1,7)
        values = []

        if roll == 1:
            rolls[1] += 1

        elif roll == 2:
            rolls[2] += 1

        elif roll == 3:
            rolls[3] += 1

        elif roll == 4:
            rolls[4] += 1

        elif roll == 5:
            rolls[5] += 1

        else:
            rolls[6] += 1

        for j in range(1,7):
            values.append(j*rolls[j])

        mean.append(sum(values)/sum(rolls.values()))

    print(f"Mean after {n} trials is {round(mean[-1],3)}.")
    print(f"Diffrence between the mean and the E[X] is {round(abs(mean[-1]-3.5),3)}")

    return rolls
