
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


class Furgoneta(Vehiculos):
    
    def cargar(self, carga):
        self.cargado = carga
        if self.cargado:
            return f'La furgoneta esta cargada con {self.cargado}'
        else:
            return 'La furgoneta no esta cargada'


class Moto(Vehiculos):
    derrapa = ''
    def derrapar(self):
        self.derrapa = 'Derrapando la moto'

    def estado(self):
        print(f'Marca: {self.marca}', f'\nModelo: {self.modelo}', f'\nEn marcha: {self.en_marcha}', f'\nAcelera {self.acelera}', f'\nFrena: {self.frena}', f'\nDerrapa: {self.derrapa}')



class VehiculosElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True
  

# Clase con herencia multiple
class BicicletaElectrica(VehiculosElectricos, Vehiculos):
    pass




# Instancia de Vehiculos y Moto
mi_moto = Moto('Honda', 'Ka41')
mi_moto.derrapar()
mi_moto.estado()

# Instancia de Vehiculos y Furgoneta
mi_furgoneta = Furgoneta('Renault', 'Kangg')
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.cargar(True))

# Instancia con multiple herencia de VehiculosElectricos
mi_bici = BicicletaElectrica()













