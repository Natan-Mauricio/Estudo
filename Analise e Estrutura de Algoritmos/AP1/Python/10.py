"""
Faça um algoritmo que leia a largura e altura de uma parede,
calcule e mostre a área a ser pintada e a quantidade de tinta
necessária para o serviço, sabendo que cada litro de tinta pinta
uma área de 2 metros quadrados.

Algoritmo:
1. Exibir a mensagem "Tinta Necessária para Pintar uma Parede".
2. Iniciar um loop para solicitar as dimensões da parede (largura e altura) até que valores válidos e positivos sejam fornecidos.
3. Solicitar ao usuário que insira a largura da parede (em metros).
4. Solicitar ao usuário que insira a altura da parede (em metros).
5. Tentar converter os valores inseridos para números reais (float).
6. Verificar se ambos os valores são maiores que 0; caso contrário, exibir uma mensagem de erro e solicitar novamente.
7. Calcular a área da parede multiplicando a largura pela altura.
8. Exibir a área da parede em metros quadrados.
9. Calcular e exibir a quantidade de tinta necessária, considerando que 1 litro de tinta cobre 2 metros quadrados, com 
duas casas decimais.
"""

print("Tinta Necessária para Pintar uma Parede\n")

while True:
    largura = input("Largura (metros): ")
    altura = input("Altura (metros): ")
    try:
        largura = float(largura)
        altura = float(altura)
        if largura > 0 and altura > 0:
            break
        else:
            raise Exception
    except:
        print("Um ou mais valores inválidos! Tente novamente...")
        
area = largura * altura

print(f'\nÁrea: {area} m²\nTinta: {(area / 2):.2f} L')