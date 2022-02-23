from ast import Try


myList = [1, 2, 3]
myIter = iter(myList)

while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break

# Todo esto es lo mismo que el ciclo for
# pero en python no existe realmente
# solo es azucar sintactica.

for i in myList:
    print(i)

# Creemos un iterador.

class EvenNumbers:
    """
    Clase que implementa un iterador de todos
    los numeros pares o hasta un numero maximo
    """

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):  # dander iter
        self.num = 0
        return self

    def __next__(self):  # dander next
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

