import pickle

class Vehiculos:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.en_marcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca}', f'\nModelo: {self.modelo}', f'\nEn marcha: {self.en_marcha}', f'\nAcelera {self.acelera}', f'\nFrena: {self.frena}')



coche1 = Vehiculos('Mazda', 'MX5')
coche2 = Vehiculos('Seat', 'Leon')
coche3 = Vehiculos('Renault', 'Megane')

coches = [coche1, coche2, coche3]

# Creación del fichero
fichero = open('coches', 'wb')
pickle.dump(coches, fichero)
fichero.close()
del (fichero) 


# Carga del fichero ya creado a variables python
fichero_apertura = open('coches', 'rb')
lista_coches = pickle.load(fichero_apertura)

# Cerrado del fichero en memoria
fichero_apertura.close()

# Imprimir la lista de objetos
for object in lista_coches:
    object.estado()


