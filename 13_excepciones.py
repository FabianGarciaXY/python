
def divide(num1, num2):
		return num1 + num2


try:
	num1 = int(input("Numero 1: "))
	num2 = int(input("Numero 2: "))
	print(divide(num1, num2))
except ValueError:
	print("No se puede dividir por 0")

print("Programa finalizado")
