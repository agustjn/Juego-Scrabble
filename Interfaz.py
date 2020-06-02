import PySimpleGUI as sg
import random
bolsa_letras={'A':11,'E':11,'O':8,'S':7,'I':6,'U':6,'N':5,'L':4,'R':4,'T':4,
              'C':4,'D':4,'G':2,'M':3,'B':2,'P':2,'F':2,'H':2,'V':2,'Y':1,
              'J':2,'K':1,'LL':1,'Ñ':1,'Q':1,'RR':1,'W':1,'X':1,'Z':1}
letras_juego=[]
for letra,cantidad in bolsa_letras.items():
    if(letra not in letras_juego):
        letras_juego.append(letra)

def InterfazAtril(letras_jugador):
    '''cont=0
    while (cont!=7):
        letra_random=letras_juego[random.randrange(0,len(letras_juego))]
        if (bolsa_letras[letra_random]==0):
            repetida=letra_random
            while(letra_random==repetida):
                letra_random=letras_juego[random.randrange(0,len(letras_juego))]
        bolsa_letras[letra_random]-=1
        letras_jugador.append(letra_random)
        cont+=1'''
    letras=[[sg.Button(letras_jugador[x],key=str(x),size=(5,3))]for x in range(7)
    ]
    botones_especiales=[[sg.Button('Cambiar Fichas')],[sg.Button('Fin De Turno')]

    ]
    layout=[[sg.Column(letras)],[sg.Column(botones_especiales)]

    ]
    #print(bolsa_letras)
    window=sg.Window('Atril').Layout(layout)
    return window
