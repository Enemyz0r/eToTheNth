import math

def eToNth(integer, number):
    print(round(math.exp(number), integer))

number = int(input("What number? "))
integer=int(input("To how many decimals do you wish to display exponent of {}? ".format(number)))
eToNth(integer, number)
