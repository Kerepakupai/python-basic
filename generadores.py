# Funciones que guardan un estado "sugar syntax de los iteradores"
# Ventajas - Es mas facil de escribir
#          - Todas las ventajas de un Iterador

from time import sleep

def my_gen():
    """Un ejemplo de generadores"""
    print("Hello world!")
    n = 0
    # yield = return pero pausa la funcion
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n


def back():
    a = my_gen()
    print(next(a))
    print(next(a))
    print(next(a))
    # StopIteration
    # print(next(a))

    # Generator expression
    my_list = [0, 1, 2, 4, 7, 9, 10]

    my_second_list = [x*2 for x in my_list] # List comprehencion
    my_second_gen = (x*2 for x in my_list)  # Generator expression

    print(type(my_second_gen))
    print(type(my_second_list))


def fibo_gen(num_max=0):
    n1 = 0
    n2 = 1
    aux = 0
    counter = 0
    while num_max > aux:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    limit = input("Ingrese el numero limite: ")
    try:
        assert limit.isnumeric(), "Debes ingresar un numero"
        fibonacci = fibo_gen(int(limit))
        for element in fibonacci:
            print(element)
            sleep(0.5)
    except AssertionError as ae:
        print(f'ERROR::{ae}')
