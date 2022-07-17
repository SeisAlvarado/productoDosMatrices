"""
Created on Fri Mar 25 09:31:45 2022

@author: José Luis Márquez Alvarado
Date: 25-03-2022
Descripción: Producto punto de 2 matrices 
"""

class ProductoPunto:
    matrizA   = []
    matrizB   = []
    matrizC   = []
    filasA    = 0
    columnasB = 0
    
    def __init__(self)->None:
        self.filasA    = int(input("¿Cuántas filas tiene su matríz A?: "    ))
        self.columnasB = int(input("¿Cuántas Columnas tiene sus matríz B?: "))


        if self.filasA == self.columnasB:
            #hacer matriz
            self.matrizA = self.solicitarDatos(self.filasA   )
            print("----------------------------------------" )
            self.matrizB = self.solicitarDatos(self.columnasB)
            print("----------------Matríz A----------------" )
            for fila in self.matrizA:
                print(fila)
            
            print("")
            print("----------------Matríz B----------------")
            for fila in self.matrizB:
                print(fila)
            print("--------------Matríz A * B--------------")

            self.multiplicarMatrices()
            for fila in self.matrizC:
                print(fila)
        else:
            print("Estas matrices no pueden multiplicarse... ")

    def multiplicarMatrices(self)->None:
        aux = []
        funcion = 0
        for filaA in range(self.filasA):
            for columnaB in range(self.columnasB):
                for columnaA in range(self.filasA):
                    funcion += self.matrizA[filaA][columnaA] * self.matrizB[columnaA][columnaB]

                aux.append(funcion)
                funcion = 0
            self.matrizC.append(aux)
            aux = []
        
    def solicitarDatos(self, longitudMatriz):
        matriz    = []
        matrizAux = []
        aux    = 0
        for elementoFila in range(longitudMatriz):
            for elementoCol in range(longitudMatriz):
                aux = float(input(f"({elementoFila},{elementoCol}): "))
                matrizAux.append(aux)
            matriz.append(matrizAux)
            matrizAux = []
        return matriz


objProductoPunto = ProductoPunto()