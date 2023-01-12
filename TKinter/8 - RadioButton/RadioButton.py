import os
os.system('clear')

from tkinter import*

janela = Tk()
janela.title('Raido Button')
janela.geometry('300x250')


#--------------------------- Função ---------------------------
def obter():
    resultado = selecionado_1.get()
    print(resultado)

selecionado_1 = IntVar()  # Recebe qualquer valor inteiro
selecionado_2 = BooleanVar()  # Recebe 1 ou 0 ou TRUE ou FALSE
selecionado_3 = StringVar()  # Recebe uma string(texto)
# OBS: voçẽ deve escolher qual o tipo de uma desses 3 variaveis que vc vai usar
# OBS: O valor da variavel escolhida deve ser colocada no comando ex: variable=selecionado_1
#--------------------------- Função ---------------------------


radio1 = Radiobutton ( janela,
value='1',
text='Primeiro',
command=obter,
variable=selecionado_1)
radio1.grid(row=0, column=0, padx=10, pady=5)

radio2 = Radiobutton ( janela,
value='2',
text='Segundo',
command=obter,
variable=selecionado_1)
radio2.grid(row=1, column=0, padx=10, pady=5)

radio3 = Radiobutton ( janela,
value='3',
text='Terceiro',
command=obter,
variable=selecionado_1)
radio3.grid(row=2, column=0, padx=10, pady=5)


janela.mainloop()
