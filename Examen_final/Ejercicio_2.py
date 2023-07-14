def crear_fichero():
    file = open("notas.txt", "a+")

    file.close()

    file2 = open("funciones.py", "a+")
    file2.close()

    return file, file2
crear_fichero()