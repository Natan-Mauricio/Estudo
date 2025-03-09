#Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
"""
Algoritmo:
1. Solicitar ao usuário que insira o nome do funcionário.
2. Iniciar um loop para solicitar o salário até que um valor válido seja fornecido.
3. Solicitar ao usuário que insira o salário.
4. Tentar converter o valor inserido para um número decimal (float).
5. Verificar se o salário é maior ou igual a um valor mínimo (salário mínimo atual: 1518).
6. Se o salário for válido, sair do loop.
7. Se o salário for inválido ou menor que o valor mínimo, exibir uma mensagem de erro e solicitar novamente.
8. Exibir o nome do funcionário e o salário válido informado.
"""

nome = input("Nome do Funcionário: ")

while True:
    salario = input("Salário: ")
    try:
        salario = float(salario)
        if salario >= 1518:
            break
        else:
            raise Exception
    except:
        print("Salário inválido! Tente novamente...")


print(f'O funcionário {nome} tem um salário de R${salario}')