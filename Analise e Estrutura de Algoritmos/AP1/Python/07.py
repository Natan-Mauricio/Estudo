#Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
"""
Algoritmo:
1. Iniciar um loop para solicitar um número real até que um valor válido seja fornecido.
2. Solicitar ao usuário que insira um número real.
3. Tentar converter o valor inserido para um número real (float).
4. Se o valor for um número real válido, sair do loop.
5. Se o valor não for um número real, exibir uma mensagem de erro e solicitar novamente.
6. Exibir o dobro do número inserido.
7. Exibir a terça parte do número inserido, formatando o resultado com duas casas decimais.
"""

while True:
    num = input("Digite um número real: ")
    try:
        num = float(num)
        break
    except:
        print("Não foi digitado um real! Tente novamente...")

print(f'O dobro de {num} é {num * 2}')
print(f'A terça parte de {num} é {num / 3:.2f}')