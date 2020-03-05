CI = {'a': 'z',
      'b': 'y',
      'c': 'x',
      'd': 'w',
      'e': 'v',
      'f': 'u',
      'g': 't',
      'h': 's',
      'i': 'r',
      'j': 'q',
      'k': 'p',
      'l': 'o',
      'm': 'n',
      'n': 'm',
      'o': 'l',
      'p': 'k',
      'q': 'j',
      'r': 'i',
      's': 'h',
      't': 'g',
      'u': 'f',
      'v': 'e',
      'w': 'd',
      'x': 'c',
      'y': 'b',
      'z': 'a'}


def encode(plain_text):
    cifrado = "".join([CI[k] for k in plain_text])
    return ' '.join(cifrado[i:i+5] for i in range(0, len(cifrado), 5))


def decode(ciphered_text):
    new_text = ciphered_text.replace(" ", "")
    descifrado = ""
    for letra in new_text:
        try:
            descifrado += "{}".format(int(letra))
        except Exception:
            for i, j in CI.items():
                if letra == j:
                    descifrado += i
    return descifrado


if __name__ == "__main__":
    print(encode("mindblowingly"))
    print(decode("vcvix1 rhn"))
