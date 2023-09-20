import PySimpleGUI as sg

def telaCalculadora():
    layout=[
        [sg.Push(),sg.Text("Calcularora"),sg.Push()],
        [sg.Input(key="-VALOR1-"),sg.Text("+"),sg.Input(key="-VALOR2-")],
        [sg.Button("Calcular", key="-CALCULAR-"),sg.Text("Resultado="),sg.Input(disabled=True,key="-RESULTADO-")]
    ]

    return sg.Window("Calculadora",layout)

janela1=telaCalculadora()
cont=1
while True:

    events,values = janela1.read()

    if events == sg.WIN_CLOSED:
        break

    if events =="-CALCULAR-":
        try:
            v1 = float(values["-VALOR1-"])
            v2 = float(values["-VALOR2-"])
            somar=v1+v2
            janela1["-RESULTADO-"].update(value=somar)
            janela1["-VALOR1-"].update(value="")
            janela1["-VALOR2-"].update(value="")
        except Exception as e:
            sg.Popup("Digite Somente Numeros seu Cavalo !")
            janela1["-VALOR1-"].update(value="")
            janela1["-VALOR2-"].update(value="")