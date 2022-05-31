
# Clase padre
class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def description(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Residencia: {self.residencia}")
        

# Clase hija
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        # Pasando el metodo init de la clase padre
        super().__init__(nombre, edad, residencia)

        self.salario = salario
        self.antiguedad = antiguedad

    def description(self):
        super().description()
        print(f'Salario: {self.salario}, Antiguedad: {self.antiguedad}')

fabian = Empleado(0, 2, 'Fabian', 23, 'Mexico')
fabian.description()

# Comprobando instancia
print(isinstance(fabian, Persona))