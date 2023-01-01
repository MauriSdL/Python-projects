
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

delete(0, END) => serve para apagar os campos dos entry, 0 é o começo e END é ate o fim OBS:sempre será esses valores 0 e END.

state='disable' => Desativa uma caixa de Entry

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxx
janela = Tk()
janela.title("Entry")
janela.geometry('450x350')
janela.resizable(False, False)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx



def obterDadosEntry():
    #Obtem os valores de Entry
    nome = entry_Nome.get()
    idade = entry_Idade.get()
    pais = entry_Pais.get()

    # Subistitui o valor vazio de text dos label resposta pelos valores das variaveis acima nome iidade pais 
    nomeRes['text'] = nome
    idadeRes['text'] = idade
    paisRes['text'] = pais

    # Limpa os valores dos Entry
    # # 0(zero) é o inicio
    # END é o final
    entry_Nome.delete(0, END)
    entry_Idade.delete(0, END)
    entry_Pais.delete(0, END)




# Titulo xxxxxxxxxxxxxxxxxxxx
label_Formulario = Label(janela, text="Mini Formulário", font="Arial 15 bold")
label_Formulario.grid(row=0, column=1, pady=25)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Nome xxxxxxxxxxxxxxxxxxxx
label_Nome = Label (janela, text="Nome:")
label_Nome.grid(row=1, column=0, pady=10)
# Entry Nome
entry_Nome = Entry(janela, width=25, state='disable')
entry_Nome.grid(row=1, column=1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Idade xxxxxxxxxxxxxxxxxxxx
label_Idade = Label(janela, text="Idade:")
label_Idade.grid(row=2, column=0, pady=10)
# Entry Idade
entry_Idade = Entry(janela, width=25)
entry_Idade.grid(row=2, column=1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


# Pais xxxxxxxxxxxxxxxxxxxx
label_Pais = Label(janela, text="Pais:")
label_Pais.grid(row=3, column=0, padx=5, pady=10)
# Entry Pais
entry_Pais = Entry(janela, width=25)
entry_Pais.grid(row=3, column=1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx




# Resposta xxxxxxxxxxxxxxxxxxxx
nomeRes = Label (janela, text="")
nomeRes.grid(row=4, column=0,padx=10, pady=30)

idadeRes = Label(janela, text="")
idadeRes.grid(row=4, column=1, pady=30)

paisRes = Label(janela, text="")
paisRes.grid(row=4, column=2, pady=30)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx




# Button xxxxxxxxxxxxxxxxxxxx
button = Button(janela, command=obterDadosEntry , text="Verificar Dados", width=22, height=1)
button.grid(row=5, column=1, pady=10)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx


janela.mainloop()
