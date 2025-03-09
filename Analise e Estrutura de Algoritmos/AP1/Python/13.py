#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
"""
Algoritmo:
1. Iniciar um loop para solicitar o salário até que um valor válido e maior ou igual ao salário mínimo (1.518,00) seja fornecido.
2. Solicitar ao usuário que insira o salário.
3. Tentar converter o valor inserido para um número real (float).
4. Verificar se o salário é maior ou igual ao salário mínimo; caso contrário, exibir uma mensagem de erro e solicitar novamente.
5. Calcular e exibir o salário com um aumento de 15%, formatado com duas casas decimais.
"""

while True:
    salario = input("Salário: R$")
    try:
        salario = float(salario)
        if salario < 1518:
            raise Exception
        break
    except:
        print("Salário inválido! Tente novamente...")
        
print(f'Salário com 15% de aumento: R${(salario + salario * 0.15):.2f}')