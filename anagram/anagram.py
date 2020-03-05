def find_anagrams(word, candidates):
    resultado = list()
    for letra in candidates:
        if(letra.lower() != word.lower()) and (len(letra) == len(word)):
            cant = 0
            new_word = word
            for i in letra.lower():
                if i in new_word.lower():
                    cant += 1
                    new_word = new_word.replace(i, "", 1)
            if cant == len(word):
                resultado.append(letra)
    return resultado
