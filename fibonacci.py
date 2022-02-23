from re import A
import time

# Iterador
class FiboIter():
    def __init__(self, terminos):
        self.terminos = terminos

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count == self.terminos:
            raise StopIteration
        else:
            if self.count == 0:
                self.count += 1
                return self.n1
            elif self.count == 1:
                self.count += 1
                return self.n2
            else:
                aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, aux
                del(aux)
                self.count += 1
                return self.n2

# Generador
def fiboGen(max=None):
    n1, n2, count = 0, 1, 0
    while not max or max > count:
        count += 1
        yield n1
        n1, n2 = n2, n1 + n2



if __name__ == '__main__':
    terminos = input('Cuantos terminos deseas? ')
    assert terminos.isnumeric() and int(terminos)>0, 'Debes ingresar un numero entero mayor a cero.'
    # fibo = FiboIter(int(terminos))
    # for num in fibo:
    #     print(num)
    #     time.sleep(0.2)

    fibo = fiboGen(int(terminos))
    for element in fibo:
        print(element)
        time.sleep(0.2)
