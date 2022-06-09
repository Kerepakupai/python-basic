from json.tool import main


def main():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 5458544155411,
        'Colombia': 54212366
    }
    for pais in poblacion_paises.keys():
        print(pais);
    
    for pais in poblacion_paises.values():
        print(pais);
    
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    main()
