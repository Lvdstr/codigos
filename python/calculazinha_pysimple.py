import PySimpleGUI as sg
sg.theme('DarkTeal9')

layout = [
    [sg.Text('Digite o primeiro numero:'), sg.InputText(key='num')],
    [sg.Text('Digite o segundo numero:'), sg.InputText(key='num2')],
    [sg.Button('Somar'), sg.Button('Subtrair'), sg.Button('Multiplicar'), sg.Button('Dividir'), sg.Button('exponencial')],
    [sg.Text('Resultado:'), sg.Text('', key='resultado')]
]

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Somar':
        valor1 = float(values['num'])
        valor2 = float(values['num2'])
        resultado = valor1 + valor2
        window['resultado'].update(resultado)

    elif event == 'Subtrair':
        valor1 = float(values['num'])
        valor2 = float(values['num2'])
        resultado = valor1 - valor2
        window['resultado'].update(resultado)

    elif event == 'Multiplicar':
        valor1 = float(values['num'])
        valor2 = float(values['num2'])
        resultado = valor1 * valor2
        window['resultado'].update(resultado)

    elif event == 'Dividir':
        valor1 = float(values['num'])
        valor2 = float(values['num2'])
        resultado = valor1 / valor2
        window['resultado'].update(resultado)

    elif event == 'exponencial':
        valor1 = float(values['num'])
        valor2 = float(values['num2'])
        resultado = valor1 ** valor2
        window['resultado'].update(resultado)
        
    elif event == '':
        window['digite algo']

window.close()