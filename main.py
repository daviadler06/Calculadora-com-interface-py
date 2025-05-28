# front end

from tkinter import *
from tkinter import ttk

#cores
preto = "#212121"
branco = "#ffffff"
azul = "#3a576b"
cinza = "#dee0e0"
laranja = "#e39734"

#criando janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg = preto)

#frames
frame_tela = Frame(janela, width = 235, height = 50, bg = azul)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row = 1, column = 0)

#label
app_label = Label(frame_tela, text = '123456789', width=24, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 13'), bg=azul, fg = branco)
app_label.place(x =0, y = 0)

#botoes
botao_clear = Button(frame_corpo, text = "C", width = 11, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_clear.place(x = 0, y = 0)

botao_porcentagem = Button(frame_corpo, text = "%", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_porcentagem.place(x = 118, y = 0)

botao_divisao = Button(frame_corpo, text = "/", width = 5, height = 2, bg = laranja, fg = branco, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_divisao.place(x = 177, y = 0)


botao_7 = Button(frame_corpo, text = "7", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_7.place(x = 0, y = 52)

botao_8 = Button(frame_corpo, text = "8", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_8.place(x = 59, y = 52)

botao_9 = Button(frame_corpo, text = "9", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_9.place(x = 118, y = 52)

botao_multiplicacao = Button(frame_corpo, text = "*", width = 5, height = 2, bg = laranja, fg = branco, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_multiplicacao.place(x = 177, y = 52)


botao_4 = Button(frame_corpo, text = "4", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_4.place(x = 0, y = 104)

botao_5 = Button(frame_corpo, text = "5", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_5.place(x = 59, y = 104)

botao_6 = Button(frame_corpo, text = "6", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_6.place(x = 118, y = 104)

botao_subtracao = Button(frame_corpo, text = "-", width = 5, height = 2, bg = laranja, fg = branco, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_subtracao.place(x = 177, y = 104)


botao_1 = Button(frame_corpo, text = "1", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_1.place(x = 0, y = 156)

botao_2 = Button(frame_corpo, text = "2", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_2.place(x = 59, y = 156)

botao_3 = Button(frame_corpo, text = "3", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_3.place(x = 118, y = 156)

botao_adicao = Button(frame_corpo, text = "+", width = 5, height = 2, bg = laranja, fg = branco, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_adicao.place(x = 177, y = 156)


botao_0 = Button(frame_corpo, text = "0", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_0.place(x = 0, y = 208)

botao_ponto = Button(frame_corpo, text = ".", width = 5, height = 2, bg = cinza, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_ponto.place(x = 59, y = 208)

botao_igual = Button(frame_corpo, text = "=", width = 11, height = 2, bg = laranja, fg = branco, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
botao_igual.place(x = 118, y = 208)


#rodando a janela
janela.mainloop()   


# Parte (back-end) da lógica dos cálculos

# função de calcular (posteriormente será colocada abaixo do código dos frames)


def calcular():
    resultado = eval()
    # passando o valor para a tela
    app.label.set(resultado)


calcular()
