from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import math

KV = '''
<CalcWidget>:
    orientation: 'horizontal'
    entry: entry
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.2
        Button:
            text: 'Padrão'
            on_release: root.show_mode('padrao')
        Button:
            text: 'Científica'
            on_release: root.show_mode('cientifica')
        Button:
            text: 'Programação'
            on_release: root.show_mode('programacao')
        Button:
            text: 'Conversor'
            on_release: root.show_mode('conversor')
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        TextInput:
            id: entry
            font_size: 32
            size_hint_y: 0.1
            multiline: False
        BoxLayout:
            id: main_area
            orientation: 'vertical'
            size_hint_y: 0.9
'''


class CalcWidget(BoxLayout):
    entry = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modes = {
            'padrao': ['+', '-', '*', '/', '='],
            'cientifica': ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'exp'],
            'programacao': ['bin', 'hex', 'oct'],
            'conversor': ['C->F', 'F->C', 'm->cm', 'cm->m', 'kg->g', 'g->kg', 'L->mL', 'mL->L']
        }
        self.show_mode('padrao')

    def show_mode(self, mode):
        area = self.ids.main_area
        area.clear_widgets()
        # Teclado numérico responsivo com tecla ⌫ para apagar último dígito
        num_pad = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '⌫', 'C']
        ]
        for row in num_pad:
            row_layout = BoxLayout(
                orientation='horizontal', spacing=5, size_hint_y=0.2)
            for key in row:
                btn = Button(text=key, size_hint=(1, 1))
                btn.bind(on_release=lambda inst, k=key: self.on_numeric(k))
                row_layout.add_widget(btn)
            area.add_widget(row_layout)

        # grid de funções específicas do modo
        buttons = self.modes.get(mode, [])
        cols = 4 if mode in ['padrao', 'conversor'] else 3
        func_grid = GridLayout(cols=cols, spacing=5, size_hint_y=0.6)
        for b in buttons:
            btn = Button(text=b)
            btn.bind(on_release=lambda inst, txt=b,
                     m=mode: self.on_button(m, txt))
            func_grid.add_widget(btn)
        area.add_widget(func_grid)

    def on_numeric(self, key):
        if key == 'C':
            self.entry.text = ''
        elif key == '⌫':
            self.entry.text = self.entry.text[:-1]
        else:
            self.entry.text += key

    def on_button(self, mode, text):
        e = self.entry
        if mode == 'padrao':
            if text == '=':
                try:
                    e.text = str(eval(e.text))
                except:
                    e.text = 'Erro'
            else:
                e.text += text
        elif mode == 'cientifica':
            try:
                x = float(e.text)
                funcs = {
                    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                    'log': math.log10, 'ln': math.log, 'sqrt': math.sqrt,
                    'exp': math.exp
                }
                e.text = str(funcs[text](x))
            except:
                e.text = 'Erro'
        elif mode == 'programacao':
            try:
                v = int(e.text)
                conv = {'bin': bin, 'hex': hex, 'oct': oct}[text]
                e.text = conv(v)
            except:
                e.text = 'Erro'
        elif mode == 'conversor':
            try:
                v = float(e.text)
                convs = {
                    'C->F': v*9/5+32, 'F->C': (v-32)*5/9,
                    'm->cm': v*100, 'cm->m': v/100,
                    'kg->g': v*1000, 'g->kg': v/1000,
                    'L->mL': v*1000, 'mL->L': v/1000
                }
                e.text = str(convs[text])
            except:
                e.text = 'Erro'


class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return CalcWidget()


if __name__ == '__main__':
    CalculatorApp().run()

# Parte (back-end) da lógica dos cálculos

# função de calcular (posteriormente será colocada abaixo do código dos frames)


def calcular():
    resultado = eval()
    # passando o valor para a tela
    app.label.set(resultado)


calcular()
