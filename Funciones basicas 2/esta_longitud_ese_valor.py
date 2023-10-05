
def tamanio_y_longitud(lista):
    lista_nueva = []
    cont = 1
    while cont <= lista[0]:
        lista_nueva.append(lista[1])
        cont += 1
    return lista_nueva

print(tamanio_y_longitud([6, 2]))
print(tamanio_y_longitud([4, 7]))