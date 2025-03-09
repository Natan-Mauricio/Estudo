"""
Crie um programa que leia o número de dias trabalhados em um
mês e mostre o salário de um funcionário, sabendo que ele trabalha
8 horas por dia e ganha R$25 por hora trabalhada.

Algoritmo:
1. Iniciar um loop para solicitar o número de dias trabalhados até que um valor válido e dentro do intervalo 
permitido (1 a 31) seja fornecido.
2. Solicitar ao usuário que insira o número de dias trabalhados.
3. Tentar converter o valor inserido para um número inteiro.
4. Verificar se o número de dias é maior que 0 e menor ou igual a 31; caso contrário, exibir uma mensagem de erro e 
solicitar novamente.
5. Calcular o salário, considerando 8 horas por dia e 25 reais por hora, e exibir o valor do salário.
"""

while True:
    dias = input("Dias trabalhados: ")
    try:
        dias = int(dias)
        if dias <= 0 or dias > 31:
            raise Exception
        break
    except:
        print("Quantidade inválida! Tente novamente...")

print(f'Salário: R${(dias * 8 * 25)}')