def convert(number):
    factores = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    gotas = "".join(j for i, j in factores.items() if number % i == 0)
    return gotas if gotas else str(number)
