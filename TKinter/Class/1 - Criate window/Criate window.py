# o asteristico significa todos , importa tudo o que tem dentro da biblioteca tkinter
from tkinter import *

# Cores em variaveis
preto = '#242323'

# Criar uma instancia
janela = Tk()

# Titulo da janela
janela.title("Olá Mundo")

# Tamanho da janela
janela.geometry('600x250') # Largura,Separado por X, da Altura

# Icone da janela
# Aqui, False significa que esta imagem de ícone se aplica apenas a esta janela específica, mas não a futuros toplevels criados.
# Se True for utilizado, a imagem de ícone é aplicada a todos os futuros toplevels criados também.
janela.iconphoto(TRUE, PhotoImage(file="TKinter/Class/Class_1_Introductionto window/ico/Python-icon-16x16.png"))

# Redimensionar a janela
janela.resizable(width=True, height=True)

# Alterar cor de fundo da Janela
janela.config(bg='#242323')

# Manter a janela Aberta direto
janela.mainloop()
