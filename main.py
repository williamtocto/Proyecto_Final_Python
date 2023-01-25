from Funciones import Funciones


class Principal:
        a=0
        matriz = []
        while(a!=7):
            obj = Funciones()
            # menu de Ingreso de Enunciado
            print("=================================================================================================================================")

            print('\n1. Crear una matriz Cuadrada de nxn')
            print('2. Matriz de numeros enteros')
            print('3. Numero Central de la Matriz')
            print('4. Matriz Antihorario desde el centro')
            print('5. Divisores del numero Central de la matriz')
            print('6. Reemplazar lod dividores de la matriz')
            print('7. Salir')

            a = int(input("\nIngrese un numero para relizar una Operacion: "))
            if a == 1:
                n = 0
                while (n % 2 != 1 or n<=3):
                    n = int(input("Ingrese el tamaño de la matriz:  "))
                    if(n % 2 !=1):
                        print('ERROR: Debe ser un Numero Impar, Ingrese Nuevamente')
                    elif(n<3):
                        print('ERROR: El numero debe ser Mayor a 3')
                    else:
                        obj.mattriz_nxn(n)
            if a==2:
                n = int(input("Ingrese el tamaño de la matriz:  "))
                matriz=obj.segunda_mattriz(n)
            if a==3:
                obj.numero_central(matriz)
            if a==4:
                obj.matriz_antihorario()
            if a==5:
                obj.matriz_divisores()
            if a==6:
                obj.matriz_reemplazar_divisores()
            if a==7:
                print('\n!Ha finalizado Gracias!')

