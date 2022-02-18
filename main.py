#Esto es un comentario de linea

'''
Esto es un comentario de bloque
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