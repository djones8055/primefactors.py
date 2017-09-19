""" Program that gives me all the factors and then all the prime factors
    of a number """

NUM = int(input("What number do you want to find the factors of: "))
FACTORS = []

for i in range(1, NUM +1):
    if (NUM / i).is_integer():
        print(i, " is a factor")
        FACTORS.append(i)

for i in FACTORS[1:]:
    PRIME = True
    for x in range(2, i):
        if i % x == 0:
            PRIME = False
    if PRIME:
        print(i, " is a prime factor")
