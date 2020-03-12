resultado = 1
AJEDREZ = list()
for i in range(1, 65):
    AJEDREZ.append(resultado)
    resultado = resultado * 2


def square(number):
    if number > 0 and number < 65:
        return AJEDREZ[number-1]
    else:
        raise ValueError("invalid number")


def total():
    return sum(AJEDREZ)
