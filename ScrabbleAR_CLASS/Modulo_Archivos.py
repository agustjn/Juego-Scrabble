from time import strftime
from os import startfile
from const import *
import json


class Archivos():

    # Inicializa los .JSON 'enlaces' con una lista vacía,
    # enlaces = [enlace i del archivo i a manipular durante el programa]
    def __init__(self, enlaces):
        for enlace in enlaces:
            try:
                archivo = open(enlace, 'x')
                json.dump([], archivo)
                archivo.close()
            except FileExistsError:
                pass

    # Hace un solo dump de la información entrante 'data',
    # en el archivo 'enlace' y en modo 'abrir_en'
    def escribir_json(self, data, enlace, abrir_en):
        archivo = open(enlace, abrir_en)
        json.dump(data, archivo, indent=4)
        archivo.close()

    def leer_json(self, enlace):
        archivo = open(enlace)
        data = json.load(archivo)
        archivo.close()
        return data

    # Escribe cada elemento de la lista 'data'
    # en el archivo 'enlace' y en modo 'abrir_en'
    def escribir_txt(self, data, enlace, abrir_en):
        archivo = open(enlace, abrir_en)
        for linea in data:
            archivo.write(linea)
        archivo.close()

    # Carga el record al finalizar el programa.
    def cargar_record(self, parametros_juego):
        records = self.leer_json(top_diez_json)
        records.append({'puntaje': 0, 'fecha': strftime('%d/%m/%Y'), 'dificultad': parametros_juego})
        self.escribir_json(records, top_diez_json, 'w')

    # Toma todos los records actuales y los ordena. Carga
    # solo los primeros 10 en un .txt y lo abre.
    def ver_top_diez(self):
        puntuaciones = self.leer_json(top_diez_json)
        if not puntuaciones:
            return False
        puntuaciones.sort(key=lambda data: data['puntaje'])
        top_diez, cont = [], 0
        for record in puntuaciones:
            top_diez.append(record)
            cont += 1
            if cont == 10:
                break
        self.escribir_txt(top_diez_txt_format(top_diez), top_diez_txt, 'w')
        try:
            startfile(top_diez_txt)
            # import os, sys, subprocess
            #     def open_file(top_diez_txt):
            #         if sys.platform == "win32":
            #             os.startfile(top_diez_txt)
            #         else:
            #             opener ="open" if sys.platform == "darwin" else "xdg-open"
            #             subprocess.call([opener, top_diez_txt])
        except FileNotFoundError:
            return False
        return True
