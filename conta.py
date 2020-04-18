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
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    def get_numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite