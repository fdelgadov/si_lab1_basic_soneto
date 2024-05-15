from preprocesamiento import *

nombre_archivo = "soneto"
with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
    txt = archivo.read()

print(txt)
txt = sustituciones(txt)
print(txt)
txt = eliminar_tildes(txt)
print(txt)
txt = a_mayuscula(txt)
print(txt)
txt = eliminar_signos(txt)
print(txt)

with open("PRACTICA1_PRE.TXT", "w", encoding="utf-8") as archivo:
    archivo.write(txt)