import re

def abbreviate(words):
    str_letters = ''
    a = re.findall(r"[^\W_]+'[^\W_]|[^\W_]+", words)
    for i in a:
        str_letters += i[:1].upper()
    return str_letters