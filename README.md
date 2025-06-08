🧮 Calculadora Multifuncional em Python
Este projeto é uma calculadora gráfica completa desenvolvida com Python e Tkinter, que reúne diversas funcionalidades organizadas em uma interface intuitiva com cinco abas principais:

🔢 Calculadora Padrão
Uma calculadora aritmética básica, com suporte às operações de:
➕ Adição
➖ Subtração
✖️ Multiplicação
➗ Divisão
% Porcentagem

Os resultados são exibidos em tempo real e as expressões são salvas automaticamente em um banco de dados SQLite, criando um histórico de operações acessível na aba específica.

🔁 Conversão de Unidades
Conversor de unidades para dois modos principais:
⚖️ Peso: kg, g, mg, etc.
📏 Comprimento: km, m, mm, etc.

Permite inserir um valor e selecionar as unidades de origem e destino. O sistema realiza a conversão automaticamente com base em fatores fixos definidos em dicionários.

⚖️ Cálculo de IMC
Ferramenta para calcular o Índice de Massa Corporal (IMC):
📝 O usuário insere o peso (kg) e a altura (m).
📊 O resultado informa a categoria correspondente:

Abaixo do peso

Peso ideal

Sobrepeso

Obesidade

💻 Conversor de Bases Numéricas
Ideal para estudantes e programadores, essa aba permite converter números decimais para:

⚙️ Binário

⚙️ Octal

⚙️ Hexadecimal

Basta digitar um número inteiro e clicar no tipo de conversão desejado.

🗃️ Histórico
Exibe as últimas 50 expressões e resultados calculados na aba principal. O histórico é carregado automaticamente sempre que a aba é acessada, consultando o banco de dados local historico_calc.db.

🧱 Tecnologias Utilizadas
Python 3

Tkinter (interface gráfica)

SQLite (banco de dados local)

📦 Execução
Basta ter Python instalado e executar o script principal. O banco de dados será criado automaticamente na primeira execução, e todas as funcionalidades estarão disponíveis via interface gráfica.

Este projeto é ideal para fins didáticos, acadêmicos ou como base para aplicações maiores. Ele demonstra como combinar GUI, lógica de programação, persistência de dados e usabilidade em um único aplicativo.