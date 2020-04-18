class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("contruindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
            
    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)