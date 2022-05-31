
# AND - OR
print('*** Programa de becas 2021 ****')

distancia_escuela = int(input("Distancia a la escuela: "))
num_hermanos = int(input("Numero de hermanos: "))
salario_fam = int(input("Salario familiar: "))

if distancia_escuela > 40 and num_hermanos >= 2 or salario_fam < 20000:
    print("Beca concedida")
else:
    print("No aplica")


# IN 
print("<< Asignaturas optativas 2021 >>")
print("Inf. Grafica, Pruebas de Software, Usabilidad y Accesibilidad")

opcion = input("Escribe la Asignatura: ")
asignatura = opcion.lower()

if asignatura in ("ing. grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura escugida: " + asignatura)
else:
    print("Asignatura NO existente")