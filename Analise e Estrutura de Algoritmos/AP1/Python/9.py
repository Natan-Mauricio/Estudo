#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar.
"""
Algoritmo:
1. Iniciar um loop para solicitar ao usuário o saldo da carteira até que um valor válido e positivo seja fornecido.
2. Solicitar ao usuário que insira o saldo em reais.
3. Tentar converter o valor inserido para um número real (float).
4. Verificar se o saldo é maior que 0; caso contrário, exibir uma mensagem de erro e solicitar novamente.
5. Exibir o valor convertido de reais para dólares (considerando a taxa de conversão de 1 real = 5.76 dólares) com 
duas casas decimais.
"""

while True:
    saldo = input("Carteira: R$")
    try:
        saldo = float(saldo)
        if saldo > 0:
            break
        else:
            raise Exception
    except:
        print("Valor inválido! Tente novamente...")

print(f'Conversão: R${saldo} = US${(saldo / 5.76):.2f}')