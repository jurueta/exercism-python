def classify(number):
    if number > 0:
        suma = sum([i for i in range(1, number) if number % i == 0])
        if suma == number:
            return 'perfect'
        elif suma > number:
            return 'abundant'
        else:
            return 'deficient'
    else:
        raise ValueError("invalid number")
