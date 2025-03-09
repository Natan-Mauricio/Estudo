#Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
"""
Algoritmo:
1. Iniciar um loop para solicitar um número inteiro até que um valor válido seja fornecido.
2. Solicitar ao usuário que insira um número inteiro.
3. Tentar converter o valor inserido para um número inteiro.
4. Se o valor for um número inteiro válido, sair do loop.
5. Se o valor não for um número inteiro, exibir uma mensagem de erro e solicitar novamente.
6. Exibir o antecessor do número inserido.
7. Exibir o sucessor do número inserido.
"""

while True:
    num = input("Digite um número inteiro: ")
    try:
        num = int(num)
        break
    except:
        print("Não foi digitado um inteiro! Tente novamente...")

print(f'O antecessor de {num} é {num - 1}')
print(f'O sucessor de {num} é {num + 1}')