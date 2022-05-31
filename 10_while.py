import math

print("Programa de calculo de Raiz Cuadrada")

num = int(input("Numero?: "))
intentos = 0

while num < 0: 
    print("No se puede hallar la raiz de un numero negativo")
    if intentos == 2:
        print("Intentos maximos alcanzados")
        break
    num = int(input("Numero?: "))

    if num < 0: 
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(num)
    print(f"La raiz cuadrada de {num} es {solucion}")




edad = int(input("Introduce la edad: "))

while edad < 5 or edad > 100:
    print("Edad incorrecta")
    edad = int(input("Edad :"))
print("La edad es correcta: " + str(edad))



i = 1

while i <= 10:
    print("Ejecución " + str(i))
    i = i + 1

print("Ejecución terminada")
