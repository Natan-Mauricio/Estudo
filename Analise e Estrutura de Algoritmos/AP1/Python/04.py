#Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
"""
Algoritmo:
1. Iniciar um loop para solicitar os valores até que ambos sejam válidos.
2. Solicitar ao usuário que insira o primeiro valor (Valor 1).
3. Solicitar ao usuário que insira o segundo valor (Valor 2).
4. Tentar converter ambos os valores para números inteiros.
5. Se ambos os valores forem válidos, sair do loop.
6. Se algum valor for inválido, exibir uma mensagem de erro e solicitar os valores novamente.
7. Exibir o resultado da soma dos dois valores.
"""

while(True):
    v1 = input("Valor 1: ")
    v2 = input("Valor 2: ")
    try:
        v1 = int(v1)
        v2 = int(v2)
        break
    except:
        print("Um ou dois valores inváidos! Tente novamente...")

print("Resultado:", v1 + v2)