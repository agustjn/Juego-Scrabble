'''class s:
    atril_jugador = {1: 1}
    atril_bot = {2: 2}

    def ya_mismo(self):
        print(1)

    def ahora_mismo(self, x):
        print(x)

    def mismo(self, cual):
        getattr(self, cual+'_mismo')()

    def var(self, quien, x):
        print(getattr(self, 'ahora_'+quien)(x))


a = s()
a.var('mismo', 5)'''

import PySimpleGUI as sg


layout = [[sg.Text('CASA', key='h')]]
w = sg.Window('Prueba').Layout(layout)
while True:
    e, v = w.Read(timeout=1000)
    print(w.Element('h').Get_Text())
