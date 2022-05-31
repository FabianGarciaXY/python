from io import open
import pickle

## ---------- DUMP o guardado --------------

# lista = ["Fabian", "Sandra", "Ana", "Juan"]
##  Creacion del fichero
# fichero_binario = open("lista_nombres", "wb")

##  Volcado de datos
##  Recibe 2 parametros: Informacion, fichero
# pickle.dump(lista, fichero_binario)
# fichero_binario.close()
# del (fichero_binario)


# ----------- LOAD o carga ------------
# Creacion del fichero binaro a partir de lectura
fichero_binario = open('lista_nombres', 'rb')

# creación de lista del fichero cargado
mi_lista = pickle.load(fichero_binario)
fichero_binario.close()
print(mi_lista)
