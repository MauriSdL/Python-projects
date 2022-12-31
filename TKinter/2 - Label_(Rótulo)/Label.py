import os
os.system("clear")

''' Sintaxe label (Rótulo)

label = label (janela, width=20,,height=2 text="olá")
label.place(x=10, y=10)
x seria o deslocamento na horizontal(coluna)
y seria o deslocamento na vertical(linha)
width=> largura
height=> altura
text=> Texto que ira aparecer ex: Digite o seu nome:
font=(Arial 15 bold)=> font define o estilo de letra, Arial sempre inicie com a primeira letra em Maiusculo, 15 tTamanho da font, bold é negrito
fg ou foreground=> é a cor da letra
bg ou background=> é a cor de fundo

# Propriedade do grid
row = linha
column = coluna
pady = é a margin
'''

from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('450x166')

Label_name = Label(janela, width=7,height=2, text="Nome:", font=('Arial 15'), fg='#fc3503', bg='black')
Label_name.grid(row=0, column=0, pady=2, padx=2)

Label_Idade = Label(janela, width=7,height=2, text="Idade:", font=('Arial 15 bold'), fg='#429639', bg='black')
Label_Idade.grid(row=1, column=0, pady=1, padx=2)

Label_Pais = Label(janela, width=7,height=2, text="Pais:", font=('Arial 15'), fg='#6168e8', bg='black')
Label_Pais.grid(row=2, column=0, pady=1, padx=2)

janela.mainloop()


