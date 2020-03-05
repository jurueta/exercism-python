def is_isogram(string):
    string = string.lower().replace(" ","").replace("-","")
    return len(string) == len(set(string))