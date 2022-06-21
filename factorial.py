def factorial(n: int) -> int:
    """Calcula el factorial de n.

    Args:
        n (int) > 0:
        returns n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n - 1)



if __name__ == '__main__':
    n = int(input('Ingresa un numero entero: '))
    print(str(factorial(n)))

