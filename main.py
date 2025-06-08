import tkinter as tk
from tkinter import ttk
import sqlite3

# cores
preto = "#212121"
branco = "#FFFFFF"
azul = "#3a576b"
azul_claro = "#3498DB"
cinza = "#dee0e0"
laranja = "#e39734"

# janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("420x520")
janela.configure(bg=preto)

# abas
abas = ttk.Notebook(janela)
tab_calc = ttk.Frame(abas)
tab_conv = ttk.Frame(abas)
tab_imc = ttk.Frame(abas)
tab_prog = ttk.Frame(abas)
tab_hist = ttk.Frame(abas)

abas.add(tab_calc, text="Calculadora")
abas.add(tab_conv, text="Conversão")
abas.add(tab_imc, text="IMC")
abas.add(tab_prog, text="Programação")
abas.add(tab_hist, text="Histórico")
abas.pack(expand=True, fill="both")

# calculadora simples
todos_valores = ""
valor_texto = tk.StringVar()

frame_tela = tk.Frame(tab_calc, bg=azul)
frame_tela.pack(expand=True, fill="both")
tk.Label(frame_tela, textvariable=valor_texto, font=('Ivy 24'), anchor='e', bg=azul, fg=branco).pack(expand=True, fill='both', padx=10, pady=10)

frame_botoes = tk.Frame(tab_calc)
frame_botoes.pack(expand=True, fill="both")

# funcoes
def entrada_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)
    
def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        salvar_no_historico(todos_valores, resultado)
        todos_valores = resultado
    except:
        valor_texto.set("Erro")
        todos_valores = ""
        
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Configurar grid para botões 5 linhas x 4 colunas
for i in range(5):
    frame_botoes.rowconfigure(i, weight=1)
for j in range(4):
    frame_botoes.columnconfigure(j, weight=1)    

# teclado
botoes = [
    ("C", 0, 0, 2, limpar_tela),
    ("%", 0, 2, 1, lambda: entrada_valores('%')),
    ("/", 0, 3, 1, lambda: entrada_valores('/')),
    ("7", 1, 0, 1, lambda: entrada_valores('7')),
    ("8", 1, 1, 1, lambda: entrada_valores('8')),
    ("9", 1, 2, 1, lambda: entrada_valores('9')),
    ("*", 1, 3, 1, lambda: entrada_valores('*')),
    ("4", 2, 0, 1, lambda: entrada_valores('4')),
    ("5", 2, 1, 1, lambda: entrada_valores('5')),
    ("6", 2, 2, 1, lambda: entrada_valores('6')),
    ("-", 2, 3, 1, lambda: entrada_valores('-')),
    ("1", 3, 0, 1, lambda: entrada_valores('1')),
    ("2", 3, 1, 1, lambda: entrada_valores('2')),
    ("3", 3, 2, 1, lambda: entrada_valores('3')),
    ("+", 3, 3, 1, lambda: entrada_valores('+')),
    ("0", 4, 0, 2, lambda: entrada_valores('0')),
    (".", 4, 2, 1, lambda: entrada_valores('.')),
    ("=", 4, 3, 1, calcular)
]

# botoes
for (texto, linha, coluna, colspan, comando) in botoes:
    bg = laranja if texto in "C/*-+%=" else cinza
    fg = branco if texto in "C/*-+%=" else preto
    btn = tk.Button(frame_botoes, text=texto, bg=bg, fg=fg,
                    font=('Ivy 18 bold'), command=comando)
    btn.grid(row=linha, column=coluna, columnspan=colspan,
             sticky="nsew", padx=2, pady=2)
    
# banco de dados
def salvar_no_historico(expressao, resultado):
    conn = sqlite3.connect("historico_calc.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS historico (id INTEGER PRIMARY KEY AUTOINCREMENT, expressao TEXT, resultado TEXT)")
    cursor.execute("INSERT INTO historico (expressao, resultado) VALUES (?, ?)", (expressao, resultado))
    conn.commit()
    conn.close()

frame_hist = tk.Frame(tab_hist, bg=branco)
frame_hist.pack(expand=True, fill="both")

lb_hist = tk.Listbox(frame_hist, font=('Ivy', 12))   
lb_hist.pack(expand=True, fill="both", padx=10, pady=10)
 
def carregar_historico():
    lb_hist.delete(0, tk.END)
    conn = sqlite3.connect("historico_calc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT expressao, resultado FROM historico ORDER BY id DESC LIMIT 50")
    for expr, res in cursor.fetchall():
        lb_hist.insert(tk.END, f"{expr} = {res}")
    conn.close()
    
abas.bind("<<NotebookTabChanged>>", lambda e: carregar_historico() if abas.tab(abas.select(), "text") == "Histórico" else None)



janela.mainloop()