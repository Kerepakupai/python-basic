paises = {'venezuela': 1, 'colombia': 2, 'chile': 3, 'usa': 4, 'madrid': 5}

def busca_pais(pais: str)->int:
    try:
        return paises[pais]
    except KeyError:
        return None


if __name__ == '__main__':
    pais = 'colombia'
    print(busca_pais(pais))
