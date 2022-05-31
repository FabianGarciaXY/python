import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f'Se a creado una persona: {self.nombre}')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas:

    personas = []

    def __init__(self):
        lista_de_personas = open("ficheroExterno", "ab+")
        lista_de_personas.seek(0)
        
        try:
            self.personas = pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("Fichero vacio")
        finally:
            lista_de_personas.close()
            del (lista_de_personas)
    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFichero()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFichero(self):
        lista_de_personas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, lista_de_personas)

        lista_de_personas.close()
        del(lista_de_personas)

    def mostrarInformacionFichero(self):
        print("La informacion del ficher externo es: ")
        for p in self.personas:
            print(p)

# Creación del objeto lista
mi_lista = ListaPersonas()
persona = Persona("Ana", "Femenino", 23)
mi_lista.agregarPersonas(persona)
mi_lista.mostrarInformacionFichero()
