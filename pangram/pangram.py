def is_pangram(sentence):
    return len(set([x for x in sentence.lower() if x.isalpha()])) == 26
