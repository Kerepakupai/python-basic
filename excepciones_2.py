def palindromo(string):
    if len(string) == 0:
        raise ValueError('No se puede ingresar una cadena vacia')
       
    return string == string[::-1]
            
    
    

def main():
    try:
        string = input('Ingrese palabra: ')
        print(palindromo(string))
    except TypeError:
        print('Solo se puden ingresar cadenas de texto')
    except ValueError as ve:
        print('Error ingresando dato', ve) 
    finally:
        print('Manejo de Excepciones')

if __name__ == '__main__':
    main()
