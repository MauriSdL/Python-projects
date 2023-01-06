
import os
os.system("clear")

from tkinter import *


#-----------------------------------------------------------------------

# Segundo Cria a Segunda Janela e seu conteudo dentro dela
def abrir_janela():
    janela2 = Toplevel()  # Comando para chamar a outra janela
    janela2.title('Janela Nova')
    janela2.geometry('300x400')
    

    label_Nome = Label(janela2, text='Nome:')
    label_Nome.grid(row=0, column=0, padx=20, pady=80)

    botao_voltar = Button(janela2, text='Fechar a janela', command=janela2.destroy)  # destroy tem como função destruir(fechar a janela aberta)
    botao_voltar.grid(row=1, column=0, padx=30, pady=25)




#------------------------------------------------------------------------
# Primeiro Cria a Primeira Janela e seus conteudos dentro dela
janela1 = Tk()
janela1.geometry('500x600')

botao = Button(janela1, text='Ir para nova janela', command=abrir_janela)
botao.grid(row=0, column=0, padx=50, pady= 50)


janela1.mainloop()