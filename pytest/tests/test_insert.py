import configparser
import cx_Oracle

CONFIG = configparser.ConfigParser()
CONFIG.read('../clase3.conf')
USER = CONFIG['clase3']['user']
PASS = CONFIG['clase3']['pass']
CONNECTION = cx_Oracle.connect(USER, PASS)

def test_mytab_must_have_7_items():
    cursor = CONNECTION.cursor()
    cursor.execute('SELECT * FROM mytab')
    res = cursor.fetchall()
    cursor.close()
    assert len(res) == 7

def test_first_item_must_have_id_1():
    cursor = CONNECTION.cursor()
    cursor.execute('SELECT id FROM mytab WHERE id=1')
    res = cursor.fetchall()[0][0]
    cursor.close()
    assert res == 1

def test_first_item_must_have_data():
    cursor = CONNECTION.cursor()
    cursor.execute('SELECT data FROM mytab WHERE id=1')
    res = cursor.fetchall()[0][0]
    cursor.close()
    assert res == 'First'
