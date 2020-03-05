def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        dist = 0
        for i, j in zip(strand_a, strand_b):
            if i != j:
                dist += 1
        return dist
    else:
        raise ValueError("Los tamanos son invalidos")
