class Aluno:
    nome: str
    notas: list[float]

    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota: float):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        media = self.media()
        print(f"A média de {self.nome} é {media:.2f}...")
        return "Aprovado(a)!" if media >=7 else "Reprovado(a)!"


aluno = Aluno('Maria')
aluno.adicionar_nota(8)
aluno.adicionar_nota(6.5)
aluno.adicionar_nota(7.5)
print(f'{aluno.nome} está {aluno.situacao()}')