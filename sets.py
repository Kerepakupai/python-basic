# SETS: Una coleccion desordenada de elementos unicos e inmutables

my_set = {3, 4, 5}
print(f"my_set = {my_set}")

my_set2 = {"Hola", 23.3, False, True}
print(f"my_set2 = {my_set2}")

my_set3 = {3, 3, 2}
print(f"my_set3 = {my_set3}")

my_set4 = {(1, 2, 3), 4}
print(f"my_set4 = {my_set4}")

empty_set = set()
print(type(empty_set))

my_set = {1, 2, 3}
print(my_set)

# Añadir un elemento
my_set.add(4)
print(my_set)

# Añadir multiples elementos
my_set.update([1, 2, 5])
print(my_set)

# Añadir multiples elememtos
my_set.update((1, 7, 2), {6, 8})
print(my_set)

# Borrar un elemento existente
my_set.discard(1)
print(my_set)

# Borrar un elemento existente
my_set.remove(2)
print(my_set)

# Borrar un elemento inexistente
my_set.discard(10)
print(my_set)

# Borrar un elemento inexistente
# KeyError => Diferencia
# my_set.remove(12)
print(my_set)

# Borrar elemento aleatorio
my_set.pop()
print(my_set)

# limpiar el set
my_set.clear()
print(my_set)


# Operaciones con Sets
# Union: Combinar todos los elementos de los conjuntos
print("UNION")
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set1 | my_set2
print(my_set3)

# Interseccion: Combinarlos los conjuntos pero solo obtener los que coinciden en ambos
print("INTERSECCION")
my_set1 = {3, 4, 5}
my_set2 = {4, 5, 6}
my_set3 = my_set1 & my_set2
print(my_set3)

# Diferencia: Resultado de tomar dos sets y de uno quitar todos los elementos que tenian el set 1
print("DIFERENCIA")
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set1 - my_set2
print(my_set3)
my_set3 = my_set2 - my_set1
print(my_set3)

# Diferencia Simetrica: Los elementos que no se comparten
print("DIFERENCIA SIMETRICA")
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set1 ^ my_set2
print(my_set3)

# set1.union(set2)
# set1.symmetric_difference(set2)
# set1.difference(set2)
# set1.intersection(set2)


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


if __name__ == '__main__':
    my_list = [1, 1, 3, 3, 4]
    print(remove_duplicates(my_list))
    print(remove_duplicates_with_sets(my_list))
