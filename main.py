import math
#Esto es un comentario de linea

'''
Esto es un comentario de bloque
'''
'''
#SALIDA POR CONSOLA
print("Hola mundo en PYTHON")

#VARIABLES O ENTRADAS
nombreUsuario : str = 'mateo'
edad : int = 20
estatura : float = 1.60
esIngresadoDelcesde : bool = True

#SALIDA
print(nombreUsuario)
print('Buenos dias',nombreUsuario) #La coma es la concatenacion
print(f'Buenos dias {nombreUsuario} con edad {edad}')# Otra forma de concatenacion

#Recibiendo variables desde la consola
num1 = int(input("Digite un numero: "))
print(f"Usted dijito el numero: {num1}")

num2 = int(input("Digite otro numero entero: "))
print(f"Usted digito el numero: {num2}")

suma = num1 + num2
print(f"La suma de {num1} y de {num2} es de: {suma}")

numero : int = 'Mateo'
print(numero)
'''

#menu de opciones

import math


opcion = 1

print("Empanadas el machetico")
print("*********")
print("0 . Salir")
print("1. Encontrar multiplo 2")
print("2. Enocntrar raiz cuadrada")
print("3. sumar +100")
print("4. Elevar a la 12")

while(opcion != 0):
    opcion = int (input("digita una opcion: "))
    if(opcion == 1):
        numero = int(input("Digite un numero: "))
        if(numero %2 == 0 ):
            print(f'El numero {numero} es multiplo de 2')
        else:
            print(f'El numero: {numero} no es multiplo de 2')
    elif(opcion == 2):
        numero = int(input("Digite un numero: "))
        print(f'La raiz cuadrada de {numero} es : {math.sqrt(numero)}')
    elif(opcion == 3):
        numero = int(input("Digite un numero: "))
        print(f'La suma de {numero} + 100 es: {numero + 100}')
    elif(opcion == 4):
        numero = int(input("Digite un numero: "))
        print(f'El cuadrado de {numero} es: {numero * numero}')


else:
    print("para hay")