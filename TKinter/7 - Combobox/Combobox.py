
import os
os.system("clear")

# Para usar o combobox tem que importar o ttk antes de importar o tkinter
from tkinter.ttk import*
from tkinter import*



def obter():
    resultado = combo.get()
    print(resultado)




janela = Tk()
janela.title("Combobox")
janela.geometry('300x250')


Label_nome = Label(janela,
width=20,
height=2,
text='Faça a sua escolha',
font=('Arial 10'),
anchor=W)
Label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)


# Criando Combobox(Caixa de seleção)
combo = Combobox(janela)
# Definindo valores para o combobox
combo['values'] = (1, 2, 3, 'joao', 'futi')
# Escolhe qual (pelo indice) o valor da lista acima irá aparecer no combobox, OBS: se nao usar o current o combobox ira funcionar mas nao aparecerá nada, mas mesmo assim poderá usar normalmente
combo.current(0)
combo.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
# para pegar o valor escolhido no combobox crie uma função usando .get()

botao =  Button(janela,
command=obter,
width=10,
height=1,
text='Ver resposta',
relief='raised',
bg='white')
botao.grid(row=2, column=0, padx=5, pady=20)


janela.mainloop()