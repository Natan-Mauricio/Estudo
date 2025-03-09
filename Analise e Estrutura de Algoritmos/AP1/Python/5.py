#Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
"""
Algoritmo:
1. Definir uma função 'valida' que verifica se uma nota está dentro do intervalo válido (0 a 10).
2. Iniciar um loop para solicitar as duas notas até que ambas sejam válidas.
3. Solicitar ao usuário que insira a primeira nota (Nota 1).
4. Solicitar ao usuário que insira a segunda nota (Nota 2).
5. Tentar converter as duas notas para números decimais (float).
6. Verificar se ambas as notas estão dentro do intervalo válido utilizando a função 'valida'.
7. Se ambas as notas forem válidas, sair do loop.
8. Se uma ou ambas as notas forem inválidas, exibir uma mensagem de erro e solicitar as notas novamente.
9. Calcular e exibir a média das duas notas com 2 casas decimais.
"""

def valida(nota):
    if nota < 0 or nota > 10:
        return False
    else:
        return True

while True:
    n1 = input("Nota 1: ")
    n2 = input("Nota 2: ")
    try:
        n1 = float(n1)
        n2 = float(n2)
        if (valida(n1) and valida(n2)):
            break
        else:
            raise Exception
    except:
        print("Uma ou mais notas inválidas! Tente novamente...")

print(f'Média: {((n1 + n2) / 2):.2f}')