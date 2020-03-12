def is_paired(input_string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    lista = list()
    for i in input_string:
        if i in open_list:
            lista.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(lista) > 0) and (open_list[pos] == lista[len(lista)-1])):
                lista.pop()
            else:
                return False
    return len(lista) == 0
