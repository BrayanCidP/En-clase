"""
Cuenta regresiva: Crea una funcion que acepte un numero como entrada.
Devuelve una lista nueva que cuente de uno en uno, desde el numero(como elemento 0)
hasta 08como ultimo elemento).

Ejemplo; countdown(5) deberia devolver [5,4,3,2,1,0]
"""
def cuenta_regresiva(num):
    resultado = []
    for valor in range(num, -1, -1):
        resultado.append(valor)
    return resultado

print(cuenta_regresiva(10))