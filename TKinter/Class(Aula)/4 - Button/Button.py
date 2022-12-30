import os
os.system("clear")

''' # Button
text =>    Texto que aparece no botão. 
style =>   Estilo a ser usado na renderização deste botão
image =>  Imagem a ser exibida no Botão. 
relief =>  Escolhe o estilo do botao(flat, groove, solid, raised, sunken, ridge)
comand => Uma função a ser chamada quando o botão é pressionado. 
'''

from tkinter import *

janela = Tk()
janela.title("Button")
janela.geometry("300x250")

global contador
contador = 0

def executar():    
    global contador

    texto_1 = 'Numero Impar: '
    texto_2 = 'Numero Par: '

    if (contador % 2) == 0:
        resultado = texto_2 + str(contador)
        label['text'] = resultado
        label['fg'] = '#24851e'
        
    else:
        resultado = texto_1 + str(contador)
        label['text'] = resultado
        label['fg'] = '#2586c2'

    contador += 1

# Label
label = Button (janela, width=20, height=2, text="Texto será apresentado", relief="flat", fg='white',bg='#121211')
label.grid(row=0, column=0, padx=5, pady=10)

#Button
button = Button (janela, command=executar, width=8, height=1, text="Cica Aqui", relief="raised", fg='#fcb603',bg='white')
button.grid(row=0, column=1, padx=5, pady=10)


janela.mainloop()