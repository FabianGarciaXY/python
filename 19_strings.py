edad = input('Edad: ')


while edad.isdigit() == False:
    print('Introduce un valor numerico')
    edad= input("Edad: ")


if int(edad) < 18:
    print("No puede pasar")
else:
    print("Adelante")
