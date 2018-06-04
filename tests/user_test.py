import unittest
import mongoengine
#from flask import current_app
#from app import create_app as create_app_base
import app
from app.objects import users, drinks, orders
from flask_mongoengine import MongoEngine
from IPython import embed
from tests.makedatabase import make_database
import time
TEST_DB_NAME = 'ChambordPi_testdb'

def create_app():
    return app.create_app(MONGODB_SETTINGS={'db': 'ChambordPi_testdb'}, LOGIN_DISABLED=False,
        TESTING=True, CSRF_ENABLED=False)

#TODO test alchohol changes
class TestUserObject(unittest.TestCase):
    #TODO the make database is probably just being run too many times we are currently using
    #an actualy database, this may be slowing down tests not really a problem at the moment.
    @classmethod
    def setUpClass(self):
        make_database(TEST_DB_NAME)
        self.test_app = create_app().test_client()
        self.test_app.testing = True
        self.user = users.User.objects.get(username='koalatea')

    def test_user_password_check(self):
        #TODO conver to grabbing a user from the db
        print(mongoengine.connection.get_db())
        user = users.User.objects.get(username='koalatea')
        self.assertTrue(self.user.validate_login(self.user.password, 'temporary2017koalatea'))

    def test_user_order_drink(self):
        users_orders = len(orders.Order.objects(username='koalatea'))
        start_credits = self.user.credits
        start_drinks = self.user.drinks_ordered
        drink = drinks.Drink.objects.get(name='Moscow Mule')
        self.user.order_drink(drink, "")
        self.assertEqual(start_credits - drink.cost, self.user.credits)
        self.assertEqual(start_drinks + 1, self.user.drinks_ordered)
        self.assertEqual(users_orders + 1, len(orders.Order.objects(username='koalatea')))

    #TODO
    def test_user_order_custom_drink(self):
        pass

    def test_cancel_order(self):
        start_credits = self.user.credits
        start_drinks = self.user.drinks_ordered
        drink = drinks.Drink.objects.get(name='Moscow Mule')
        order = orders.Order(username=self.user.username, status='queued', cost=drink.cost,
                recipe=drink.recipe, name=drink.name, image=drink.image,
                instructions='', order_type=drink.drink_type,
                time_ordered=int(time.time()))
        self.user.cancel_order(order)
        # TODO check for 0s? and fix
        self.assertEqual(start_credits + order.cost, self.user.credits)
        self.assertEqual(start_drinks - 1, self.user.drinks_ordered)

    # TO

    @classmethod
    def tearDownClass(self):
        pass
        '''
        if mongoengine.connection.get_db().name == TEST_DB_NAME:
            mongoengine.connection.get_db().client.drop_database(TEST_DB_NAME)
        else:
            print('not correct db')
        '''

if __name__ == '__main__':
    unittest.main()
