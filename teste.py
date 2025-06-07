import tkinter as tk
from tkinter import ttk
import sqlite3
import re

# ----------- CORES -----------
PRETO = "#212121"
BRANCO = "#FFFFFF"
AZUL = "#3a576b"
AZUL_CLARO = "#3498DB"
CINZA = "#dee0e0"
LARANJA = "#e39734"

# ----------- DADOS DE UNIDADES -----------
unidades = {
    'Peso': [{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'mg':0.001}],
    'Comprimento': [{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}]
}

# ----------- JANELA PRINCIPAL -----------
janela = tk.Tk()
janela.title("Calculadora Completa")
janela.geometry("420x520")
janela.configure(bg=PRETO)

# ----------- CRIAR ABAS -----------
notebook = ttk.Notebook(janela)

tab_calc = ttk.Frame(notebook)   # Aba Calculadora Simples
tab_conv = ttk.Frame(notebook)   # Aba Conversão de Unidades
tab_imc = ttk.Frame(notebook)    # Aba Cálculo IMC
tab_prog = ttk.Frame(notebook)   # Aba Programação (bin, oct, hex)
tab_hist = ttk.Frame(notebook)   # Aba Histórico

notebook.add(tab_calc, text="Calculadora")
notebook.add(tab_conv, text="Unidades")
notebook.add(tab_imc, text="IMC")
notebook.add(tab_prog, text="Programação")
notebook.add(tab_hist, text="Histórico")
notebook.pack(expand=True, fill="both")

# ==================== ABA 1: CALCULADORA SIMPLES ====================
todos_valores = ""
valor_texto = tk.StringVar()

# Tela da calculadora
frame_tela = tk.Frame(tab_calc, bg=AZUL)
frame_tela.pack(expand=True, fill="both")

label_tela = tk.Label(frame_tela, textvariable=valor_texto,
                      font=('Ivy 24'), bg=AZUL, fg=BRANCO, anchor='e')
label_tela.pack(expand=True, fill="both", padx=10, pady=10)

# Frame dos botões
frame_botoes = tk.Frame(tab_calc)
frame_botoes.pack(expand=True, fill="both")

# Função para atualizar valores da tela
def entrada_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)

# Função para calcular o resultado
def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        salvar_no_historico(todos_valores, resultado)  # Salva no banco histórico
        todos_valores = resultado
    except:
        valor_texto.set("Erro")
        todos_valores = ""
def calcular_porcentagem():
    global todos_valores
    try:
        # Expressão com números e operadores
        expressao = todos_valores
        match = re.search(r'([0-9\.]+)([\+\-\*/])([0-9\.]+)$', expressao)
        if match:
            a, operador, b = match.groups()
            a = float(a)
            b = float(b)
            porcentagem = a * b / 100
            nova_expr = f"{a}{operador}{porcentagem}"
            todos_valores = nova_expr
            valor_texto.set(todos_valores)
        else:
            valor_texto.set("Erro")
    except:
        valor_texto.set("Erro")
        todos_valores = ""

# Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Configurar grid para botões 5 linhas x 4 colunas
for i in range(5):
    frame_botoes.rowconfigure(i, weight=1)
for j in range(4):
    frame_botoes.columnconfigure(j, weight=1)

