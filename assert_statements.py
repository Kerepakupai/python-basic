# assert condicion, mensaje de error

def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
            
    return divisor
        

def main():
    num = input('Ingrese un numero: ')
    assert num.isnumeric(), 'Debes ingresar un numero positivo'
    assert int(num) > 0, 'Debes ingresar numero mayor a cero'
        
    print(divisor(int(num)))
    print('Termino mi programa')


if __name__ == '__main__':
    main()
