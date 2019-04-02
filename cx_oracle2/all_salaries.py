#!/usr/bin/env python3
import cx_Oracle
import configparser
from bottle import route, run, template, get, post, error

CONFIG = configparser.ConfigParser()
CONFIG.read('hello_world.conf')
USER = CONFIG['hello_world']['user']
PASS = CONFIG['hello_world']['pass']
HOST = CONFIG['bottle']['host']
PORT = CONFIG['bottle']['port']
DEBUG = CONFIG['bottle']['debug']

CONNECTION = cx_Oracle.connect(USER, PASS)
CURSOR = CONNECTION.cursor()

@route('/salarios')
def get_all_salaries():
    CURSOR.execute("""SELECT ename, sal FROM emp""")
    result = CURSOR.fetchall()
    col_names = [row[0] for row in CURSOR.description]
    CURSOR.close()
    return template("views/all_salaries", col_names=col_names, rows=result)

@route('/')
@route('/welcome/<name>')
def greet(name='Stranger'):
    return template('Welcome {{name}}', name=name)

@get('/login') # o @route('/login')
def login():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    """

@post('/login') # o @route('/login', method='POST')
def do_login():
    return "Login correct"

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host=HOST, port=PORT, debug=DEBUG)
