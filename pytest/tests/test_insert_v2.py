import configparser
import cx_Oracle

class TestInsert:

    @classmethod
    def setup_class(cls):
        CONFIG = configparser.ConfigParser()
        CONFIG.read('../clase3.conf')
        USER = CONFIG['clase3']['user']
        PASS = CONFIG['clase3']['pass']
        CONNECTION = cx_Oracle.connect(USER, PASS)
        cls.cursor = CONNECTION.cursor()

    @classmethod
    def teardown_class(cls):
        cls.cursor.close()

    def test_mytab_must_have_7_items(self):
        self.cursor.execute('SELECT * FROM mytab')
        res = self.cursor.fetchall()
        assert len(res) == 7

    def test_first_item_must_have_id_1(self):
        self.cursor.execute('SELECT id FROM mytab WHERE id=1')
        res = self.cursor.fetchall()[0][0]
        assert res == 1

    def test_first_item_must_have_data(self):
        self.cursor.execute('SELECT data FROM mytab WHERE id=1')
        res = self.cursor.fetchall()[0][0]
        assert res == 'First'