# Botões com texto, posição linha, coluna, colspan e comando
botoes = [
    ("C", 0, 0, 2, limpar_tela),
    ("%", 0, 2, 1, calcular_porcentagem),
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

# Criar os botões na tela
for (texto, linha, coluna, colspan, comando) in botoes:
    bg = LARANJA if texto in "C/*-+%=" else CINZA
    fg = BRANCO if texto in "C/*-+%=" else PRETO
    btn = tk.Button(frame_botoes, text=texto, bg=bg, fg=fg,
                    font=('Ivy 18 bold'), command=comando)
    btn.grid(row=linha, column=coluna, columnspan=colspan,
             sticky="nsew", padx=2, pady=2)

# ==================== ABA 2: CONVERSÃO DE UNIDADES ====================

frame_conv_top = tk.Frame(tab_conv, bg=BRANCO)
frame_conv_top.pack(fill="x", pady=10)

label_conv = tk.Label(frame_conv_top, text="Conversão de Unidades",
                      font=('Ivy 16 bold'), bg=BRANCO, fg=AZUL_CLARO)
label_conv.pack()

frame_conv_mid = tk.Frame(tab_conv, bg=BRANCO)
frame_conv_mid.pack(pady=10)

# Escolha do modo (Peso, Comprimento)
label_modo = tk.Label(frame_conv_mid, text="Modo:", bg=BRANCO)
label_modo.grid(row=0, column=0, padx=5)

modo_combo = ttk.Combobox(frame_conv_mid, values=list(unidades.keys()), state="readonly")
modo_combo.grid(row=0, column=1, padx=5)
modo_combo.set(list(unidades.keys())[0])

# Frame para opções e entrada
frame_conv = tk.Frame(tab_conv, bg=BRANCO)
frame_conv.pack(pady=10)

label_unidade = tk.Label(frame_conv, text="---", font=('Ivy 15 bold'), bg=BRANCO, width=10)
label_unidade.grid(row=0, column=0, columnspan=2, pady=10)

label_de = tk.Label(frame_conv, text="De:", bg=BRANCO)
label_de.grid(row=1, column=0)
c_de = ttk.Combobox(frame_conv, state="readonly", width=8)
c_de.grid(row=2, column=0, padx=5)

label_para = tk.Label(frame_conv, text="Para:", bg=BRANCO)
label_para.grid(row=1, column=1)
c_para = ttk.Combobox(frame_conv, state="readonly", width=8)
c_para.grid(row=2, column=1, padx=5)

e_num = tk.Entry(frame_conv, font=('Ivy 15 bold'), justify='center')
e_num.grid(row=3, column=0, columnspan=2, pady=10)

btn_converter = tk.Button(frame_conv, text="Calcular", bg=LARANJA, fg=PRETO, font=('Ivy 12 bold'))
btn_converter.grid(row=4, column=0, columnspan=2, pady=5)

label_resultado = tk.Label(frame_conv, text="", font=('Ivy 18 bold'), bg=BRANCO)
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

# Atualiza unidades conforme o modo escolhido
def atualizar_unidades(event=None):
    modo = modo_combo.get()
    label_unidade.config(text=modo)
    opcoes = [list(d.keys())[0] for d in unidades[modo]]
    c_de['values'] = opcoes
    c_para['values'] = opcoes
    c_de.set(opcoes[0])
    c_para.set(opcoes[1])

# Faz a conversão
def converte():
    try:
        modo = modo_combo.get()
        de = c_de.get()
        para = c_para.get()
        num = float(e_num.get())
        lista = [list(d.keys())[0] for d in unidades[modo]]
        fator = unidades[modo][lista.index(de)][de] / unidades[modo][lista.index(para)][para]
        res = num * fator
        label_resultado.config(text=f"{res:.4g} {para}")
    except:
        label_resultado.config(text="Erro na conversão")

modo_combo.bind("<<ComboboxSelected>>", atualizar_unidades)
btn_converter.config(command=converte)
atualizar_unidades()

# ==================== ABA 3: CÁLCULO DE IMC ====================

frame_imc = tk.Frame(tab_imc, bg=BRANCO)
frame_imc.pack(pady=30)

label_imc = tk.Label(frame_imc, text="Cálculo de IMC", font=('Ivy 16 bold'), bg=BRANCO, fg=AZUL_CLARO)
label_imc.pack(pady=10)

label_peso = tk.Label(frame_imc, text="Peso (kg):", bg=BRANCO)
label_peso.pack()

e_peso = tk.Entry(frame_imc, font=('Ivy 12'), justify='center')
e_peso.pack()

label_altura = tk.Label(frame_imc, text="Altura (m):", bg=BRANCO)
label_altura.pack()

e_altura = tk.Entry(frame_imc, font=('Ivy 12'), justify='center')
e_altura.pack()

label_imc_res = tk.Label(frame_imc, text="", font=('Ivy 12 bold'), bg=BRANCO, fg=AZUL)
label_imc_res.pack(pady=10)

def calcular_imc():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        label_imc_res.config(text=f"IMC: {imc}")
    except:
        label_imc_res.config(text="Entrada inválida")

btn_calcular_imc = tk.Button(frame_imc, text="Calcular", bg=LARANJA, fg=PRETO, command=calcular_imc)
btn_calcular_imc.pack(pady=5)

# ==================== ABA 4: PROGRAMAÇÃO ====================

frame_prog = tk.Frame(tab_prog, bg=BRANCO)
frame_prog.pack(pady=30)

label_prog = tk.Label(frame_prog, text="Calculadora de Programação", font=('Ivy 16 bold'), bg=BRANCO, fg=AZUL_CLARO)
label_prog.pack(pady=10)

e_prog = tk.Entry(frame_prog, font=('Ivy 12'), justify='center')
e_prog.pack(pady=5)

label_prog_res = tk.Label(frame_prog, text="", font=('Ivy 12 bold'), bg=BRANCO, fg=AZUL)
label_prog_res.pack(pady=10)

def converter(tipo):
    try:
        num = int(e_prog.get())
        if tipo == "bin":
            res = bin(num)
        elif tipo == "oct":
            res = oct(num)
        elif tipo == "hex":
            res = hex(num)
        label_prog_res.config(text=res)
    except:
        label_prog_res.config(text="Entrada inválida")

btn_bin = tk.Button(frame_prog, text="Binário", bg=CINZA, fg=PRETO, command=lambda: converter("bin"))
btn_bin.pack(pady=2)

btn_oct = tk.Button(frame_prog, text="Octal", bg=CINZA, fg=PRETO, command=lambda: converter("oct"))
btn_oct.pack(pady=2)

btn_hex = tk.Button(frame_prog, text="Hexadecimal", bg=CINZA, fg=PRETO, command=lambda: converter("hex"))
btn_hex.pack(pady=2)

# ==================== ABA 5: HISTÓRICO ====================

frame_hist = tk.Frame(tab_hist, bg=BRANCO)
frame_hist.pack(expand=True, fill="both")

lb_hist = tk.Listbox(frame_hist, font=("Ivy", 12))
lb_hist.pack(expand=True, fill="both", padx=10, pady=10)

# Função para salvar histórico no banco SQLite
def salvar_no_historico(expressao, resultado):
    conn = sqlite3.connect("historico_calc.db")
    cursor = conn.cursor()
    # Cria tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS historico (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        expressao TEXT,
                        resultado TEXT)''')
    cursor.execute("INSERT INTO historico (expressao, resultado) VALUES (?, ?)", (expressao, resultado))
    conn.commit()
    conn.close()

# Carregar histórico do banco e mostrar na lista
def carregar_historico():
    lb_hist.delete(0, tk.END)
    conn = sqlite3.connect("historico_calc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT expressao, resultado FROM historico ORDER BY id DESC LIMIT 50")
    dados = cursor.fetchall()
    for expr, res in dados:
        lb_hist.insert(tk.END, f"{expr} = {res}")
    conn.close()

# Atualiza histórico ao mudar para aba Histórico
def evento_mudar_aba(event):
    if notebook.tab(notebook.select(), "text") == "Histórico":
        carregar_historico()

notebook.bind("<<NotebookTabChanged>>", evento_mudar_aba)

# ----------- EXECUTAR APLICATIVO -----------
janela.mainloop()
