import cx_Oracle
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('hello_world.conf')
USER = CONFIG['hello_world']['user']
PASS = CONFIG['hello_world']['pass']

connection = cx_Oracle.connect("SYSTEM", "oracle2019")

cursor = connection.cursor()
cursor.execute("""
    SELECT  ename, sal
    FROM    emp
    WHERE   mgr = 7839
""")
# Consulta practico 1, ejercicio 2
for ename, sal in cursor:
   print("Values:", ename, sal)
