import random

"Ejercicio_1"

lista = []
while len(lista) < 10:
    numero = random.randint(0, 100)
    lista.append(numero)
print('Lista con los números aleatorios: {}'.format(lista))
def lista_no_repetidos(lista):
    lista_actualizada = list(set(lista))
    return lista_actualizada

lista_actualizada = lista_no_repetidos(lista)
print('Lista sin repetición: {}'.format(lista_actualizada))
def orden():
    lista_actualizada.sort()
    listaa = lista_actualizada.copy()
    listaa.reverse()
    return lista_actualizada, listaa

orden()
print('Nueva lista y su reversa: {}'. format(orden()))

def mayor(lista_actualizada):
    valor = max(lista_actualizada)
    return valor

mayor(lista_actualizada)
print('El mayor valor es: {}'.format(mayor(lista_actualizada)))