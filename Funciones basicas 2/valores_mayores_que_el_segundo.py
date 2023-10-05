
def valores_mayores_al_segundo(lista):

    if len(lista) < 2:
        return False
    
    nueva_lista = []
    for valor in lista:
        if valor > lista[1]:
            nueva_lista.append(valor)
    print(f"Son{len(nueva_lista)} valores mayores al segundo que es {lista[1]}")
    return nueva_lista

print(valores_mayores_al_segundo([5, 2, 3, 2, 1, 4]))
print(valores_mayores_al_segundo([5]))