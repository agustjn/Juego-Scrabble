import PySimpleGUI as sg
import json
import time

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
    if (nivel == 'Facil'):
        tablero = [[sg.Button("{},{}".format(x,y),size=(5,2),key=str(x)+","+str(y),pad=(0,0)) for x in range(15)]for y in range(15)
        ]
        botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
        ]
        layout = [[sg.Column(tablero),sg.Column(botones)]]
        window=sg.Window("Tablero de juego nivel "+nivel).Layout(layout)
    elif (nivel == 'Medio'):
        tablero = [[sg.Button("  ",size=(5,2),key=(x,y),pad=(0,0)) for x in range(15)]for y in range(15)
        ]
    elif (nivel == 'Dificil'):
        tablero = [[sg.Button("  ",size=(5,2),key=(x,y),pad=(0,0)) for x in range(15)]for y in range(15)
        ]
    return window

def Tablero(window,nivel):#tablero,nivel
    #window=sg.Window("Tablero de juego nivel "+nivel).Layout(tablero)
    matriz_tablero={str(x)+","+str(y):'' for x in range(15)for y in range(15)}
    print(matriz_tablero)
    while True:
        event,values=window.Read()
        print(event)
        if (event is None) | (event == 'Terminar'):
            break;
        if (event == 'Guardar Partida'):
            archivo = open('Tablero.json','w')
            json.dump(matriz_tablero,archivo)
            archivo.close()
            sg.Popup('Partida Guardada en el archivo')
        if(event == '0,0'):
            window.Element(event).Update('Z',button_color=('white','red'))
            z=window.Element(event).GetText() #GetText() te permite obtener el contenido del boton
            sg.Popup(event)
            if (matriz_tablero[event]==''):
                matriz_tablero[event]=z

    #return matriz_tablero
def ActualizarCasillas(casillas,window):
    for casilla,letra in casillas.items():
        if (letra!=''):
            window.Finalize()
            window.Element(casilla).Update(letra)
    return window
def CargarPartida(window):
    archivo_tablero=open('Tablero.json','r')
    casillas=json.load(archivo_tablero)
    archivo_tablero.close()
    return ActualizarCasillas(casillas,window)

def Jugar(opcion_menu):
    if (opcion_menu == 'Configurar'):
        nivel=Dificultad()
        Tablero(Tableros(nivel),nivel)
    elif (opcion_menu == 'Iniciar'):
        nivel='Facil'
        Tablero(Tableros(nivel),nivel)
    elif (opcion_menu == 'Cargar Partida'):
        #CargarPartida()
        Tablero(CargarPartida(Tableros('Facil')),'Facil')
        sg.Popup('En mantenimiento')

Jugar(MenuPrincipal())
