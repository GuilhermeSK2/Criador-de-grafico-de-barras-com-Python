# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita uma quantidade de valores e cria o gráfico de acordo com eles.

import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

# Função para criar o gráfico de barras
def criar_grafico_barras(valores):
    quantidade_valores = len(valores)
    largura_barra = 0.5
    posicoes_barras = range(1, quantidade_valores + 1)
    plt.bar(posicoes_barras, valores, width=largura_barra, color='blue')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Barras')
    plt.show()

# Função para solicitar os valores ao usuário
def solicitar_valores():
    valores = []
    quantidade = simpledialog.askinteger("Entrada", "Quantos valores deseja inserir?")
    for i in range(1, quantidade + 1):
        valor = simpledialog.askfloat("Entrada", f"Digite o valor {i}: ")
        valores.append(valor)
    criar_grafico_barras(valores)

# Janela principal do Tkinter
root = tk.Tk()
root.withdraw()

# Solicitando os valores e criar o gráfico
solicitar_valores()

# Encerra o loop principal do Tkinter
root.mainloop()