import PySimpleGUI as sg
from modulo_verificacion import checkOrientation
#Restricciones para el jugador
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
#Fin de restricciones para el jugador

def Palabra_Invalida(listas,matriz_tablero,window): # esta funcion saca las letras del tablero si la palabra es invalida
    for i in range(len(listas['pos_en_atril'])):
        window.Element(listas['pos_en_atril'][i]).Update(
        listas['letras_en_tablero'][i])
        window.Element(listas['pos_en_tablero'][i]).Update('')
        matriz_tablero[listas['pos_en_tablero'][i]]['letra']=''
    return matriz_tablero

#Logica del CPU
def Evaluar_Posicion(window,casilla_cpu,palabra_cpu,matriz_tablero):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    print('columna = ', columna,' fila = ', fila,'ttttttttttttttttttt')
    horizontal = True
    vertical = True
    for i in range(len(palabra_cpu)):
        if (columna+i,fila) not in matriz_tablero:
            horizontal = False
            break
        else:
            if window.Element((columna+i,fila)).GetText()!='':
                horizontal = False
                break
    if horizontal:
        return 'Horizontal'
    else:

        for i in range(len(palabra_cpu)):
            if (columna,fila+i) not in matriz_tablero:
                vertical = False
                break
            else:
                if window.Element((columna,fila+i)).GetText()!='':
                    vertical = False
                    break
        if vertical:
            return 'Vertical'
    if not horizontal and not vertical:
        print(horizontal,vertical)
        return 'No Valido'
def Colocar_Letras(window,casilla_cpu,orientacion,palabra_cpu,matriz_tablero,cpu,listas):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    lista_eliminados=[]# lista de las letras que fueron colocadas en el atril
    pos_eliminados=[] # lista con la posicion de las letras del atril que fueron colocadas
    print(palabra_cpu)
    contador_letras={}# contador de letras para sacar del atril
    for letra in palabra_cpu:
        print(letra)
        if letra not in contador_letras:
            contador_letras[letra]=1
        else:
            contador_letras[letra]+=1

    print(contador_letras)

    keysAtril=[('Cpu',y)for y in range(7)]

    for key in keysAtril:
        if window.Element(key).GetText() in palabra_cpu:
            letra=window.Element(key).GetText()
            if lista_eliminados.count(letra)!=contador_letras[letra]:
                lista_eliminados.append(letra)
                pos_eliminados.append(key)
                window.Element(key).Update('')
    print('Letras eliminadas = ',lista_eliminados)
    print('Pos letras eliminadas = ',pos_eliminados)
    if orientacion=='Horizontal':
        for i in range(len(palabra_cpu)):
            window.Element((columna,fila)).Update(palabra_cpu[i])
            matriz_tablero[(columna,fila)]['letra']=palabra_cpu[i]
            listas['pos_en_tablero'].append((columna,fila))
            listas['letras_en_tablero'].append(palabra_cpu[i])
            listas['casillas'].append(matriz_tablero[(columna,fila)]['color_casilla'])
            listas['pos_en_atril']=pos_eliminados
            listas['puntos_por_letra'].append(cpu.bolsa_fichas[palabra_cpu[i]]['puntaje'])
            cpu.actualizarCasillaAtril(pos_eliminados[i][1])
            columna+=1
    else:
        for i in range(len(palabra_cpu)):
            window.Element((columna,fila)).Update(palabra_cpu[i])
            matriz_tablero[(columna,fila)]['letra']=palabra_cpu[i]
            listas['pos_en_tablero'].append((columna,fila))
            listas['letras_en_tablero'].append(palabra_cpu[i])
            listas['casillas'].append(matriz_tablero[(columna,fila)]['color_casilla'])
            listas['pos_en_atril']=pos_eliminados
            listas['puntos_por_letra'].append(cpu.bolsa_fichas[palabra_cpu[i]]['puntaje'])
            cpu.actualizarCasillaAtril(pos_eliminados[i][1])
            fila+=1
    return matriz_tablero
#Fin de Logica CPU
