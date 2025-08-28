class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def exibir_saldo(self):
        print(f'Seu saldo é de R${self.saldo}')

conta = ContaBancaria('João', 1000)

conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()