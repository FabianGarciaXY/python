
# Continue
for letra in "Fabian Hernandez Garcia":

    if letra == "h":
        #Ignorando la ultima linea
        continue
    print(f"letra {letra}")


nombre = "Fabian Hernandez Garcia"



counter = 0

for i in nombre:
    counter += 1
    if i == " ":
        continue
print(f"El total de caracteres en el nombre es {counter}")


# Else 
email = input("Email: ")
for i in email:
    if i == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)
