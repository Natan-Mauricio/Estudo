""""
A locadora de carros precisa da sua ajuda para cobrar seus
serviços. Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço total a pagar, sabendo que o carro
custa R$90 por dia e R$0,20 por Km rodado.

Algoritmo:
1. Iniciar um loop para solicitar o número de quilômetros percorridos e os dias de aluguel até que valores válidos e 
positivos sejam fornecidos.
2. Solicitar ao usuário que insira a quantidade de quilômetros percorridos.
3. Solicitar ao usuário que insira o número de dias alugados.
4. Tentar converter o valor de quilômetros para float e o número de dias para inteiro.
5. Verificar se os valores de quilômetros e dias são maiores que 0; caso contrário, exibir uma mensagem de erro e 
solicitar novamente.
6. Calcular o total a pagar, considerando a tarifa diária de 90 reais e 0,20 reais por quilômetro percorrido, e 
exibir o valor com duas casas decimais.
"""

while True:
    km = input("Km percorridos: ")
    dias = input("Dias alugados: ")
    try:
        km = float(km)
        dias = int(dias)
        if km <= 0 or dias <= 0:
            raise Exception
        break
    except:
        print("Um ou mais valores inválidos! Tente novamente...")
        
print(f'\nTotal a pagar: R${(dias * 90 + 0.2 * km):.2f}')