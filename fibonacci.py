def fibonacci(n: int) -> int:
    """Calcula la secuencia de fibonacci

    Args:
        n (int): numero entero

    Returns:
        int: secuencia de fibonacci
    """
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n -2)



if __name__ == '__main__':
    n = int(input('Ingrese numero: '))
    print(str(fibonacci(n)))
          