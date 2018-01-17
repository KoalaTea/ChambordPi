import unittest
import mongoengine
#from flask import current_app
#from app import create_app as create_app_base
import app
from app.objects import users, drinks, orders
from flask_mongoengine import MongoEngine
from IPython import embed
from tests.makedatabase import make_database
TEST_DB_NAME = 'ChambordPi_testdb'

def create_app():
    return app.create_app(MONGODB_SETTINGS={'db': 'ChambordPiTesting'}, LOGIN_DISABLED=False, TESTING=True, CSRF_ENABLED=False)

#TODO test alchohol changes
class TestOrderDrink(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        make_database(TEST_DB_NAME)
        self.test_app = create_app().test_client()
        self.test_app.testing = True
        mongoengine.connection.disconnect()
        mongoengine.connection.connect(TEST_DB_NAME)
        #TODO run a database set up script here

    def test_pass(self):
        pass

    def test_order_page(self):
        print("APIGJRIPGJR")
        print(self.test_app.post('/login', data={'username':'koalatea',
                                           'password':'temporary2017koalatea'}))
        print('----------------')
        print(dir(self.test_app.session_transaction()))
        order = self.test_app.get('/review_order/Rum and Coke')
        print(order)
        order = self.test_app.post('/order_drink', data={'drink':'Rum and Coke',
                                                 'instructions':'test'})
        for order in orders.Order.objects():
            print(order)
        order = orders.Order.objects.get(username='koalatea')
        self.assertEqual(order.name, 'Rum and Coke')

    '''
    @classmethod
    def tearDownClass(self):
        if mongoengine.connection.get_db().name == TEST_DB_NAME:
            mongoengine.connection.get_db().client.drop_database(TEST_DB_NAME)
        else:
            print('not correct db')
    '''

if __name__ == '__main__':
    unittest.main()
