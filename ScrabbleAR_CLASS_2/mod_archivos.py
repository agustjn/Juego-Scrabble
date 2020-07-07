from json import dump, load
from time import strftime

partida_json = 'archivos/partida.json'
records_json = 'archivos/records.json'
records_txt = 'archivos/records.txt'


class Archivos():

    def __init__(self, enlaces=[partida_json,
                                records_json,
                                records_txt]):
        ''' INICIALIZA LOS ARCHIVOS PASADOR POR PARAMETRO.
            HAY PREDETERMINADOS ESCRITOS.'''
        try:
            archivo = open(records_json, 'x')
            dump({}, archivo)
            archivo.close()
        except FileExistsError:
            pass
        try:
            archivo = open(partida_json, 'x')
            dump({}, archivo)
            archivo.close()
        except FileExistsError:
            pass
        archivo = open(records_txt, 'w')
        archivo.close()
        # Se puede producir un error relacionado a esto
        # sobre la carga de records.
        # for enlace in enlaces:
            # tipo = enlace.split('.')[-1]
            # try:
                # if tipo == 'json':
                    # archivo = open(enlace, 'x')
                    # dump({}, archivo)
                # else:
                    # archivo = open(enlace, 'w')
                # archivo.close()
            # except FileExistsError:
                # pass

    def escribir_json(self, data, enlace, abrir_en):
        ''' REALIZA UN DUMP DE LA INFORMACIÓN SOBRE EL ENLACE
            CON LA EXTENSIÓN PASADOS POR PARÁMETRO'''
        archivo = open(enlace, abrir_en)
        dump(data, archivo, indent=4)
        archivo.close()

    def leer_json(self, enlace):
        ''' DEVUELVE LA INFORMACIÓN LEÍDA DESDE EL ENLACE'''
        archivo = open(enlace)
        data = load(archivo)
        archivo.close()
        return data

    def escribir_txt(self, data, enlace, abrir_en):
        ''' ITERA SOBRE LA INFORMACIÓN PASADA POR PARÁMETRO Y LA ESCRIBE
            SOBRE EL ENLACE CON LA EXTENSIÓN PASADA POR PARÁMETRO'''
        archivo = open(enlace, abrir_en)
        for linea in data:
            archivo.write(linea)
        archivo.close()

    def leer_txt(self, enlace):
        ''' DEVUELVE LA INFORMACIÓN LEÍDA DESDE EL ENLACE'''
        archivo = open(enlace)
        data = archivo.read()
        archivo.close()
        return data

    def cargar_records_json(self, puntos, dificultad):
        ''' ORDENA EL TOP 10 EXISTENTE CON EL RECORD ENTRANTE Y LOS CARGA'''
        records = self.leer_json(records_json)
        records.append({'puntos': puntos,
                        'fecha': strftime('%d/%m/%Y'),
                        'dificultad': dificultad})
        records.sort(key=lambda elem: elem['puntos'])
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
