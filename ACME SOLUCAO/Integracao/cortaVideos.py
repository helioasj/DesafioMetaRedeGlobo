import sqlite3
import requests
import shutil
import requests
from sqlite3 import Error
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()



@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('Iniciando Corte...')

    database = r"/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/CORTE-API/corte_api/db.sqlite3"
    conn = None
    try:
      conn = sqlite3.connect(database)
    except Error as e:
      print(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM corteapp_videos WHERE status='Pendente'")

    rows = cur.fetchall()

    print('Listagem de Videos com o Corte Pendente')
    if len(rows)==0:
        print('Nao ha Cortes Pendentes')
    for row in rows:
        print(row)
        filePathDe = row[6]
        filePathPara =  '/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/CORTE-API/videos/cortados/'
        print('-------------')
        print(filePathDe)
        print(filePathPara)
        print('-------------')
        shutil.copy(filePathDe,filePathPara)
        print('Arquivos Recordados e Movidos para diretorio determinado')
        r = requests.post('http://127.0.0.1:8001/acmeplay/', data = {'titulo': row[1], 'duracao': row[6], 'nome_arquivo': row[2]})

        dados = ('Concluido',row[0])
        print('Informacoes em Dados:')
        print(dados)
        cur = conn.cursor()
        sql = '''UPDATE corteapp_videos SET status=? WHERE id=?'''

        cur = conn.cursor()
        cur.execute(sql, dados)
        conn.commit()
        print('Status Atualizado!')





sched.start()


