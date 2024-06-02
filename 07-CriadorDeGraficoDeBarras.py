# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita uma quantidade de valores e cria o gráfico de acordo com eles.

import matplotlib.pyplot as plt

def criar_grafico_barras(valores):
    quantidade_valores = len(valores)
    largura_barra = 0.5
    posicoes_barras = range(1, quantidade_valores + 1)

    plt.bar(posicoes_barras, valores, width=largura_barra, color='blue')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Barras')
    plt.show()

valores = []
quantidade = int(input("Quantos valores deseja inserir? "))
for i in range(1, quantidade + 1):
    valor = float(input(f"Digite o valor {i}: "))
    valores.append(valor)

criar_grafico_barras(valores)
