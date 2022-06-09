def enumeracion(numero: int):
    respuesta = 0

    while respuesta**2 < numero:
        respuesta += 1
        
    if respuesta**2 == numero:
        print(f'La raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no tiene una raiz cuadrada exacta')


def aproximacion(numero: int):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
        respuesta += paso
        
    if abs(respuesta**2 - numero) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {numero}')
    else:
        print(f'La raiz cuadrada de {numero} es {respuesta}')


def busqueda_binaria(numero: int):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, numero)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - numero) >= epsilon:
        if respuesta**2 < numero:
            bajo = respuesta
        else:
            alto = respuesta
            
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {numero} es {respuesta}')
    
    
def main():
    numero = int(input('Ingrese un numero: '))
    print('Ingrese opción de busqueda:')  
    print('(1) Enumeración')
    print('(2) Aproximación')
    print('(3) Busqueda Binaria')
    opcion = int(input(':: '))
    
    if opcion == 1:
        enumeracion(numero)
    elif opcion == 2:
        aproximacion(numero)
    elif opcion == 3:
        busqueda_binaria(numero)
    else:
        print('Opción incorrecta')
        


if __name__ == '__main__':
    main()
