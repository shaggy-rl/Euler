
def ReciprocalCycle(n):
    counter = 1
    remainder = 10 % n

    while remainder != 1:
        remainder = remainder * 10 % n
        counter += 1
    return counter

def LargestCycle(limit):
    maxLength = 0

    for n in range(limit, 3, -1):
        if n % 2 != 0 and n % 5 != 0:
            x = ReciprocalCycle(n);
            if x > maxLength:
                maxNumber = n
                maxLength = x
    print maxNumber

LargestCycle(1000)
