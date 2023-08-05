#Ejercicio 1

def pedir_nombre(nombre):
    print(f"Hola, {nombre}! ")
nom = input("ingresa tu nombre: ")

pedir_nombre(nom)




#Ejercicio2 

def pedir_numeros():
    lista = []
    print("INGRESE UN NUMERO:  -> 0 <- para salir:")
    num = int(input("-->: "))
    while num != 0:
        lista.append(num)
        num = int(input("-->: "))
           
    lista.sort()
    print("Lista ordenada de menor a mayor:", lista)
    suma = 0
    for num in lista:
        suma += num
    promedio = suma / len(lista) 

    print("Suma total:", suma)
    print("El promedio de los numeros de la lista es:", promedio)

pedir_numeros()
