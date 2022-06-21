objetivo = int(input('Ingrese un numero entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
    
if respuesta**2 == objetivo:
    print('La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print('{objetivo} no tiene una raiz cuadrada exacta')

