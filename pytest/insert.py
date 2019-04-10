#https://github.com/oracle/python-cx_Oracle/blob/883262da074e7f6daf9c2d41d4ffa5a689939710/samples/tutorial/bind_insert.py

import cx_Oracle
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('clase3.conf')
USER = CONFIG['clase3']['user']
PASS = CONFIG['clase3']['pass']

connection = cx_Oracle.connect(USER, PASS)
cursor = connection.cursor()
rows = [(1, "First"), (2, "Second"),(3, "Third"), (4, "Fourth"),(5, "Fifth"), (6, "Sixth"), (7, "Seventh")]
cursor.execute("CREATE TABLE mytab(id NUMBER PRIMARY KEY deferrable, data VARCHAR(60))")
cursor.executemany("INSERT INTO mytab(id, data) values (:1, :2)", rows)
cursor.execute('SELECT * FROM mytab')
res = cursor.fetchall()
cursor.execute('COMMIT')
cursor.close()
