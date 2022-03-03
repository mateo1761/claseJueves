contador = 1
sumatoria = 0

while(contador <= 5):
    contador += 1
    numero = int(input("Digite un numero: "))
    if(numero < 0):
        sumatoria += 1

print(f'La cantidad de numeros negativos es {sumatoria}')