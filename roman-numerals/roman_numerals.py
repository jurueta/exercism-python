ROMAN_NUMBER = {'M': 1000,
                'CM': 900,
                'D': 500,
                'CD': 400,
                'C': 100,
                'XC': 90,
                'L': 50,
                'XL': 40,
                'X': 10,
                'IX': 9,
                'V': 5,
                'IV': 4,
                'I': 1}


def roman(number):
    if not isinstance(number, int):
        raise TypeError('Numero invalido')
    for i, j in ROMAN_NUMBER.items():
        if number >= j:
            result = i
            number -= j
            break
    if number > 0:
        result += roman(number)
    return result
