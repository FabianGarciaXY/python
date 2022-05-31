
# For con listas
for dias in ["lunes", "martes", "miercoles", "jueves"]:
    print(f"Hola {dias}")

# Print(end)
for i in ['a', 'b', 'c']:
    print('hola', end=' ')
print('\n')

# Tipo Range
# Este permite mas argumentos, como un segundo valor para indicar que rango (excuido), de que valor a que valor.
# El tercer argumento indica de cuanto en cuanto recorrer la lista
for i in range(5, 50, 3):
    print(f"valor de la variable {i}")


# For con condicionales y Strings
myemail = input('Ingresa el email: ')
counter = 0

for i in myemail:
    if i == '@' or i == '.':
        email = True
        counter = counter + 1

if counter >= 2:
    print('Email Correcto')
else:
    print('Email Incorrecto')