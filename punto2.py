#Codificar un programa en Python utilizando funciones lamda que permita: recibir 2 números y devolver
#1 → si el primer número es mayor que el segundo
#-1→ si el primer número es menor que el segundo
#Después una segunda función debe recibir el 1 o el -1 retornado por la función 1 y mostrar un mensaje
#Si recibe 1 → Debe indicar que el primer número es mayor
#Si recibe -1 → Debe indicar que el segundo número es mayor
#Recomendaciones: Utilizar operador ternario +1
#    print(f'{numero2} es mayor')     print(f'{numero1} es mayor que {numero2}')

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite El segundo numero: "))

calcularnumeromayor = lambda numero1, numero2 : 1 if numero1>numero2 else -1
mostrarResultado = lambda numero : print("El primer número es mayor") if numero == 1 else print("El segundo número es mayor")

mostrarResultado(calcularnumeromayor(numero1, numero2))

