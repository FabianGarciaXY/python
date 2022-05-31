
# Definicion de clase y propiedades
class Coche:

    # Propiedades
    largo = 250
    ancho = 120
    ruedas = 4
    en_marcha = False

    # Comportamiento
    def arrancar(self, arrancamos):
        self.en_marcha = arrancamos
        
        if self.en_marcha:
            return 'El coche está en marcha'
        else:
            return 'El coche esta parado'


    def estado(self):
        print(f'El coche tiene {self.ruedas} ruedas, un ancho de {self.ancho} y un largo de {self.largo}')




# Instancia 1
coche = Coche()
print(coche.arrancar(True))
coche.estado()


# SEGUNDA INSTANCIA
coche_2 = Coche()
print(coche_2.arrancar(False))
coche_2.estado()