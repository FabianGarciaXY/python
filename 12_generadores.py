
# Generador
def generador(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1



pares = generador(10)

print(next(pares))

print("Some random code")

print(next(pares))
print(next(pares))

print("**************************************")
for i in pares:
    print(i)



# YIELD FROM
def return_cities(*cities):
    for element in cities:
        yield from element

cities = return_cities("Mty", "CDMX", "Madrid", "Barcelona")
print(next(cities))
print(next(cities))

