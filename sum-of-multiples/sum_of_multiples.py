def sum_of_multiples(limi, multiples):
    a = [i for j in multiples for i in range(1, limi) if j != 0 and i % j == 0]
    return sum(set(a))
