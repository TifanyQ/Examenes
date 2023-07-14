
def funcionDecoradora(*args, **kwargs):

    def funcionInterna(*args):
        print("Antes de la ejecución de la función a decorar")
        resutado = funcionParametro(*args)
        print("Después de la ejecución de la función a decorar")
        return resutado
    return  funcionInterna

@funcionDecoradora
def mult(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(suma(10, 25, 10, 40, 30))