#Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
"""
Algoritmo:
1. Iniciar um loop para solicitar o preço do produto até que um valor válido e positivo seja fornecido.
2. Solicitar ao usuário que insira o preço do produto.
3. Tentar converter o valor inserido para um número real (float).
4. Verificar se o preço é maior que 0; caso contrário, exibir uma mensagem de erro e solicitar novamente.
5. Calcular e exibir o preço do produto com 15% de desconto, formatado com 2 casas decimais.
"""

while True:
    preco = input("Preço do produto: R$")
    try:
        preco = float(preco)
        if preco <= 0:
            raise Exception
        break
    except:
        print("Preço inválido! Tente novamente...")
        
print(f'Preço com 15% de desconto: R${(preco - preco * 0.15): .2f}')