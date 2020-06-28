
def Evaluar_Posiciones(window,x,y,pos,palabra_cpu,matriz_tablero):

    if pos==0:
        for i in range(len(palabra_cpu)):
            if (x+i,y) in matriz_tablero:
                if window.Element((x+i,y)).GetText() !='':
                    return 'No Valido'
            else:
                return 'No Valido'
        return 'Horizontal'
    else:
        for i in range(len(palabra_cpu)):
            if (x,y+i) in matriz_tablero:
                if window.Element((x+i,y)).GetText() !='':
                    return 'No Valido'
            else:
                return 'No Valido'
        return 'Vertical'

def Colocar_Letras(window,lista_palabra_cpu,x,y,pos,palabra_cpu):
    lista_palabra_cpu=[]

    for letra in palabra_cpu:
        lista_palabra_cpu.append(letra)
    if pos==0:
        for i in range(len(lista_palabra_cpu)):
            window.Element((x,y)).Update(lista_palabra_cpu[i])
            y+=1
    else:
        for i in range(len(lista_palabra_cpu)):
            window.Element((x,y)).Update(lista_palabra_cpu[i])
            x+=1

'''
if es_valida:
    print('es valida')
    lista_palabra_cpu=[]
    col=casilla_cpu[0]
    fila=casilla_cpu[1]
    for letra in palabra_cpu:
        lista_palabra_cpu.append(letra)
    for i in range(len(lista_palabra_cpu)):
        window.Element((col,fila)).Update(lista_palabra_cpu[i])
        fila+=1
else:
    es_valida=True
    for i in range(len(palabra_cpu)):
        if window.Element((x,y)).GetText() !='':
            es_valida=False
            break
        x+=1
        if es_valida:
            print('es valida')
            lista_palabra_cpu=[]
            col=casilla_cpu[0]
            fila=casilla_cpu[1]
            for letra in palabra_cpu:
                lista_palabra_cpu.append(letra)
            for i in range(len(lista_palabra_cpu)):
                window.Element((col,fila)).Update(lista_palabra_cpu[i])
                col+=1'''
