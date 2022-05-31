
# Constructor
class Coche:
    
    def __init__(self):
        # Encapsulacion
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__enmarcha = False


    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if self.__enmarcha:
            chequeo = self.__chequeo_coche()
        if self.__enmarcha and chequeo:
            return 'El coche esta en marcha'
        elif self.__enmarcha and chequeo == False:
            return 'El coche no esta listo'
        else:
            return 'El coche esta parado'


    def estato(self):
        print('El coche tiene ', self.__ruedas, 'ruedas, un ancho de ', self.__ancho, 'y un largo de ', self.__largo)
    

    def __chequeo_coche(self):
        print('Realizando un chequeo')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'
        
        if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False


mi_coche = Coche()
print(mi_coche.arrancar(True))
mi_coche.estato()
