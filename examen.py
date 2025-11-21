#Pide al usuario un número y muestra su tabla de multiplicar del 1 hasta un numero que indicara el usuario usando un ciclo for o while. Crea una función para capturar los datos
def capturar_datos():
    numero = int(input("ingrese un numero:"))
    return numero
def tabla_multiplicar(numero, limite):
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")
num = capturar_datos()
limite = int(input("ingrese el limite de la tabla: "))
tabla_multiplicar(num, limite)
