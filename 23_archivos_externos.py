from io import open


# Creacion y manipulacion de archivos
# archivo_text = open('texto.txt', 'w')

# frase = "test test test \n test test test"
# archivo_text.write(frase)
# archivo_text.close()


# Lectura de texto
archivo_text = open("texto.txt", "r")
texto = archivo_text.read()
archivo_text.close()

print(texto)
