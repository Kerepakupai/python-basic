import random as rnd

def ordenamiento_de_burbuja(lista): # O(n ** 2)
    n = len(lista)

    for i in range(n):  # O(n)
        for j in range(n - i - 1): # O(n)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista
    


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [rnd.randint(0, tamano_de_lista) for i in range(1, tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)