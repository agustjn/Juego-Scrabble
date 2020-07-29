from PySimpleGUI import Popup, PopupScrolled


class Popups:

    # Imprime un Popup con 'data' como valor.
    def popup(self, data):
        Popup(data,
              title='ScrabbleAR',
              custom_text='ACEPTAR',
              font=24,
              auto_close=True,
              auto_close_duration=10)

    def popup_scrolled(self, data):
        PopupScrolled(data,
                      title='ScrabbleAR',
                      size=(24, 18))
