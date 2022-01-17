from tkinter import *
# Abertura da Janela
janela = Tk()

janela.title("LanchoNET") #Título da Página

# MENSAGENS
boasVindas = Label(janela, text="Boas Vindas! Este é o Sistema LanchoNet")
boasVindas.grid(column=0, row=0)

escolha = Label(janela, text='Escolha sua Ação:')
escolha.grid(column=0, row=1)

# BOTÕES
bVender = Button(janela, text='Venda')
bTabela = Button(janela, text='Tabela de Vendas')
bRegistro = Button(janela, text='Registro Geral de Vendas')
bEncerrar = Button(janela, text='Encerrar')

botoes = [bVender, bTabela, bRegistro, bEncerrar]
y = 2
for botao in botoes:
    botao.grid(column=0, row=y)
    y += 1

janela.mainloop() # Mantém a janela aberta
