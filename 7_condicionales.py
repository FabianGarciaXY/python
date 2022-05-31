print("Evaluacion de notas")

nota_alumno = input("Ingresa la nota: ")

def evaluation(note):

	valoration = "Aprobado"
	if note <= 5:
		valoration = "No aprobado"

	return valoration


note = evaluation(int(nota_alumno))
print(note)