def heads_tails(N):
    import random

    tosses = []

    for i in range(N):
        if random.randint(0,1) == 0:
            tosses.append(0)

        else:
            tosses.append(1)

    return tosses
