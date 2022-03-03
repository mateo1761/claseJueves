'''
contador = 1
sumatoria = 0

while(contador <= 5):
    contador += 1
    numero = int(input("Digite un numero: "))
    if(numero < 0):
        sumatoria += 1

print(f'La cantidad de numeros negativos es {sumatoria}')
'''

##Ciclo for

##for i in range(1,20,5):
##    print(i)

##trabajos con Arreglos (LISTAS)

nombres = [
    "juan",
    "carlos",
    "marta"
]
print(nombres)

#for para recorrer listas en PY
for nombre in nombres:
    print(nombre)