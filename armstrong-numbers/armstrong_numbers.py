def is_armstrong_number(number):
    return sum(pow(int(i), len(str(number))) for i in str(number)) == number
