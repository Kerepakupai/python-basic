def divisor(num):
    try:
        if num < 0:
            raise ValueError('Debes ingresar un numero positivo')

        divisor = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisor.append(i)
            
        return divisor
    except ValueError as ve:
        print(ve)
        return []
        

def main():
    try:
        num = int(input('Ingrese un numero: '))
        print(divisor(num))
        print('Termino mi programa')
    except ValueError:
        print('debes ingresar un numero')


if __name__ == '__main__':
    main()
