#Codificar un programa en Python utilizando funciones que permita recibir: Nombre, edad, País, Equipo y tiempo en minutos de múltiples ciclistas. El software estará en la capacidad de calcular y mostrar en pantalla cual fue el ciclista más rápido

#Recomendaciones: Programar menú (1. Agregar ciclista, 2. Ver resultados) +2

 

print("***MENU***")

print("1. Agregar Cilcista.")

print("2. Mostrar Ciclista.")

print("0. SALIR")

 

def calcularciclista():

   

    i = 100

    ciclistas = []

 

    while(i !=0):

        ciclista = {}

        i = int(input("Digite una opción del menú: "))

        if (i == 1):

            ciclista['nombre'] = input("Digite el nombre del ciclista: ")

            ciclista['edad'] = input("Digite la edad: ")

            ciclista['pais'] = input("Digite el país: ")

            ciclista['equipo'] = input("Digite el equipo: ")

            ciclista['tiempo'] = int(input("Digite el tiempo en minutos: "))

            ciclistas.append(ciclista)

        elif(i == 2):

            print(ciclistas)

    else:

        print("Fin del programa.")

   

calcularciclista()