#El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:
#Almacenar información de un cliente (nombre, apellido, cedula, ciudad)
#Almacenar información de la cuenta (numeroCuenta, saldo)
#Se debe permitir consultar saldo en cualquier momento
#Se debe permitir ingresar o retirar dinero cuando se desee +1
#FINALMENTE, CADA INTEGRANTE DEBE TRABAJAR EN UNA RAMA INDEPENDIENTE Y UNO DE LOS 3 SE ENCARGARÁ DE UNIR TODO EL DESARROLLO +1

from punto3cliente import Cliente
from punto3cuenta import Cuenta

objeto1 = Cliente("Jenn", "Marulanda", "1152684", "Medellín", "200")
objeto2 = Cuenta("1010", "100", "0")

print("***MENU***")
print("1. Agregar informacion.")
print("2. Consultar Saldo.")
print("3. Ingresar dinero.")
print("4. Retirar Dinero.")
print("0. SALIR")

i = 100

while(i !=0):
    i = int(input("Digite una opción del menú: "))
    if (i == 1):
        objeto1.login()
    if(i == 2):
        objeto2.consultar()
    if(i == 3):
        objeto2.depositar()
    if(i == 4):
        objeto2.retirar()        
else:
    print("Fin del programa.")
