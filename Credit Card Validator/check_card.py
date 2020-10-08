from bigger10 import bigger_10

def check_card(digits):
    check_sum = [int(digits[-1])]
    digits = digits[::-1]
    for i in range(1,len(digits)):
        if i%2 == 1:
            check_sum.append(bigger_10(2*int(digits[i])))

        else:
            check_sum.append(int(digits[i]))

    if sum(check_sum)%10 == 0:
        print("The card is valid!")

    else:
        print("The card is not valid!")
