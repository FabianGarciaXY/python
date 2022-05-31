
# DICCIONARIOS

my_dictionary = {"Mexico": "DF", "Francia":"Paris", "Reino Unido": "Londres"}
print(my_dictionary["Mexico"])

# Añadir
my_dictionary["Italia"] = "Lisboa"

# Modificar
my_dictionary["Italia"] = "Roma"
print(my_dictionary)

# Eliminar
del my_dictionary["Italia"]
print(my_dictionary)

# Distintos tipos
new_dic = {"Alemania": "Berlin", 23: "Jordan", "mosqueteros": 3}
print(new_dic)

# Diccionario a partir de tupla
my_tuple = ("Mexico", "España", "UK")
my_dic = {my_tuple[0]:"DC", my_tuple[1]: "Madrid", my_tuple[2]:"London"}
print(my_dic)

# Tupla dentro de un diccionario
dictionary = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1997, 1998]}
print(dictionary)
print(dictionary["Anillos"])

# keys()
print(dictionary.keys())

# values()
print(dictionary.values())

#len()
print(len(dictionary))