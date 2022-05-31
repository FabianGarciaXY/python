
#Declaracion
my_list = ["Fabian", "Maria", "Antonio", "Juana"]
print(my_list[:])

# Para acceder a un valor especifico indicamos el indice.
print(my_list[1])
# Accediendo desde el final 
print(my_list[-1])
# Obteniendo una porcion
print(my_list[0:3])


# Append
my_list.append("Test")
print(my_list)

# Extend
my_list.extend(["test2", "test3"])
print(my_list[:])