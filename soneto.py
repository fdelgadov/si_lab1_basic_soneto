caracter_sustituto = {
    'a': 'u',
    'h': 't',
    'ñ': 'e',
    'k': 'l',
    'v': 'f',
    'w': 'b',
    'z': 'y',
    'r': 'p'
}

tildes_vocales = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U'
}

signos = [' ', ',', '.', ';']

def sustituciones(txt):
    aux = txt
    for k, v in caracter_sustituto.items():
        aux = aux.replace(k, v)
        aux = aux.replace(chr(ord(k) - 32), chr(ord(v) - 32))

    return aux

def eliminar_tildes(txt):
    aux = txt
    for k, v in tildes_vocales.items():
        aux = aux.replace(k, v)
    return aux

def a_mayuscula(txt):
    aux = txt

    for x in range(97, 123):
        aux = aux.replace(chr(x), chr(x - 32))

    return aux

def eliminar_signos(txt):
    aux = txt

    for c in signos:
        aux = aux.replace(c, '')

    return aux

def preprocesamiento(texto):
    res = texto
    res = sustituciones(res)
    res = eliminar_tildes(res)
    res = a_mayuscula(res)
    res = eliminar_signos(res)

    return res

def main():
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

main()