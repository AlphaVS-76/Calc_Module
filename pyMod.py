def adder():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    sum = a + b
    print("The sum is:", sum)


def subtracter():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    diff = a - b
    print("The difference is:", diff)


def multiplier():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    mult = a * b
    print("The product is:", mult)


def divider():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if b == 0:
        print("Denominator should not be 0")
    else:
        div = a / b
        print("The result is:", div)


def modder():
    print("\n\t\tDISCLAIMER: Try not to go beyond 22\n")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    mod = a % b
    print("The sum is:", mod)


def power():
    a = int(input("Enter the base number: "))
    b = int(input("Enter number to be raised: "))

    raiser = a ** b
    print("The result is:", raiser)