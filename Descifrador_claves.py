import time
import random
 
def descifrador_claves(clave_cifrada):
    digitos = "0123456789"
    digitos_ordenados = mergesort(list(digitos))  # Ordena los dígitos con mezcla

    for i in digitos_ordenados:
        for j in digitos_ordenados:
            for k in digitos_ordenados:
                # Implementación de búsqueda binaria para el último dígito
                l_index = binary_search(digitos_ordenados, clave_cifrada[3])
                if l_index is not None:
                    posible_clave = i + j + k + digitos_ordenados[l_index]
                    if posible_clave == clave_cifrada:
                        return f"La clave descifrada es {posible_clave}"
                else:
                    break
    return "La clave no pudo ser descifrada."


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    return merge(izquierda, derecha)


def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


def binary_search(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None


# Ejemplo de uso
clave_cifrada = "4937"

start_time = time.time()
resultado = descifrador_claves(clave_cifrada)
end_time = time.time()

print(resultado)
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
