import PySimpleGUI as sg

def MenuPrincipal():
    menu = [[sg.Button("Iniciar"),sg.Button("Configurar"),sg.Button("Cargar Partida"),sg.Button("Salir")]
    ]
    window=sg.Window("Menu de juego").Layout(menu)
    event,values=window.Read()
    window.Close()
    return event

def Dificultad():
    dificultad = [[sg.Button('Facil',size=(10,2))],[sg.Button('Medio',size=(10,2))],[sg.Button('Dificil',size=(10,2))]
    ]
    window=sg.Window("Dificultad de juego").Layout(dificultad)
    nivel,values=window.Read()
    window.Close()
    return nivel

def Tableros(nivel):
    if (nivel is 'Facil'):
        tablero = [[sg.Button("  ",size=(5,2),key=(x,y)) for x in range(10)]for y in range(10)
        ]
    elif (nivel is 'Medio'):
        tablero = [[sg.Button("  ",size=(5,2),key=(x,y)) for x in range(10)]for y in range(10)
        ]
    elif (nivel is 'Dificil'):
        tablero = [[sg.Button("  ",size=(5,2),key=(x,y)) for x in range(10)]for y in range(10)
        ]
    return tablero

def Tablero(tablero,nivel):
    window=sg.Window("Tablero de juego nivel "+nivel).Layout(tablero)
    while True:
        event,values=window.Read()
        print(event)
        if (event is None):
            break;
        if (event == (0,0)):
            sg.Popup(event)

event=MenuPrincipal()
if (event is 'Configurar'):
    nivel=Dificultad()
    print(nivel)
    Tablero(Tableros(nivel),nivel)
elif (event is 'Iniciar'):
    nivel='Facil'
    Tablero(Tableros(nivel),nivel)
print('cambio')
print('otro print')
