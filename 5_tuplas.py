
my_tuple = ("Fabian", "test", 2, 0)

# Tupla a lista
my_list = list(my_tuple)
print(my_list)

# Lista a tupla
my_new_tuple = tuple(my_list)
print(my_new_tuple)

# in
print("Fabian" in my_new_tuple)

#Count
print(my_new_tuple.count("Fabian"))

# Len()
print(len(my_new_tuple))