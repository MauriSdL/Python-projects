
import os
os.system("clear")

# from (a partir de)
from tkinter import *


# Sintaxe sticky
'''
sticky => Permite ajustar a posição de um widget em uma janela ou em outro widget.

Ele é usado para controlar o alinhamento de um widget dentro de um gerenciador de layout, como o pack ou o grid.

Para usar o sticky, basta passar um dos seguintes valores como parâmetro do método pack ou grid:

N: alinha o widget no topo do espaço disponível.
S: alinha o widget na parte inferior do espaço disponível.
E: alinha o widget à direita do espaço disponível.
W: alinha o widget à esquerda do espaço disponível.
NW: alinha o widget no canto superior esquerdo do espaço disponível.
NE: alinha o widget no canto superior direito do espaço disponível.
SW: alinha o widget no canto inferior esquerdo do espaço disponível.
SE: alinha o widget no canto inferior direito do espaço disponível.
CENTER: centraliza o widget no espaço disponível.

Além disso, é possível combinar vários valores de sticky para obter um alin
'''

# Sintaxe anchor
'''
anchor => É um recurso que permite ajustar a posição de um widget em relação ao espaço disponível. Ele é usado para controlar o alinhamento de um widget dentro de um gerenciador de layout, como o pack ou o grid.

Para usar o anchor, basta passar um dos seguintes valores como parâmetro do método pack ou grid:

N: alinha o widget no topo do espaço disponível.
S: alinha o widget na parte inferior do espaço disponível.
E: alinha o widget à direita do espaço disponível.
W: alinha o widget à esquerda do espaço disponível.
NW: alinha o widget no canto superior esquerdo do espaço disponível.
NE: alinha o widget no canto superior direito do espaço disponível.
SW: alinha o widget no canto inferior esquerdo do espaço disponível.
SE: alinha o widget no canto inferior direito do espaço disponível.
CENTER: centraliza o widget no espaço disponível.

O anchor é um parâmetro opcional dos métodos pack e grid, e pode ser usado para ajustar a posição de um widget dentro do espaço disponível de acordo com as suas necessidades. Por exemplo, para centralizar um widget horizontalmente e alinhá-lo ao topo do espaço disponível, você poderia usar o código a seguir:

Copy code
widget.pack(anchor="N", fill="x", expand=True)
O anchor é uma ferramenta útil para controlar o alinhamento de widgets em uma janela ou em outro widget

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxx
janela = Tk()
janela.title("Entry")
janela.geometry('340x360')
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Titulo xxxxxxxxxxxxxxxxxxxx
label_Formulario = Label(janela, text="Mini Formulário", font="Arial 15 bold")
label_Formulario.place(x=100, y=30)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Nome xxxxxxxxxxxxxxxxxxxx
label_Nome = Label (janela, text="Nome: ")
label_Nome.place(x=35, y=90)
# Nome Entry
entry_Nome = Entry(janela, width=25)
entry_Nome.place(x=90, y=90)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Idade xxxxxxxxxxxxxxxxxxxx
label_Idade = Label(janela, text="Idade: ")
label_Idade.place(x=35, y=120)
# Idade Entry
entry_Idade = Entry(janela, width=25)
entry_Idade.place(x=90, y=120)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Pais xxxxxxxxxxxxxxxxxxxx
label_Pais = Label(janela, text="Pais: ")
label_Pais.place(x=35, y=150)
# Pais Entry
entry_Pais = Entry(janela, width=25)
entry_Pais.place(x=90, y=150)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Resposta xxxxxxxxxxxxxxxxxxxx
resNome = Label (janela, text="Nome: ")
resNome.pack(side=LEFT)

resIdade = Label(janela, text="Idade: ")
resIdade.pack(side=LEFT)

resPais = Label(janela, text="Pais: ")
resPais.pack(side=LEFT)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Button xxxxxxxxxxxxxxxxxxxx
button = Button(janela, text="Verificar Dados", width=22, height=1)
button.place(x=75, y=300)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx

janela.mainloop()
