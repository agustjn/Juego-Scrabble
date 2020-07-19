from json import dump, load
from time import strftime

partida_json = 'archivos/partida.json'
records_json = 'archivos/records.json'
records_txt = 'archivos/records.txt'


class Archivos():

    def __init__(self):
        ''' CREA LOS ARCHIVOS A USAR DURANTE EL PROGRAMA'''
        try:
            with open(partida_json, 'x') as a:
                dump([], a)
        except FileExistsError:
            pass
        try:
            with open(records_json, 'x') as a:
                dump({}, a)
        except FileExistsError:
            pass

    def escribir_json(self, data, enlace, abrir_en):
        ''' REALIZA UN DUMP DE LA INFORMACIÓN SOBRE EL ARCHIVO
            CON LA EXTENSIÓN PASADOS POR PARÁMETRO'''
        with open(enlace, abrir_en) as a:
            dump(data, a, indent=4)

    def leer_json(self, enlace):
        ''' DEVUELVE LA INFORMACIÓN LEÍDA DESDE EL ARCHIVO'''
        with open(enlace) as a:
            return load(a)

    def escribir_txt(self, data, enlace, abrir_en):
        ''' ITERA SOBRE LA INFORMACIÓN Y LA ESCRIBE SOBRE EL
            ARCHIVO CON LA EXTENSIÓN PASADOS POR PARÁMETRO'''
        with open(enlace, abrir_en) as a:
            for linea in data:
                a.write(linea)

    def leer_txt(self, enlace):
        ''' DEVUELVE LA INFORMACIÓN LEÍDA DESDE EL ARCHIVO'''
        with open(enlace) as a:
            return a.read()

    def cargar_records_json(self, puntos, dificultad):
        ''' ORDENA EL TOP 10 EXISTENTE CON EL RECORD ENTRANTE Y LOS CARGA'''
        records = self.leer_json(records_json)
        records.append({'puntos': puntos,
                        'fecha': strftime('%d/%m/%Y'),
                        'dificultad': dificultad})
        if len(records) == 11:
            records.remove(records[-1])
        self.escribir_json(records, records_json, 'w')

    def cargar_records_txt(self):
        ''' DEVUELVE LOS RECORDS EN FORMATO DE TEXTO'''
        records = self.leer_json(records_json)
        if not records:
            return 'NO HAY RECORDS'
        for record in records:
            self.escribir_txt('Puntos: {}\nFecha: {}\nDificultad: {}\n\n'.
                              format(record['puntos'],
                                     record['fecha'],
                                     record['dificultad']), records_txt, 'a')
        return self.leer_txt(records_txt)
