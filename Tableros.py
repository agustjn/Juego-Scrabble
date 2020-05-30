import PySimpleGUI as sg

def TableroFacil():
    tablero = [[sg.Button(size=(5,2),button_color=('black', 'grey'),key=str(x)+","+str(y), pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')],[sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero), sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Facil").Layout(layout).Finalize()
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":["1,1","7,0","13,1","0,7","7,7","14,7","1,13","7,14","13,13"],
             "green":["0,0","14,0","0,14","14,14","6,3","7,4","8,3","3,6","4,7","3,8","11,6","10,7","11,8","6,11","7,12","8,11"],
             "blue":["2,4","4,1","10,1","12,4","6,6","6,8","8,6","8,8","2,10","3,13","12,10","10,13"],
             "red":["3,3","7,3","11,3","2,7","12,7","3,11","7,11","11,11"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window,matriz_tablero,'Facil'

def TableroMedio():
    #sg.theme('Dark Brown')
    tablero = [[sg.Button(size=(5,2),button_color=('black','grey'),key=str(x)+","+str(y),pad=(0,0)) for x in range(15)]for y in range(15)
    ]
    botones=[
               [sg.Button('Guardar Partida')],
               [sg.Button('Terminar')]
            ]

    layout = [[sg.Column(tablero),sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Medio").Layout(layout).Finalize()
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={
             "yellow":["0,0","4,4","7,7","4,10","0,14","10,4","14,0","10,10","14,14","2,4","2,10","4,12","10,12","12,4","12,10","4,2","10,2"],
             "green":["2,2","6,6","6,8","2,12","8,6","12,2","8,8","12,12","0,4","0,10","4,14","10,14","14,4","14,10","4,0","10,0"],
             "blue":["7,1","7,5","7,9","7,13","9,7","13,7","5,7","1,7"],
             "red":["7,3","7,11","11,7","3,7","2,6","2,8","6,12","8,12","12,6","12,8","6,2","8,2"]
            }
    for color, casillas in colores.items():
        for casilla in casillas:
            #casilla=x,y
            #casillas=['x,y','x,y'...'x,y']
            #color='colorName'
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window,matriz_tablero,"Medio"

def TableroDificil():
    tablero = [[sg.Button(size=(5, 2), button_color=('black', 'grey'), key=str(x)+","+str(y), pad=(0, 0)) for x in range(15)]for y in range(15)
    ]
    botones=[[sg.Button('Guardar Partida')], [sg.Button('Terminar')]
    ]
    layout = [[sg.Column(tablero),sg.Column(botones)]]
    window=sg.Window("Tablero de juego nivel Dificil").Layout(layout).Finalize()
    matriz_tablero={str(x)+","+str(y):{'letra':'','color_casilla':''} for x in range(15)for y in range(15)}
    colores={"yellow":['5,0',
                    '11,4',
                    '6,6',
                    '0,7', '1,7', '13,7', '14,7',
                    '8,8',
                    '3,10',
                    '9,14',],
             "green":['2,0', '12,0',
                    '4,2', '10,2',
                    '2,5', '13,5',
                    '4,7', '5,7', '9,7', '10,7',
                    '1,9', '13,9',
                    '4,12', '10,12',
                    '2,14', '12,14',],
             "blue":['7,0', '9,0',
                    '7,2',
                    '3,4',
                    '8,6',
                    '3,7', '6,7', '8,7', '11,7',
                    '6,8',
                    '11,10',
                    '7,12',
                    '5,14', '7,14'],
             "red":['1,1', '3,1', '11,1', '13,1',
                    '3,3', '5,3', '9,3', '11,3',
                    '1,4', '13,4',
                    '5,5', '7,5', '9,5',
                    '1,6', '13,6',
                    '2,7', '7,7', '12,7',
                    '1,8', '13,8',
                    '5,9', '7,9', '9,9',
                    '1,10', '13,10',
                    '3,11', '5,11', '9,11', '11,11',
                    '1,13', '3,13', '11,13', '13,13']}
    for color, casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla']=color
    return window, matriz_tablero, "Dificil"

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
