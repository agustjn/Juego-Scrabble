from json import dump, load
from time import strftime

partida_json = 'partida.json'
records_json = 'records.json'
records_txt = 'records.txt'


class Archivos():

    def __init__(self):
        ''' CREA LOS ARCHIVOS A USAR DURANTE EL PROGRAMA.
            LA SENTENCIA 'with' CIERRA EL ARCHIVO AUTOMATICAMENTE
            AL FINALIZAR SU CICLO.'''
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
        open(records_txt, 'w').close()

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
        records = self.leer_json(records_json)  # CARGA LOS RECORDS ACTUALES
        records.append({'puntos': puntos,
                        'fecha': strftime('%d/%m/%Y'),
                        'dificultad': dificultad})
        records.sort(key=lambda i: i['puntos']) # ORDENA LOS RECORDS SEGÚN EL PUNTAJE
        if len(records) == 11:  # SOLO CARGA HASTA 10 (TOP 10) RECORDS
            records.remove(records[-1]) # REMUEVE EL ÚLTIMO SEGÚN EL ÓRDEN
        self.escribir_json(records, records_json, 'w')  # LOS REESCRIBE

    def cargar_records_txt(self):
        ''' DEVUELVE LOS RECORDS EN FORMATO DE TEXTO'''
        records = self.leer_json(records_json)  # CARGA LOS RECORDS
        if not records: # SI NO HAY RECORDS
            return 'NO HAY RECORDS'
        for record in records:  # POR CADA RECORD, SE LO ESCRIBE EN UN .txt
            self.escribir_txt('Puntos: {}\nFecha: {}\nDificultad: {}\n\n'.
                              format(record['puntos'],
                                     record['fecha'],
                                     record['dificultad']), records_txt, 'a')
        return self.leer_txt(records_txt)   # SE DEVUELVE LO ESCRITO EN ESE .txt
