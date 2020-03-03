def latest(scores):
    return scores[-1]


def personal_best(scores):
    max = 0
    for score in scores:
        if score > max:
            max = score
    return max


def personal_top_three(scores):
    list_three = list()
    max = 0
    for iter in range(3):
        max = 0
        for score in scores:
            if score > max:
                max = score
        if max:
            scores.remove(max)
            list_three.append(max)
    return list_three