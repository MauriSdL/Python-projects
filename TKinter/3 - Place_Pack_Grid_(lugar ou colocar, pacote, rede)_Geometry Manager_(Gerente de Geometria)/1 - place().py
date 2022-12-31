
import os
os.system("clear")

''' Sintaxe place() (Lugar ou colocar)

O place() Usa Cordenadas Absolutas(Em pixes), Sua Referencia, Para as medidas de x (horizontal) e y (vertical) tem como Referencia o canto Superior Esquerdo da Tela, Esse seria o valor zero(0) da tela.

    Novos widgts são colocados ao lado direito de widgts ja existentes

label = label (janela, width=20, text="Olá Mundo!" )
label.place(x=10, y=10)
'''

from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x235')

Label_name = Label(janela, width=7,height=2, text="Nome:", font=('Arial 15'), fg='#fc3503', bg='black')
Label_name.place(x=35, y=20)

Label_name = Label(janela, width=7,height=2, text="Mauri", font=('Arial 15'), fg='#fc3503', bg='black')
Label_name.place(x=135, y=20)



Label_Idade = Label(janela, width=7,height=2, text="Idade:", font=('Arial 15 bold'), fg='#429639', bg='black')
Label_Idade.place(x=35, y=90)

Label_Idade = Label(janela, width=7,height=2, text="41", font=('Arial 15 bold'), fg='#429639', bg='black')
Label_Idade.place(x=135, y=90)



Label_Pais = Label(janela, width=7,height=2, text="Pais:", font=('Arial 15'), fg='#6168e8', bg='black')
Label_Pais.place(x=35, y=160)

Label_Pais = Label(janela, width=7,height=2, text="Brasil", font=('Arial 15'), fg='#6168e8', bg='black')
Label_Pais.place(x=135, y=160)



janela.mainloop()
