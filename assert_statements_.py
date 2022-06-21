def primera_letra(lista_palabras):
    primeras_letras = []
    
    try:
        for palabra in lista_palabras:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, f'No se permiten str vacios'
            
            primeras_letras.append(palabra[0])
    except AssertionError as e:
        print(e)
             
    return primeras_letras


if __name__ == '__main__':
    lista_palabras = ['Hola', '', 'desde', 'Python']
    print(primera_letra(lista_palabras))
