import random as rnd

def busqueda_lineal(lista, objetivo): # O(n)
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [rnd.randint(0, 100) for i in range(1, tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')