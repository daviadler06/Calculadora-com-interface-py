import tkinter as tk
from tkinter import ttk
import sqlite3

# cores
PRETO = "#212121"
BRANCO = "#FFFFFF"
AZUL = "#3a576b"
AZUL_CLARO = "#3498DB"
CINZA = "#dee0e0"
LARANJA = "#e39734"

# Dados para conversão de unidades
unidades = {
    'Peso': [{'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1}, {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}],
    'Comprimento': [{'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}]
}

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
tk.Label(frame_tela, textvariable=valor_texto, font=('Ivy 24'), anchor='e',
         bg=azul, fg=branco).pack(expand=True, fill='both', padx=10, pady=10)

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
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS historico (id INTEGER PRIMARY KEY AUTOINCREMENT, expressao TEXT, resultado TEXT)")
    cursor.execute(
        "INSERT INTO historico (expressao, resultado) VALUES (?, ?)", (expressao, resultado))
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
    cursor.execute(
        "SELECT expressao, resultado FROM historico ORDER BY id DESC LIMIT 50")
    for expr, res in cursor.fetchall():
        lb_hist.insert(tk.END, f"{expr} = {res}")
    conn.close()


abas.bind("<<NotebookTabChanged>>", lambda e: carregar_historico()
          if abas.tab(abas.select(), "text") == "Histórico" else None)


# ========== ABA 2: Conversão de Unidades ==========

frame_conv = tk.Frame(tab_conv, bg=branco)
frame_conv.pack(pady=20)

tk.Label(frame_conv, text="Conversor de Unidades", font=('Ivy 16 bold'),
         bg=branco, fg=azul_claro).grid(row=0, column=0, columnspan=2, pady=10)

# Modo de conversão: Peso ou Comprimento
tk.Label(frame_conv, text="Tipo:", bg=branco).grid(
    row=1, column=0, sticky="e", padx=5)
modo_combo = ttk.Combobox(frame_conv, values=list(
    unidades.keys()), state="readonly", width=12)
modo_combo.grid(row=1, column=1, sticky="w", padx=5)
modo_combo.set("Peso")

# ComboBox de unidades
tk.Label(frame_conv, text="De:", bg=branco).grid(
    row=2, column=0, sticky="e", padx=5)
c_de = ttk.Combobox(frame_conv, state="readonly", width=12)
c_de.grid(row=2, column=1, sticky="w", padx=5)

tk.Label(frame_conv, text="Para:", bg=branco).grid(
    row=3, column=0, sticky="e", padx=5)
c_para = ttk.Combobox(frame_conv, state="readonly", width=12)
c_para.grid(row=3, column=1, sticky="w", padx=5)

# Entrada de valor
tk.Label(frame_conv, text="Valor:", bg=branco).grid(
    row=4, column=0, sticky="e", padx=5)
e_valor = tk.Entry(frame_conv, font=("Ivy", 12), justify="center")
e_valor.grid(row=4, column=1, sticky="w", padx=5)

# Resultado
l_res_conv = tk.Label(frame_conv, text="", font=(
    "Ivy", 14), bg=branco, fg=azul)
l_res_conv.grid(row=6, column=0, columnspan=2, pady=10)

# Funções


def atualizar_opcoes(event=None):
    modo = modo_combo.get()
    opcoes = [list(d.keys())[0] for d in unidades[modo]]
    c_de['values'] = opcoes
    c_para['values'] = opcoes
    c_de.set(opcoes[0])
    c_para.set(opcoes[1])


def calcular_conversao():
    try:
        modo = modo_combo.get()
        lista = [list(d.keys())[0] for d in unidades[modo]]
        valor = float(e_valor.get())
        de = c_de.get()
        para = c_para.get()
        fator = unidades[modo][lista.index(
            de)][de] / unidades[modo][lista.index(para)][para]
        resultado = valor * fator
        l_res_conv.config(text=f"{resultado:.4g} {para}")
    except:
        l_res_conv.config(text="Erro na conversão")


# Botão calcular
btn_conv = tk.Button(frame_conv, text="Converter",
                     command=calcular_conversao, bg=laranja, fg=preto)
btn_conv.grid(row=5, column=0, columnspan=2, pady=10)

modo_combo.bind("<<ComboboxSelected>>", atualizar_opcoes)
atualizar_opcoes()


# ========== ABA 3: IMC ==========

frame_imc = tk.Frame(tab_imc, bg=branco)
frame_imc.pack(pady=30)

tk.Label(frame_imc, text="Calculadora de IMC", font=(
    'Ivy 16 bold'), bg=branco, fg=azul_claro).pack(pady=10)

tk.Label(frame_imc, text="Peso (kg):", bg=branco).pack()
e_peso = tk.Entry(frame_imc, font=('Ivy 12'), justify="center")
e_peso.pack(pady=5)

tk.Label(frame_imc, text="Altura (m):", bg=branco).pack()
e_altura = tk.Entry(frame_imc, font=('Ivy 12'), justify="center")
e_altura.pack(pady=5)

l_res_imc = tk.Label(frame_imc, text="", font=("Ivy", 14), bg=branco, fg=azul)
l_res_imc.pack(pady=10)


def calcular_imc():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())
        imc = peso / (altura ** 2)
        resultado = f"IMC: {imc:.2f} — "
        if imc < 18.5:
            resultado += "Abaixo do peso"
        elif 18.5 <= imc < 25:
            resultado += "Peso ideal"
        elif 25 <= imc < 30:
            resultado += "Sobrepeso"
        else:
            resultado += "Obesidade"
        l_res_imc.config(text=resultado)
    except:
        l_res_imc.config(text="Valores inválidos")


tk.Button(frame_imc, text="Calcular", command=calcular_imc,
          bg=laranja, fg=preto).pack(pady=10)


# ========== ABA 4: Programação (Binário, Octal, Hexadecimal) ==========

frame_prog = tk.Frame(tab_prog, bg=branco)
frame_prog.pack(pady=30)

tk.Label(frame_prog, text="Conversor de Programação", font=(
    'Ivy 16 bold'), bg=branco, fg=azul_claro).pack(pady=10)

e_prog = tk.Entry(frame_prog, font=('Ivy 12'), justify='center')
e_prog.pack(pady=5)

l_prog_result = tk.Label(
    frame_prog, text="", font=("Ivy", 14), bg=branco, fg=azul)
l_prog_result.pack(pady=10)


def converter_programacao(tipo):
    try:
        valor = int(e_prog.get())
        if tipo == "bin":
            resultado = bin(valor)
        elif tipo == "oct":
            resultado = oct(valor)
        elif tipo == "hex":
            resultado = hex(valor)
        l_prog_result.config(text=resultado)
    except:
        l_prog_result.config(text="Entrada inválida")


tk.Button(frame_prog, text="Binário", command=lambda: converter_programacao(
    "bin"), bg=cinza, fg=preto).pack(pady=2)
tk.Button(frame_prog, text="Octal", command=lambda: converter_programacao(
    "oct"), bg=cinza, fg=preto).pack(pady=2)
tk.Button(frame_prog, text="Hexadecimal", command=lambda: converter_programacao(
    "hex"), bg=cinza, fg=preto).pack(pady=2)


janela.mainloop()
