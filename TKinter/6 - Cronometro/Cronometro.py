import os
os.system("clear")

from tkinter import *

# cores
cor1 = "#0a0a0a" # black/preto
cor2 = "#fafcff" # white/branco
cor3 = "#21c25c" # green/verde
cor4 = "#eb463b" # red/vermelha
cor5 = "#dedcdc" # gray/sinza
cor6 = "#3080f0" # bue/azul


janela = Tk()
janela.title('Cronometro')
janela.geometry('300x180')
janela.configure(bg=cor1) # Cor de fundo da janela
janela.resizable(width=FALSE, height=FALSE)


# Variaveis global
global tempo
global rodar
global contador
global limitador


# limitador
limitador = 59

# Tempo do Cronometro
tempo = "00:00:00"

# Permite se continua com o cronometro ou não
rodar = False

# Contador
contador = -5


# Função Iniciar
def iniciar():
    global tempo
    global contador
    global limitador


    if rodar:
        # antes do cronometro começar
        if contador <= 0:
            inicio = (f'Começando em {str(contador)}')
            appTempo['text'] = inicio
            appTempo['font'] = 'Arial 10'
        
        # Rodando o Cronometro
        else:
            appTempo['font'] = 'Times 50 bold'

            temporario = str(tempo)
            hora, minutos, segundos = map(int, temporario.split(":"))
            hora = int(hora)
            minutos = int(minutos)
            segundos = int(contador)


            if segundos >= limitador:
                contador = 0
                minutos += 1

            segundos = str(0) + str(segundos)
            minutos = str(0) + str(minutos)
            hora =  str(0) + str(hora)


            # Atualizando os valores atuais
            temporario = str(hora[-2:]) + ":" + str(minutos[-2:]) + ":" + str(segundos[-2:])
            appTempo['text'] = temporario
            tempo = temporario

    

    # Esse 1000 significa um segundo
    label_tempo.after(1000,iniciar)
    contador += 1

# Função para dar inicio
def start():
    global rodar
    rodar = True
    iniciar()

# Função Pausar
def pausar():
    global rodar
    rodar = False

# Função reiniciar
def reiniciar():
    global contador
    global tempo

    # reiniciando o contador
    contador = 0

    # reiniciando o tempo
    tempo = "00:00:00"
    label_tempo['text'] = tempo



# Titulo 
label_tempo = Label(janela, text='Cronometro', font=('Arial 20'), bg=cor1, fg=cor2)
label_tempo.place(x=74, y=8)

appTempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor4)
appTempo.place(x=28, y=53)

# Botão iniciar
btn_Iniciar = Button(janela,command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn_Iniciar.place(x=15, y=130)

# Botão Pausar
btn_Pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn_Pausar.place(x=105, y=130)

# Botão Reiniciar
btn_Reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn_Reiniciar.place(x=190, y=130)


janela.mainloop()