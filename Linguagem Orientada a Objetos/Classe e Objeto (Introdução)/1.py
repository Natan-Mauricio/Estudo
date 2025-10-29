class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

    def fazer_aniversario(self):
        self.idade += 1
        print(f'Parabéns, {self.nome}! Agora você tem {self.idade} anos.')
    
p1 = Pessoa('Clara', 15)
p2 = Pessoa('João', 18)

p1.apresentar()
p1.fazer_aniversario()
print("---")
p2.apresentar()
p2.fazer_aniversario()