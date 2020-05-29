import PySimpleGUI as sg

def TableroFacil():
    tablero = [[sg.Button(size=(5,2),button_color=('black', 'grey'),key=str(x)+","+str(y), pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero), sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Facil").Layout(layout)
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":["1,1","7,0","13,1","0,7","7,7","14,7","1,13","7,14","13,13"],
             "green":["0,0","14,0","0,14","14,14","6,3","7,4","8,3","3,6","4,7","3,8","11,6","10,7","11,8","6,11","7,12","8,11"],
             "blue":["2,4","4,1","10,1","12,4","6,6","6,8","8,6","8,8","2,10","3,13","12,10","10,13"],
             "red":["3,3","7,3","11,3","2,7","12,7","3,11","7,11","11,11"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Finalize()
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window,matriz_tablero,'Facil'

def TableroMedio():
    tablero = [[sg.Button(size=(5,2),button_color=('black','grey'),key=str(x)+","+str(y),pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero),sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Medio").Layout(layout)
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":["1,1","7,0","13,1","0,7","7,7","14,7","1,13","7,14","13,13"],
             "green":["0,0","14,0","0,14","14,14","6,3","7,4","8,3","3,6","4,7","3,8","11,6","10,7","11,8","6,11","7,12","8,11"],
             "blue":["2,4","4,1","10,1","12,4","6,6","6,8","8,6","8,8","2,10","3,13","12,10","10,13"],
             "red":["3,3","7,3","11,3","2,7","12,7","3,11","7,11","11,11"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Finalize()
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window,matriz_tablero,"Medio"

def TableroDificil():
    tablero = [[sg.Button(size=(5,2),button_color=('black','grey'),key=str(x)+","+str(y),pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero),sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Dificil").Layout(layout)
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":["1,1","7,0","13,1","0,7","7,7","14,7","1,13","7,14","13,13"],
             "green":["0,0","14,0","0,14","14,14","6,3","7,4","8,3","3,6","4,7","3,8","11,6","10,7","11,8","6,11","7,12","8,11"],
             "blue":["2,4","4,1","10,1","12,4","6,6","6,8","8,6","8,8","2,10","3,13","12,10","10,13"],
             "red":["3,3","7,3","11,3","2,7","12,7","3,11","7,11","11,11"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Finalize()
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window,matriz_tablero,"Dificil"

def TableroPersonalizado(nivel):
    tablero = [[sg.Button(size=(5,2),button_color=('black','grey'),key=str(x)+","+str(y),pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero),sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel "+nivel).Layout(layout)
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":["1,1","7,0","13,1","0,7","7,7","14,7","1,13","7,14","13,13"],
             "green":["0,0","14,0","0,14","14,14","6,3","7,4","8,3","3,6","4,7","3,8","11,6","10,7","11,8","6,11","7,12","8,11"],
             "blue":["2,4","4,1","10,1","12,4","6,6","6,8","8,6","8,8","2,10","3,13","12,10","10,13"],
             "red":["3,3","7,3","11,3","2,7","12,7","3,11","7,11","11,11"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Finalize()
            window.Element(casilla).Update(button_color=('black', color))
            matriz_tablero[casilla]['color_casilla']=color
    return window, matriz_tablero, nivel