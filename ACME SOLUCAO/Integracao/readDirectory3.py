import sys
import time
import re
import sqlite3
import requests
from sqlite3 import Error
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ManipuladorDeEventos(FileSystemEventHandler):

    def __init__(self, numeroLinha):
        self.numeroLinha = numeroLinha
        self.title = ''
        self.start_time = ''
        self.end_time = ''
        self.duration = ''
        self.reconcile_key = ''

    def setNumeroLinha(self,numeroLinha):
        self.numeroLinha = numeroLinha

    def getNumeroLinha(self):
        return self.numeroLinha

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setStartTime(self, start_time):
        self.start_time = start_time

    def getStartTime(self):
        return self.start_time

    def setEndTime(self, end_time):
        self.end_time = end_time

    def getEndTime(self):
        return self.end_time

    def setDurantion(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration

    def setReconcile_key(self, reconcile_key):
        self.reconcile_key = reconcile_key

    def getReconcile_key(self):
        return self.reconcile_key



    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def inserir(self,conn, dados):
        sql = ''' INSERT INTO leituratxt(title, start_time, end_time, duration, reconcile_key,status_corte)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, dados)
        return cur.lastrowid

    def gravaLeitura(self, dados):
        database = r"/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/Integracao/database/acme.db3"

        # create a database connection
        conn = self.create_connection(database)
        with conn:
            self.inserir(conn, dados)

    def getId(self, reconciley_key):
        database = r"/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/Integracao/database/acme.db3"
        conn = None
        try:
            conn = sqlite3.connect(database)
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT id FROM leituratxt WHERE reconcile_key=?", ((reconciley_key,)))

        rows = cur.fetchall()

        for row in rows:
            pass
            #print(row)
        return row[0]

    def updateId(self, dados):
        database = r"/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/Integracao/database/acme.db3"
        conn = None
        try:
            conn = sqlite3.connect(database)
        except Error as e:
            print(e)

        cur = conn.cursor()
        sql = '''UPDATE leituratxt SET job_cod=?, msg_retorno=?, status_corte='Pendente' WHERE id=?'''

        cur = conn.cursor()
        cur.execute(sql, dados)
        conn.commit()


    def on_created(self, event):
        #print(event.src_path)
        self.readFile(event.src_path)

    def readFile(self,src_path):
        print('Arquivo Criado:',str(src_path))
        f = open(src_path, 'r')
        g = 1
        for line in f:
            if g>self.getNumeroLinha():
                #print(str(self.getNumeroLinha())+ line)

                # Localiza o Title
                patternTitle = 'Event([ ]{10})([\D|\d]{33})'
                if re.search( patternTitle, line):
                    info = re.search(patternTitle, line)
                    title = info.group(2)
                    self.setTitle(title)
                    #print(str(self.getNumeroLinha())+title)

                # Localiza o startTime
                patternStartTime = 'P([ ]{4})([\d]{2}\/[\d]{2}\/[\d]{4} [\d]{2}\:[\d]{2}\:[\d]{2};[\d]{2})'
                if re.search( patternStartTime, line):
                    info = re.search(patternStartTime, line)
                    startTime = info.group(2)
                    self.setStartTime(startTime)
                    #print(str(self.getNumeroLinha())+startTime)

                # Localiza o endTime
                patternEndTime = ';([\d]{2} )([\d]{2}\/[\d]{2}\/[\d]{4} [\d]{2}\:[\d]{2}\:[\d]{2};[\d]{2})'
                if re.search(patternEndTime, line):
                    info = re.search(patternEndTime, line)
                    endTime = info.group(2)
                    self.setEndTime(endTime)
                    #print(str(self.getNumeroLinha()) + endTime)

                # Localiza a duration
                patternDuration = '([\d]{2}\:[\d]{2}\:[\d]{2};[\d]{2} )(S)'
                if re.search(patternDuration, line):
                    info = re.search(patternDuration, line)
                    duration = info.group(1)
                    self.setDurantion(duration)
                    #print(str(self.getNumeroLinha()) + duration)


                # Localiza a Reconcile Key
                patternReconcile_Key = '(\)|M\.)([\d\D]{31})([\d]{12}|[\d]{11})'
                if re.search(patternReconcile_Key, line):
                    info = re.search(patternReconcile_Key, line)
                    reconcileKey = info.group(3)
                    self.setReconcile_key(reconcileKey)
                    #print(str(self.getNumeroLinha()) + reconcileKey)

                dadosLeitura = (self.getTitle(),self.getStartTime(),self.getEndTime(),self.getDuration(),self.getReconcile_key(),'')
                path = '/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/CORTE-API/videos/originais/' + self.getReconcile_key()


                if len(dadosLeitura[0])>0:
                    self.gravaLeitura(dadosLeitura)
                    hora = self.getDuration()[0 : 2]
                    minuto = self.getDuration()[3 : 5]
                    segundo = self.getDuration()[6 : 8]
                    tempoTotal = (int(hora)*60)+(int(minuto))+(int(segundo)/60)

                    if tempoTotal>=30:
                        print(path)
                        print('Enviando Post:',dadosLeitura)
                        data = {'nome': dadosLeitura[0], 'path': path, 'start_time': dadosLeitura[1], 'end_time': dadosLeitura[2], 'duration': dadosLeitura[3]}

                        # Executando o Post para a API de Corte, apenas dos videos com mais de 30 min
                        r = requests.post('http://127.0.0.1:8000/videos/',  json = data)

                        id = self.getId(str(dadosLeitura[4]))
                        job_cod = r.json()['id']
                        job_msg = str(r.status_code) + ' - ' + str(r.reason)
                        dadosJob = (job_cod, job_msg, id)
                        self.updateId(dadosJob)

                    print(dadosLeitura, '---', len(dadosLeitura[0]), hora, minuto, segundo)

                self.setNumeroLinha(self.getNumeroLinha() + 1)
            g = g+1

eventos = ManipuladorDeEventos(1)
observador = Observer()
observador.schedule(eventos, sys.argv[1], recursive=False)
observador.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observador.unschedule(eventos)
    observador.stop()
observador.join()

