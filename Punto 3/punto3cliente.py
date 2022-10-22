class Cliente:
    
    def __init__(self, userBD, Apell, City, IT, saldo):
        self.userBD = userBD
        self.Apell = Apell
        self.City = City
        self.IT = IT
        self.Saldo = saldo
        

    def login(self):
        user = input('Escriba su nombre de usuario: ')
        Apellido = input('Escriba su apellido: ')
        City = input ('Escriba su ciudad: ')
        Cedula = input('Escriba su Cedula: ')
        if self.userBD == user and self.Apell == Apellido and self.IT == Cedula and self.City == City:
            print(f'Bienvenido {self.userBD, self.Apell} su saldo es: {int(self.saldo)}')
        else:
            print('Usuario o Cedula inválido')