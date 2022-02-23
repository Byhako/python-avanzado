from datetime import date, datetime

"""
Función que recibe como parametro otra funcion (closure),
le agrega cosas y retorna una funcion diferente.
"""

def decorador(func):
    def wrapper(name):
        # aqui se agrega algo a la funcion
        return func() + f' {name}'
    return wrapper


def saludar():
    return 'Hola'

# Forma no estetica
saludar = decorador(saludar)

# Forma estetica
@decorador
def despedir():
    return 'Adios'


print(saludar('Ruben'))
print(despedir('Ruben'))

# -------------------------------------

def execution_time(func):
    def wrapper(*args, **kwargs):
        init = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time = end - init
        print(f'Duration: {time.total_seconds()} segundos.')
    return wrapper


def execution_time_with_name(name):
    def with_name(func):
        def wrapper(*args, **kwargs):
            init = datetime.now()
            func(*args, **kwargs)
            end = datetime.now()
            time = end - init
            print(f'Duration of {name}: {time.total_seconds()} segundos.')
        return wrapper
    return with_name

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time_with_name('random_func2')
def random_func2():
    for _ in range(1, 1000000):
        pass


random_func()
random_func2()