#!/usr/bin/env python3
import cx_Oracle
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('hello_world.conf')
USER = CONFIG['hello_world']['user']
PASS = CONFIG['hello_world']['pass']

connection = cx_Oracle.connect(USER, PASS)

cursor = connection.cursor()
cursor.execute("""
    SELECT  ename, sal
    FROM    emp
    WHERE   mgr =: mgrid""", mgrid=7839
)
# Consulta practico 1, ejercicio 2
col_names = [row[0] for row in cursor.description]
for ename, sal in cursor:
   print(f"{col_names[0]}: {ename} | {col_names[1]}: {sal}")
