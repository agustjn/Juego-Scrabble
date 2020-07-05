
def Evaluar_Posicion(window,casilla_cpu,palabra_cpu,matriz_tablero):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    print('columna = ', columna,' fila = ', fila,'ttttttttttttttttttt')
    horizontal = True
    vertical = True
    #(0,0)
    for i in range(len(palabra_cpu)):
        if (columna+i,fila) not in matriz_tablero:
            horizontal = False
            break
        else:
            if window.Element((columna+i,fila)).GetText()!='':
             #matriz_tablero[(columna+i,fila)]['letra']!='':
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
                #matriz_tablero[(columna,fila+i)]['letra']!='':
                    vertical = False
                    break
        if vertical:
            return 'Vertical'
    if not horizontal and not vertical:
        print(horizontal,vertical)
        return 'No Valido'
def Colocar_Letras(window,lista_palabra_cpu,casilla_cpu,orientacion,palabra_cpu,matriz_tablero,cpu,listas):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    lista_palabra_cpu=[] # lista para colocar las letras en orden
    lista_eliminados=[]# lista de las letras que fueron colocadas en el atril
    pos_eliminados=[] # lista con la posicion de las letras del atril que fueron colocadas

    contador_letras={}# contador de letras para sacar del atril
    for letra in palabra_cpu:
        print(letra)
        if letra not in contador_letras:
            contador_letras[letra]=1
        else:
            contador_letras[letra]+=1

    print(contador_letras)

    keysAtril=[('Cpu',y)for y in range(7)]
    for letra in palabra_cpu:
        lista_palabra_cpu.append(letra)

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
        for i in range(len(lista_palabra_cpu)):
            window.Element((columna,fila)).Update(lista_palabra_cpu[i])
            matriz_tablero[(columna,fila)]['letra']=lista_palabra_cpu[i]
            listas['pos_en_tablero'].append((columna,fila))
            listas['letras_en_tablero'].append(lista_palabra_cpu[i])
            listas['casillas'].append(matriz_tablero[(columna,fila)]['color_casilla'])
            listas['pos_en_atril']=pos_eliminados
            listas['puntos_por_letra'].append(cpu.bolsa_fichas[lista_palabra_cpu[i]]['puntaje'])
            cpu.actualizarCasillaAtril(pos_eliminados[i][1])
            columna+=1
    else:
        for i in range(len(lista_palabra_cpu)):
            window.Element((columna,fila)).Update(lista_palabra_cpu[i])
            matriz_tablero[(columna,fila)]['letra']=lista_palabra_cpu[i]
            listas['pos_en_tablero'].append((columna,fila))
            listas['letras_en_tablero'].append(lista_palabra_cpu[i])
            listas['casillas'].append(matriz_tablero[(columna,fila)]['color_casilla'])
            listas['pos_en_atril']=pos_eliminados
            listas['puntos_por_letra'].append(cpu.bolsa_fichas[lista_palabra_cpu[i]]['puntaje'])
            cpu.actualizarCasillaAtril(pos_eliminados[i][1])
            fila+=1
    return matriz_tablero
