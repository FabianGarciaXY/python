class Coche():
    def desplazamiento(self):
        print("Desplazamiento a 4 ruedas")

class Moto():
    def desplazamiento(self):
        print('Desplazamiento a 2 ruedas')

class Camion():
    def desplazamiento(self):
        print('Desplazamiento a 6 ruedas')



def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

mi_vehiculo=Camion()
desplazamiento_vehiculo(mi_vehiculo)
