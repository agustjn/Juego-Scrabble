import PySimpleGUI as sg
from VerificadorPalabra import checkOrientation

def Primera_Letra(listas,pos_en_tablero,letra_turno,matriz_tablero,window,key_letra,jugador):
    if window.Element(pos_en_tablero).GetText()=='':
        if (pos_en_tablero!=(7,7)) and (window.Element((7,7)).GetText()==''):
            sg.Popup("Debe iniciar en la casilla central")
        else:
            listas['pos_en_tablero'].append(pos_en_tablero)
            listas['letras_en_tablero'].append(letra_turno)
            listas['pos_en_atril'].append(key_letra)
            listas['casillas'].append(matriz_tablero[pos_en_tablero]['color_casilla'])
            listas['puntos_por_letra'].append(jugador.bolsa_fichas[letra_turno]['puntaje'])
            window.Element(pos_en_tablero).Update(letra_turno)
            window.Element(key_letra).Update('')
            jugador.actualizarCasillaAtril(key_letra[1])
            matriz_tablero[pos_en_tablero]['letra'] = letra_turno
    else:
        sg.Popup("Esa casilla contiene una letra")
    return listas,matriz_tablero

def Segunda_Letra(listas,pos_en_tablero,letra_turno,matriz_tablero,window,key_letra,jugador):
    orientacion=''
    columna = listas['pos_en_tablero'][-1][0]
    fila = listas['pos_en_tablero'][-1][1]
    print(pos_en_tablero,'columna = ', columna,' fila = ', fila)
    if window.Element(pos_en_tablero).GetText()=='':
        if ((pos_en_tablero[0] == columna+1) and (pos_en_tablero[1] == fila)) or(
           (pos_en_tablero[0] == columna) and (pos_en_tablero[1] == fila+1)):
            listas['pos_en_tablero'].append(pos_en_tablero)
            listas['letras_en_tablero'].append(letra_turno)
            listas['pos_en_atril'].append(key_letra)
            listas['casillas'].append(matriz_tablero[pos_en_tablero]['color_casilla'])
            listas['puntos_por_letra'].append(jugador.bolsa_fichas[letra_turno]['puntaje'])
            window.Element(pos_en_tablero).Update(letra_turno)
            window.Element(key_letra).Update('')
            jugador.actualizarCasillaAtril(key_letra[1])
            matriz_tablero[pos_en_tablero]['letra'] = letra_turno
            orientacion=checkOrientation(listas['pos_en_tablero'])
            print('Segunda letra orientacion = '+orientacion)
        else:
            sg.Popup('Trate con la casilla de la derecha o la de abajo')
    else:
        sg.Popup("Esa casilla contiene una letra")
    return listas,matriz_tablero,orientacion

def Letras_Horizontal(listas,pos_en_tablero,letra_turno,matriz_tablero,window,key_letra,jugador):
    columna = listas['pos_en_tablero'][-1][0]
    fila = listas['pos_en_tablero'][-1][1]
    print('columna = ', columna,' fila = ', fila)
    if window.Element(pos_en_tablero).GetText()=='':
        if(pos_en_tablero[0] == columna+1) and (pos_en_tablero[1] == fila):
            listas['pos_en_tablero'].append(pos_en_tablero)
            listas['letras_en_tablero'].append(letra_turno)
            listas['pos_en_atril'].append(key_letra)
            listas['casillas'].append(matriz_tablero[pos_en_tablero]['color_casilla'])
            listas['puntos_por_letra'].append(jugador.bolsa_fichas[letra_turno]['puntaje'])
            window.Element(pos_en_tablero).Update(letra_turno)
            window.Element(key_letra).Update('')
            jugador.actualizarCasillaAtril(key_letra[1])
            matriz_tablero[pos_en_tablero]['letra'] = letra_turno
        else:
            sg.Popup('Trate con la casilla de la derecha')
    else:
        sg.Popup("Esa casilla contiene una letra")
    return listas,matriz_tablero

def Letras_Vertical(listas,pos_en_tablero,letra_turno,matriz_tablero,window,key_letra,jugador):
    columna = listas['pos_en_tablero'][-1][0]
    fila = listas['pos_en_tablero'][-1][1]
    print('columna = ', columna,' fila = ', fila)
    if window.Element(pos_en_tablero).GetText()=='':
        if(pos_en_tablero[0] == columna) and (pos_en_tablero[1] == fila+1):
           listas['pos_en_tablero'].append(pos_en_tablero)
           listas['letras_en_tablero'].append(letra_turno)
           listas['pos_en_atril'].append(key_letra)
           listas['casillas'].append(matriz_tablero[pos_en_tablero]['color_casilla'])
           listas['puntos_por_letra'].append(jugador.bolsa_fichas[letra_turno]['puntaje'])
           window.Element(pos_en_tablero).Update(letra_turno)
           window.Element(key_letra).Update('')
           jugador.actualizarCasillaAtril(key_letra[1])
           matriz_tablero[pos_en_tablero]['letra'] = letra_turno
        else:
            sg.Popup('Trate con la casilla de abajo')
    else:
        sg.Popup("Esa casilla contiene una letra")
    return listas,matriz_tablero

def Palabra_Invalida(listas,matriz_tablero,window):
    for i in range(len(listas['pos_en_atril'])):
        window.Element(listas['pos_en_atril'][i]).Update(
        listas['letras_en_tablero'][i])
        window.Element(listas['pos_en_tablero'][i]).Update('')
        matriz_tablero[listas['pos_en_tablero'][i]]['letra']=''
    return matriz_tablero
