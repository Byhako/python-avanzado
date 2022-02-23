"""
debemos tener una nested function
la nested function debe referenciar un valor de un scope superior
la función que envuelve la nested debe retornarla también
"""

def make_multiplier(x):
    def multiplier(n):
        return x * n

    return multiplier


def make_division(x):
    assert x != 0, 'No puedes dividir por cero'
    return lambda n : n/x


if __name__ == '__main__':
    times5 = make_multiplier(5)
    times2 = make_multiplier(2)
    divide2 = make_division(2)

    print('cinco veces: ', times5(5))
    print('dos veces: ', times2(5))
    print(divide2(8))