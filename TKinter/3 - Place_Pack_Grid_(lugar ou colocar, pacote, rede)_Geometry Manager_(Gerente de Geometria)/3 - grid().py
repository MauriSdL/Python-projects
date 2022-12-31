import os
os.system("clear")

''' Sintaxe grid() (Rede)
O grid() coloca os widgts em uma grade semelhante a uma tabela
    row(fileira) = são as linhas de uma tabela
    colunm(coluna) = são as colunas de uma tabela
label = label (janela, widgth=20, text="Olhá Mundo!")
label.grid(row=0, column=1)
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


