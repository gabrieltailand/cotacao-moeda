import requests
import json
from tkinter import *

def pegar_cotacoes():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()

    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_bitcoin = cotacoes['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_bitcoin}'''

    texto_cotacoes['text'] = texto


janela = Tk()
janela.title('Cotação Atual de Moedas')
janela.geometry('400x200')
# Texto do topo
texto_orientacao = Label(janela, text='Clique no Botão para ver as cotações das moedas.')
texto_orientacao.grid(column=0, row=0, padx=60, pady=0)
# Botão de interação
botao = Button(janela, text='Buscar Cotações Dólar/Euro/BTC', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=20)
# Texto das cotações
texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()