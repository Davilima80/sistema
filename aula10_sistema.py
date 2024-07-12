import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

dados = pd.read_csv('aula10_dados.csv')

venda = dados['vendas']
vende = dados['vendedor']

janela = tk.Tk()
janela.geometry('500x500')
janela.title('GRÁFICOS')
texto = tk.Label(janela, text = 'Escolha um tipo de gráfico')
texto.pack()

def bar():
    plt.bar(vende, venda)
    plt.show()

def plot():
    plt.plot(vende, venda)
    plt.show()

def pie():
    plt.pie(venda, labels=vende)
    plt.show()

btn  =  tk.Button(janela, text='gráfico de coluna', command=bar)
btn.pack()

btn  =  tk.Button(janela, text='gráfico de linha', command=plot)
btn.pack()

btn  =  tk.Button(janela, text='gráfico de pizza', command=pie)
btn.pack()

janela.mainloop()

