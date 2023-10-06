# -*- coding: utf-8 -*-
from PySimpleGUI import (
    Text, Input, Button,
    Multiline, Canvas,
    Table, CalendarButton,
    Window, WIN_CLOSED,
    popup_get_text, Frame,
    Column, Combo, Push,
    theme, VSeparator,
    HSeparator, read_all_windows
)

tema = 'LightBlue2'

setor = [
    'Sala-Professor'
,
        'Sala-Funcionário'
]

problema_professor = [
    [
        'Computador'
    ],

    [
        'Limpeza'
    ]
]

problema_funcionario = [
    [
        'Manutenção'
    ],

    [
        'Ajustes'
    ]
]

professores = [
    [
        'Rogério'
    ],

    [
        'Joselito'
    ]
]

funcionarios = [
    [
        'Pedrinho'
    ],

    [
        'Adalberto'
    ]
]


def tela_requisicao():
    theme(tema)

    layout_esquerdo = [
        [
            Text(text='Setor')
        ],

        [
            Combo(values=setor,
                  size=(21, 1),
                  key='-SETOR-',
                  enable_events=True)
        ],

        [
            Text(text='Funcionário')
        ],

        [
            Combo(values=[],
                  key='-FUNCIONARIO-',
                  size=(21, 1),
                  enable_events=True)
        ],

        [
            HSeparator()
        ],

        [
            Button(button_text='LISTAR')
        ]

    ]

    layout_direito = [
        [
            Text(text='Problema')
        ],

        [
            Combo(values='',
                  key='-PROBLEMA-',
                  size=(21, 1),
                  enable_events=True)
        ],

        [
            Text(text='Data')
        ],

        [
            Input(readonly=True,
                  key='-DATA-',
                  size=(15, 1)),

            CalendarButton(button_text='DATA',
                           default_date_m_d_y=(1, 1, 2023),
                           format='%d/%m/%Y',
                           close_when_date_chosen=False,
                           target='-DATA-')
        ],

        [
            HSeparator()
        ],

        [
            Push(),
            Button(button_text='REQUISITAR',
                   key='-REQUISITAR-')
        ]
    ]

    layout_coluna = [
        [
            Column(layout=layout_esquerdo),
            VSeparator(),
            Column(layout=layout_direito)
        ]
    ]

    layout = [
        [
            Frame(title='REQUISITAR',
                  layout=layout_coluna)
        ]
    ]

    return Window(title='REGISTRAR',
                  layout=layout,
                  finalize=True)


janela = tela_requisicao()

# while True:
#     eventos, valores = janela.read()
#     match eventos:
#         case '-SETOR-':
#             for i in setor:
#                 if i == 'Sala-Professor':
#                     janela['-FUNCIONARIO-'].update(values=professores)
#                     janela['-PROBLEMA-'].update(values=problema_professor)
#                 elif i == 'Sala-Funcionário':
#                     janela['-FUNCIONARIO-'].update(values=funcionarios)
#                     janela['-PROBLEMA-'].update(values=problema_funcionario)
#         case '-REQUISITAR-':
#             pass
#         case '-LISTAR-':
#             pass
#         case WIN_CLOSED:
#             break
while True:
    eventos, valores = janela.read()


    if eventos == "-SETOR-":

        if valores["-SETOR-"] == "Sala-Professor":
            janela['-FUNCIONARIO-'].update(values=professores)
        elif valores["-SETOR-"] == "Sala-Funcionário":
            janela["-FUNCIONARIO-"].update(values=funcionarios)


