def slices(series, length):
    if length > 0 and length <= len(series):
         tam = len(series)
         inico = 0
         siguiente = length
         serie = list()
         while siguiente <= tam:
             serie.append(series[inico:siguiente])
             inico = inico + 1
             siguiente = siguiente + 1
         return serie
    else:
        raise ValueError("El numero es invalido")
    
