import PySimpleGUI as sg
import json
import time
from Tableros import TableroFacil, TableroMedio, TableroDificil, TableroPersonalizado
from ScoreControl import ScoreControl as sc

def MenuPrincipal():
    menu = [[sg.Button("Iniciar"), sg.Button("Configurar"), sg.Button("Cargar Partida"), sg.Button("Salir")]
    ]
    window=sg.Window("Menu de juego").Layout(menu)
    event,values=window.Read()
    window.Close()
    return event

def Dificultad():
    dificultad = [[sg.Button('Facil', size=(10, 2))], [sg.Button('Medio', size=(10, 2))], [sg.Button('Dificil', size=(10, 2))],
                  [sg.Button('Personalizado', size=(10, 2))]
    ]
    window=sg.Window("Dificultad de juego").Layout(dificultad)
    nivel,values=window.Read()
    window.Close()
    return nivel

def MenuPersonalizado():
    niveles=['Facil', 'Medio', 'Dificil']
    personalizado = [[sg.Text("Nivel"),sg.InputCombo(niveles, size = (10, 8), key='Nivel')],
                     [sg.Text("Tiempo"),sg.InputText(size = (10, 8), key='Tiempo')],
                     [sg.Button('Iniciar')]

    ]
    window=sg.Window("Juego personalizado").Layout(personalizado)
    event, values=window.Read()
    return event, values

def Tablero(window,matriz_tablero,nivel):#tablero,nivel
    puntos=sc(0)
    while True:
        event, values=window.Read()
        if event in (None, 'Terminar'):
            break;
        if (event == 'Guardar Partida'):
            archivo_tablero = open('Tablero.json', 'w')
            archivo_tablero_nivel=open('TableroNivel.json', 'w')
            json.dump(nivel, archivo_tablero_nivel)
            json.dump(matriz_tablero, archivo_tablero)
            archivo_tablero.close()
            archivo_tablero_nivel.close()
            sg.Popup('Partida Guardada en el archivo')
        if event in matriz_tablero:
            puntos.multiplicar(matriz_tablero[event]['color_casilla'])
            print(puntos.get_puntos)

def ActualizarCasillas(window,matriz_tablero):
    for casilla,contenido in matriz_tablero.items():
        if (contenido['letra']!=''):
            window.Finalize()
            window.Element(casilla).Update(contenido['letra'])
    return window

def CargarPartida():
    archivo_tablero=open('Tablero.json', 'r')
    archivo_tablero_nivel=open('TableroNivel.json', 'r')
    nivel=json.load(archivo_tablero_nivel)
    if (nivel=='Facil'):
        window,matriz_tablero,nivel=TableroFacil()
    elif(nivel=='Medio'):
        window,matriz_tablero,nivel=TableroMedio()
    elif(nivel=='Dificil'):
        window,matriz_tablero,nivel=TableroDificil()
    matriz_tablero=json.load(archivo_tablero)

    archivo_tablero.close()
    archivo_tablero_nivel.close()
    return ActualizarCasillas(window, matriz_tablero), matriz_tablero, nivel

def Jugar(opcion_menu):
    if (opcion_menu == 'Configurar'):
        nivel=Dificultad()
        if (nivel=='Facil'):
            window, matriz_tablero, nivel=TableroFacil()
        elif(nivel=='Medio'):
            window, matriz_tablero, nivel=TableroMedio()
        elif(nivel=='Dificil'):
            window, matriz_tablero, nivel=TableroDificil()
        elif(nivel=='Personalizado'):
            event, values=MenuPersonalizado()
            window, matriz_tablero, nivel=TableroPersonalizado(values['Nivel'])
        Tablero(window, matriz_tablero, nivel)
    elif (opcion_menu == 'Iniciar'):
        window, matriz_tablero, nivel=TableroFacil()
        Tablero(window, matriz_tablero, nivel)
    elif (opcion_menu == 'Cargar Partida'):
        window, matriz_tablero, nivel=CargarPartida()
        Tablero(window, matriz_tablero, nivel)

Jugar(MenuPrincipal())