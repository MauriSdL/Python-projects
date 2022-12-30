import os
os.system("clear")

''' Sintaxe pack() (Pacote)
Ele coloca os widgth um em baixo do outro
lavel = label (janela, width=20, text="Olá Mundo!)
label.pack()

# Parametros do pack()
side(lado) =>  indica de que lado você quer que seja adicionado (TOP, BOTTOM, LEFT e RIGHT). Se quer um alinhamento horizontal, use side=LEFT, por exemplo

fill => para preencher um espaço. Pode usar como argumneto X, Y ou BOTH, e ele vai cobrir todo o espaçamento horizontal (X), vertical (Y) ou ambos (BOTH)

expand => pode passar como YES ou NO, para definir se o widget vai preencher todo o espaço extra do container ou não.

padx e pady => preenchem o ao redor do widget com espaço em branco

pack_forget => retira um widget empacotado do container que foi inserido anteriormente

'''

# Dessa forma o pack() coloca um widgt abaixo do outro
from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('450x166')



Label_name = Label(janela, width=7,height=2, text="Nome:", font=('Arial 15'), fg='#fc3503', bg='black')

# Um widgt abaixo do outro
#Label_name.pack()

# Alinhado da Esquerda para Direita formando uma linha horizontal
#Label_name.pack(side=LEFT)

# Alinhado da Direita para Esquerda formando uma linha horizontal
#Label_name.pack(side=RIGHT)

# Alinhado de cima para baixo formando uma linha vertical
#Label_name.pack(side=TOP)

# Alinhado de Baixo para Cima formando uma linha vertical
Label_name.pack(side=BOTTOM)



Label_Idade = Label(janela, width=7,height=2, text="Idade:", font=('Arial 15 bold'), fg='#429639', bg='black')
# Um widgt abaixo do outro
#Label_Idade.pack()

# Alinhado da Esquerda para Direita formando uma linha horizontal
#Label_Idade.pack(side=LEFT)

# Alinhado da Direita para Esquerda formando uma linha horizontal
#Label_Idade.pack(side=RIGHT)

# Alinhado de cima para baixo formando uma linha vertical
#Label_Idade.pack(side=TOP)

# Alinhado de Baixo para Cima formando uma linha vertical
Label_Idade.pack(side=BOTTOM)



Label_Pais = Label(janela, width=7,height=2, text="Pais:", font=('Arial 15'), fg='#6168e8', bg='black')

# Um widgt abaixo do outro
#Label_Pais.pack()

# Alinhado da Esquerda para Direita formando uma linha horizontal
#Label_Pais.pack(side=LEFT)

# Alinhado da Direita para Esquerda formando uma linha horizontal
#Label_Pais.pack(side=RIGHT)

# Alinhado de cima para baixo formando uma linha vertical
#Label_Pais.pack(side=TOP)

# Alinhado de Baixo para Cima formando uma linha vertical
Label_Pais.pack(side=BOTTOM)



janela.mainloop()
