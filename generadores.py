# Suggar syntax para los iteradores.

my_list = [1, 2, 3, 4]

# Guarda todo en ram
second_list = [x**2 for x in my_list]

# Se genera cada elemento al ser necesitado
second_generator = (x**2 for x in my_list)
