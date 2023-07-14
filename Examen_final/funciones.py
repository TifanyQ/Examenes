import math

lista = []
lista2 = []
def tamaño_lista():
    x = int(input('Ingresa el tamaño de la lista: '))
    while len(lista) < x:
        numero = int(input('Ingresa {} números: '.format(x)))
        lista.append(numero)
        lista_nueva = str(lista)
        file_numeros = open("notas.txt", "w")
        file_numeros.writelines(lista_nueva)
        file_numeros.close()
    return lista

tamaño_lista()
print('Su lista es {}'.format(lista))

lista_raiz = []

def raiz_cuadrada():
    for x in lista:
        raiz = math.sqrt(x)
        lista_raiz.append(raiz)
        lista_2 = str(lista_raiz)
        file_numeros2 = open("notas.txt", "w")
        file_numeros2.writelines(lista_2)
        file_numeros2.close()

raiz_cuadrada()
