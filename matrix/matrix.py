class Matrix:
    def __init__(self, matrix_string):
        self.filas = (matrix_string.split("\n"))
        self.matFil = list()
        self.columnas = list()
        
        for i in self.filas:
            self.matFil.append(list(map(int, i.split(" "))))

        for i in range(len(self.matFil[0])):
            colum = list()
            for col in self.matFil:
                colum.append(col[i])
            self.columnas.append(colum)

    def row(self, index):
        return self.matFil[index-1]

    def column(self, index):
        return self.columnas[index-1]
