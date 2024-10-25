class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = []

    def realizar_transacao (conta, trasacao):
        pass

    def adicionar_conta (conta):
        pass

class ContaCorrente():
    def __init__(self, limite, limite_saques):
        self._limite = limite
        self._limite_saque = limite_saques

class Conta(ContaCorrente):
    def __init__ (self, limite, limite_saque, saldo, numero, agencia, cliente, historico):
        super().__init__(limite, limite_saque)
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def saldo():
        pass

    def nova_conta(cliente: Cliente, numero: int):
        pass

    def sacar (valor: float):
        pass

    def depositar (valor: float):
        pass

class Deposito:
    def __init__(self, valor):
        self._valor = valor

class Saque:
    def __init__(self, valor):
        self._valor = valor

class Transação():
    pass

class Historico():
    pass