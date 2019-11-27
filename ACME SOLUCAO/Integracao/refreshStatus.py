import sqlite3
import requests
from sqlite3 import Error
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()



@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('Iniciando Refresh de Status...')

    database = r"/home/helio/Documents/Programas/Python/Meta Desafios/ACME SOLUCAO/Integracao/database/acme.db3"
    conn = None
    try:
      conn = sqlite3.connect(database)
    except Error as e:
      print(e)

    cur = conn.cursor()
    cur.execute("SELECT id,job_cod FROM leituratxt WHERE status_corte='Pendente'")

    rows = cur.fetchall()

    print('Listagem de Id`s de Videos com o Corte Pendente')
    if len(rows)==0:
        print('Nao ha Cortes Pendentes')
    for row in rows:
        print(row)
        r = requests.get('http://localhost:8000/videos/'+row[1])
        print(r.json())
        dados = (r.json()['status'],row[0])
        cur = conn.cursor()
        sql = '''UPDATE leituratxt SET status_corte=? WHERE id=?'''

        cur = conn.cursor()
        cur.execute(sql, dados)
        conn.commit()
        print('Status Atualizado!')



sched.start()


