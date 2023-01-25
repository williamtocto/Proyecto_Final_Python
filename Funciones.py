
from random import randint
class Funciones:

    def mattriz_nxn(self,n):
        matriz=[]
        print('\nMATRIZ DE: ', n, ' x ', n ,'\n')
        for r in range(n):
            fila=[]
            for c in range (n):
                fila.append(randint(1,100))
            matriz.append(fila)
            print(matriz[r])


    def segunda_mattriz(self,n):
        matriz = [[0 for x in range(n)] for y in range(n)]
        print(matriz)
        valores = input("Ingrese los valores de la matriz, separados por comas: ")
        valores = valores.split(",")
        indice = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                matriz[i][j] = int(valores[indice])
                indice += 1
        for row in matriz:
            print(row)
        return  matriz


    def numero_central(self,matriz):
        # Se asume que matriz es una matriz cuadrada
        n = len(matriz)
        if n % 2 == 1:
            # Si la matriz tiene un número impar de filas/columnas
            centro = matriz[n // 2][n // 2]
            print("El número central de la matriz es:", centro)
        elif(n==0):
            print("Ingrese una matriz desde la Opcion 2")
        else:
            print("La matriz no tiene un número central")


    def matriz_antihorario(self):
        matriz = [[4, 5, 6, 7, 8], [6, 9, 10, 15, 2], [1, 0, 21, 16, 12], [18, 3, 21, 45, 80], [11, 12, 6, 64, 13]]
        # Obtener el tamaño de la matriz
        n = len(matriz)
        # Obtener el centro de la matriz
        x, y = n // 2, n // 2
        # Iniciar la cadena para almacenar los números
        resultado =[]
        # Direcciones para avanzar en sentido antihorario
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Iniciar en la dirección -1 (IZQUIERDA)
        direccion = -1
        # Contador de pasos
        contador = 1
        while True:
            for _ in range(2):
                for _ in range(contador):
                    if (0 <= x < n) and (0 <= y < n) and matriz[x][y] is not None:
                        resultado.append(matriz[x][y])
                        matriz[x][y] = None
                    x += direcciones[direccion][1]
                    y += direcciones[direccion][0]
                direccion = (direccion + 1) % 4
            if contador == n:
                #Finaliza el recorrido de la matriz y termina el bucle
                break
            contador += 1
        # Imprimir el resultado
        print(', '.join(str(i) for i in resultado))

    def matriz_divisores(self):
        matriz = [[4, 5, 6, 7, 8], [6, 9, 10, 15, 2], [1, 0, 21, 16, 12], [18, 3, 21, 45, 80], [11, 12, 6, 64, 13]]
        # Obtener el tamaño de la matriz
        n = len(matriz)
        # Obtener el centro de la matriz
        x, y = n // 2, n // 2
        numero_central=matriz[x][y]
        # Iniciar la cadena para almacenar los números
        divisores = []
        # Direcciones para avanzar en sentido antihorario
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Iniciar en la dirección -1 (IZQUIERDA)
        direccion = -1
        # Contador de pasos
        contador =1
        if(numero_central ==0):
            print("EL numero cero no tiene divisores")
        else:
            while True:
                for _ in range(2):
                    for _ in range(contador):
                        if (0 <= x < n) and (0 <= y < n) and matriz[x][y] is not None:
                            if(matriz[x][y]!=0 and contador>1):
                                if( numero_central % matriz[x][y]==0):
                                    divisores.append(matriz[x][y]) # Aqui se va agregando a la matriz en el caso de que sea divisor del numero central
                            matriz[x][y] = None
                        x += direcciones[direccion][1]
                        y += direcciones[direccion][0]
                    direccion = (direccion + 1) % 4
                if contador == n:# Finaliza el recorrido de la matriz y termina el bucle
                    break
                contador += 1
            # Imprimir el
            print("Los numeros divisores de ",numero_central," son: ")
            print(', '.join(str(i) for i in divisores))

    def matriz_reemplazar_divisores(self):
        matriz = [[4, 5, 6, 7, 8], [6, 9, 10, 15, 2], [1, 0, 21, 16, 12], [18, 3, 21, 45, 80], [11, 12, 6, 64, 13]]
        # Obtener el tamaño de la matriz
        n = len(matriz)
        # Obtener el centro de la matriz
        x= n // 2
        y = n // 2
        numero_central = matriz[x][y]
        contador = 1
        if (numero_central == 0):
            print("EL numero cero no tiene divisores")
        else:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] !=0:
                        if numero_central % matriz[i][j]==0:
                            if i==x and j==y:
                                continue
                            else:
                                matriz[i][j]=int(numero_central/matriz[i][j])
                print(matriz[i])







