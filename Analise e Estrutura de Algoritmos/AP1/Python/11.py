#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
"""
Algoritmo:
1. Exibir a mensagem "Valor de Delta (Equação do 2° Grau)".
2. Iniciar um loop para solicitar os coeficientes da equação do segundo grau (a, b, c) até que valores válidos sejam fornecidos.
3. Solicitar ao usuário que insira o valor de 'a'.
4. Solicitar ao usuário que insira o valor de 'b'.
5. Solicitar ao usuário que insira o valor de 'c'.
6. Tentar converter os valores inseridos para números reais (float).
7. Verificar se o valor de 'a' não é zero, pois a equação do segundo grau não é válida se 'a' for igual a zero; caso contrário, 
exibir uma mensagem de erro e solicitar novamente.
8. Calcular e exibir o valor de Delta da equação do segundo grau com duas casas decimais, utilizando a fórmula: 
Δ = b² - 4ac.
"""

print("Valor de Delta (Equação do 2° Grau)")

while True:
    a = input("A: ")
    b = input("B: ")
    c = input("C: ")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0:
            raise Exception
        break
    except:
        print("Um ou mais valores inválidos! Tente novamente...") 

print(f'Delta: {(b * b - 4 * a * c):.2f}')