def equilateral(sides):
    if 0 not in sides and suma_lados(sides):
        return len(set(sides)) == 1
    else:
        return False


def isosceles(sides):
    if 0 not in sides and suma_lados(sides):
        return len(set(sides)) == 2 or len(set(sides)) == 1
    else:
        return False


def scalene(sides):
    if 0 not in sides and suma_lados(sides):
        return len(set(sides)) == 3
    else:
        return False


def suma_lados(sides):
    valor = True
    if (sides[0] + sides[1]) < sides[2]:
        valor = False
    elif (sides[1] + sides[2]) < sides[0]:
        valor = False
    elif (sides[0] + sides[2]) < sides[1]:
        valor = False
    return valor
