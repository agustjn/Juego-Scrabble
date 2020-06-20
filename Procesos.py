import PySimpleGUI as sg
def Primera_Letra(lista_de_posiciones,cont,event,letra_turno,matriz_tablero,window):
    lista_de_posiciones.append(event)
    cont += 1
    matriz_tablero[event]['letra'] = letra_turno
    window.Element(event).Update(letra_turno)
    return lista_de_posiciones,cont,matriz_tablero

def Segunda_Letra(lista_de_posiciones,cont,event,columna,fila,letra_turno,matriz_tablero,window):
    if ((int(event.split(',')[0]) == columna+1) & (
         int(event.split(',')[1]) == fila)) | (
        (int(event.split(',')[0]) == columna) & (
         int(event.split(',')[1]) == fila+1)):
        lista_de_posiciones.append(event)
        matriz_tablero[event]['letra'] = letra_turno
        window.Element(event).Update(letra_turno)

        cont += 1
    else:
        sg.Popup('Trate con la casilla de abajo o la derecha')
    return lista_de_posiciones,cont,matriz_tablero

def Letras_Horizontal(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window):
    if(int(event.split(',')[0]) == columna+1) & (
       int(event.split(',')[1]) == fila):
        matriz_tablero[event]['letra'] = letra_turno
        window.Element(event).Update(letra_turno)
        lista_de_posiciones.append(event)
    else:
        sg.Popup('La casilla valida es '+str(
                 columna+1)+','+str(fila))
    return lista_de_posiciones,matriz_tablero

def Letras_Vertical(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window):
    if(int(event.split(',')[0]) == columna) & (
       int(event.split(',')[1]) == fila+1):
        matriz_tablero[event]['letra'] = letra_turno
        window.Element(event).Update(letra_turno)
        lista_de_posiciones.append(event)
    else:
        sg.Popup('La casilla valida es '+str(
                 columna)+','+str(fila+1))
    return lista_de_posiciones,matriz_tablero
