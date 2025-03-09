#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
"""
Algoritmo:
1. Definir duas listas: 'medidas' (contendo unidades de medida) e 'mult' (contendo os fatores de conversão para cada unidade).
2. Iniciar uma variável 'i' com valor 0.
3. Iniciar um loop para solicitar ao usuário que insira uma distância em metros até que um valor válido e positivo seja fornecido.
4. Solicitar ao usuário que insira a distância em metros.
5. Tentar converter o valor inserido para um número real (float).
6. Verificar se o valor é maior que 0; caso contrário, exibir uma mensagem de erro e solicitar novamente.
7. Exibir uma mensagem "Conversões:".
8. Iniciar outro loop para realizar as conversões, iterando por todas as unidades de medida, utilizando o índice 'i'.
9. Para cada unidade, calcular a conversão multiplicando o valor em metros pelo fator de conversão correspondente em 'mult[i]' 
e exibir o resultado com 3 casas decimais.
10. Incrementar 'i' a cada iteração até alcançar o final da lista.
"""

medidas = [" km", " hm", " dam", " dm", " cm", " mm"]
mult = [0.001, 0.01, 0.1, 10, 100, 1000]
i = 0

while True:
    m = input("Digite uma distância em metros: ")
    try:
        m = float(m)
        if m > 0:
            break
        else:
            raise Exception
    except:
        print("Valor inválido! Tente novamente...")

print("Conversões:")
while i <= 5:
    print(f'{(m * mult[i]):.3f}{medidas[i]}')
    i += 1