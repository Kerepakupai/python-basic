# Protocolo: tenemos que tener una clase que contenga los metodos __iter__ y __next__
# Ventajas: - Ahorro de recursos
#           - Ocupan menos espacio
#           - Mas rapido
import time

class EvenNumbers:
    """Clase que implementa un iterador de todos los numeros pares, o los numeros pares hasta un maximo"""

    def __init__(self, max_number=None):
        self.max = max_number

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


# La sucesion de Fibonacci
class FiboIter:

    def __init__(self, num_max=None):
        self.max = num_max
        self.aux = 0

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.aux < self.max or not self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


if __name__ == '__main__':
    fibo = FiboIter(50)
    for num in fibo:
        print(num)
        time.sleep(0.5)
