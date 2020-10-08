def bigger_10(num):
    """
    The function deals with the numbers that when doubled are higher than 10.
    """
    if num >= 10:
        num = num//10+num%10

    return num
