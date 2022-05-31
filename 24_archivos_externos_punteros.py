from io import open

archivo = open('texto.txt', 'r+')
print(archivo.read())

archivo.seek(0)
archivo.writelines("Title")
archivo.seek(0)
print(archivo.read())
