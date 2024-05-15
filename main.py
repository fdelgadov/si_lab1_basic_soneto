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
print(f"{txt}\nLongitud: {len(txt)}")

archivo_destino = "PRACTICA1_PRE.TXT"
with open(archivo_destino, "w", encoding="utf-8") as archivo:
    archivo.write(txt)

tabla_frecuencias = frecuencias(archivo_destino)

with open(archivo_destino, 'r', encoding="utf-8") as archivo:
    secuencias = secuencias_repetidas(archivo.read())
    distancias = calcular_distancias(secuencias)
print(f"{tabla_frecuencias}\n\n{secuencias}\n\n{distancias}")

with open(archivo_destino, 'r', encoding="utf-8") as archivo:
    txt = archivo.read()

print(a_unicode(txt))
print(otra_sustitucion(txt))
print(insertar_epis(txt))