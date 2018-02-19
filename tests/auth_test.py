import unittest
import mongoengine
#from flask import current_app
#from app import create_app as create_app_base
import app
from app.objects import users, drinks, orders
from flask_mongoengine import MongoEngine
from IPython import embed
from tests.makedatabase import make_database
from bs4 import BeautifulSoup
TEST_DB_NAME = 'ChambordPi_testdb'

def create_app():
    return app.create_app(MONGODB_SETTINGS={'db': 'ChambordPi_testdb'}, LOGIN_DISABLED=False, TESTING=True)

#TODO test alchohol changes
class Test(unittest.TestCase):
    def setUp(self):
        make_database(TEST_DB_NAME)
        self.app = create_app()
        self.test_app = create_app().test_client()
        self.test_app.testing = True
        #TODO run a database set up script here

    def test_login_page_exists(self):
        resp = self.test_app.get('/login')
        self.assertEqual(resp.status_code, 200)

    def test_signup_exists(self):
        resp = self.test_app.get('/signup')
        self.assertEqual(resp.status_code, 200)

    def test_login_csrf(self):
        # verify lack of csrf fails
        login_data = {'username': 'bartender', 'password': 'bartender'}
        resp = self.test_app.post('/login', data=login_data)
        soup = BeautifulSoup(resp.data, 'html.parser')
        self.assertEqual(soup.find(text='Login Failed'), 'Login Failed')
        # verify csrf token works
        resp = self.test_app.get('/login')
        soup = BeautifulSoup(resp.data, 'html.parser')
        csrf_token = soup.find('input', {'id': 'csrf_token'})['value']
        login_data['csrf_token'] = csrf_token
        resp = self.test_app.post('/login', data=login_data)
        self.assertEqual(resp.status_code, 302)

    def tearDown(self):
        if mongoengine.connection.get_db().name == TEST_DB_NAME:
            mongoengine.connection.get_db().client.drop_database(TEST_DB_NAME)
        else:
            print('not correct db')

if __name__ == '__main__':
    unittest.main()
