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
    return app.create_app(MONGODB_SETTINGS={'db': TEST_DB_NAME}, TESTING=True, CSRF_ENABLED=False)

#TODO test alchohol changes
class TestOrderDrink(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        make_database(TEST_DB_NAME)
        self.test_app = create_app().test_client()
        self.test_app.testing = True
        #TODO run a database set up script here

    def test_user_order(self):
        #TODO conver to grabbing a user from the db
        user = users.User.objects.get(username='koalatea')
        drink = drinks.Drink(name='test_drink', available=True, cost=20, times_ordered=0,
                             recipe={'nothing':'nothing'}, image='test.png', drink_type='mixed',
                             drink_id=1)
        user.order_drink(drink, 'just a silly line')
        self.assertEqual(user.credits, 999980)
        self.assertEqual(user.drinks_ordered, 1)
        self.assertEqual(len(orders.Order.objects()), 1)
        print(mongoengine.connection.get_db().name)

    @classmethod
    def tearDownClass(self):
        if mongoengine.connection.get_db().name == TEST_DB_NAME:
            mongoengine.connection.get_db().client.drop_database(TEST_DB_NAME)
        else:
            print('not correct db')

if __name__ == '__main__':
    unittest.main()
