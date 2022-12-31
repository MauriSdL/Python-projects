import os
os.system("clear")

''' # Sintaxe Entry

'''
# from (a partir de)
from tkinter import *

janela = Tk()
janela.title("Entry")
janela.geometry('340x393')

# Widget Label de nome e idade e pais
label_Nome = Label (janela, text="Nome: ")
label_Idade = Label(janela, text="Idade: ")
label_Pais = Label(janela, text="Pais: ")

# Widget Entry de nome e idade e pais
entry_Nome = Entry(janela, width=25)
entry_Idade = Entry(janela, width=25)
entry_Pais = Entry(janela, width=25)

# Geometry Manager nome e idade e pais
label_Nome.place(x=20, y=10)
label_Idade.place(x=20, y=40)
label_Pais.place(x=20, y=70)

entry_Nome.place(x=75, y=10)
entry_Idade.place(x=75, y=40)
entry_Pais.place(x=75, y=70)



janela.mainloop()