# Addition function
def add(*args):
    """
    Takes in any number of integer arguments, adds them, and returns the total.
    """
    total = 0
    for num in args:
        total += num

    return total


# Subtraction function
def sub(*args):
    """
    Takes in any number of integer arguments, subtracts them, and returns the total.
    **Anti-commutative - order of arguments matter.**
    """
    total = args[0]
    for num in args[1:-1]:
        total -= num

    return total


# Multiplication function
def mult(*args):
    """
    Takes in any number of integer arguments, multiplies them, and returns the product.
    """
    product = 1
    for num in args:
        product *= num

    return product


# Division function
def div(*args):
    """
    Takes in any number of integer arguments, divides them, and returns the quotient.
    **Anti-commutative - order of arguments matter.**
    """
    quotient = args[0]
    for num in args[1:-1]:
        quotient /= num

    return quotient


# Exponential function
def exp(x, n):
    """
    Takes in two argument, `x` and `n`, and returns `x` raised to the `n`-th power.
    """
    return x ** n
