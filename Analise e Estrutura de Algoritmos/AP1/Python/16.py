"""
Escreva um programa para calcular a redução do tempo
de vida de um fumante. Pergunte a quantidade de cigarros fumados
por dias e quantos anos ele já fumou. Considere que um fumante
perde 10 min de vida a cada cigarro. Calcule quantos dias de vida
um fumante perderá e exiba o total em dias.

Algoritmo:
1. Iniciar um loop para solicitar a quantidade de cigarros fumados por dia e os anos fumando até que valores válidos e 
positivos sejam fornecidos.
2. Solicitar ao usuário que insira a quantidade de cigarros fumados por dia.
3. Solicitar ao usuário que insira o número de anos fumando.
4. Tentar converter os valores inseridos para números inteiros.
5. Verificar se a quantidade de cigarros e os anos são maiores que 0; caso contrário, exibir uma mensagem de erro e 
solicitar novamente.
6. Calcular a quantidade aproximada de dias perdidos de vida, considerando que cada cigarro fumado diminui a vida em 
10 minutos, e exibir o resultado arredondado para o número inteiro mais próximo.
"""

while True:
    qtd = input("Cigarros fumados por dia: ")
    anos = input("Anos fumando: ")
    try:
        qtd = int(qtd)
        anos = int(anos)
        if qtd > 0 and anos > 0:
            break
        else:
            raise Exception
    except:
        print("Um ou dois valores inválidos! Tente novamente...")

print(f'Você perdeu aproximadamente {(qtd * 10 * anos * 365 / 1440):.0f} dias de vida!')