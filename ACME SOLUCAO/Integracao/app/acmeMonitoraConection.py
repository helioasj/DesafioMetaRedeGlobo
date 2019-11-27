import sqlite3
from sqlite3 import Error
import config

def open():
    cfg = ConfigParser.ConfigParser()
    cfg.read('acmeMonitoraDb.ini')
    host = cfg.getint('section1', 'host')

    conn = None
    try:
        conn = sqlite3.connect(host)
    except Error as e:
        print(e)

    return conn
