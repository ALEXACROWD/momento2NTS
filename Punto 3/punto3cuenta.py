class Cuenta:
    
    def __init__(self, numerocuenta, saldo, saldo_anterior):
        self.numerocuenta = numerocuenta
        self.saldo = saldo
        self.saldo_anterior = saldo_anterior
    
    def consultar(self):
        self.saldo
        print(self.saldo)

    def depositar(self):
        valor = int(input('¿Cuánto desea depositar?: '))
        if valor <= 0:
            print('Usted está intentando depositar una cantidad menor o igual a cero')
        else:
            self.saldo = int(self.saldo) + valor
            print(f'Su nuevo saldo es: {self.saldo}')

    def retirar(self):
        valor = int(input('¿Cuánto desea retirar?: '))
        if valor > int(self.saldo) or valor <= 0:
            print('Ha ocurrido un error')
        else:
            self.saldo = int(self.saldo_anterior) - valor
            print(f'Su nuevo saldo es: {self.saldo}')


