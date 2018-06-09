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
from . import TestPagesObject
import time
TEST_DB_NAME = 'ChambordPi_testdb'

def create_app():
    return app.create_app(MONGODB_SETTINGS={'db': 'ChambordPi_testdb'}, LOGIN_DISABLED=False,
                          TESTING=True)

#TODO test alchohol changes
class Test(TestPagesObject):
    def setUp(self):
        make_database(TEST_DB_NAME)
        self.app = create_app()
        self.test_app = create_app().test_client()
        self.test_app.testing = True

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
        # verify csrf token works and login works
        resp = self.test_app.get('/login')
        soup = BeautifulSoup(resp.data, 'html.parser')
        csrf_token = soup.find('input', {'id': 'csrf_token'})['value']
        login_data['csrf_token'] = csrf_token
        resp = self.test_app.post('/login', data=login_data)
        self.assertEqual(resp.status_code, 302)

    # TODO test empty data in another location
    # data for post requests to ensure it works
    post_datas = {
        'order_drink': {'drink': 'Moscow Mule', 'instructions': ''},
        'cancel_drink': {},
        'order_custom_drink': {},
        'order_complete': {},
        'admin/add_credits/bartender': {},
        'add_alcohol': {},
        'remove_alcohol': {},
        'update_order': {},
        'update_menu': {}
    }
    #TODO test pages for access
    def test_login_pages(self):
        # TODO I just do not feel like dealing with most of these locations
        #get_endpoints = ['recent_orders', 'review_order/Moscow Mule', 'custom_drink',
        #'admin/admin', 'admin/manage_credits', 'admin/add_credits/bartender', 'orders',
        get_endpoints = ['recent_orders', 'review_order/Moscow Mule',
            'admin/manage_credits', 'orders',
            'current_orders']
        post_endpoints = ['order_drink', 'cancel_drink']
        #post_endpoints = ['order_drink', 'cancel_drink', 'order_custom_drink', 'order_complete',
        #    'admin/add_credits/bartender', 'add_alcohol', 'remove_alcohol', 'update_order',
        #    'update_menu']
        try:
            for endpoint in get_endpoints:
                r = self.test_app.get('/{}'.format(endpoint))
                if r.status_code == 404:
                    print(endpoint)
                self.assertEqual(r.status_code, 302)
            for endpoint in post_endpoints:
                r = self.test_app.post('/{}'.format(endpoint), data=self.post_datas[endpoint])
                if r.status_code == 404:
                    print(endpoint)
                self.assertEqual(r.status_code, 302)
        except Exception as e:
            print('endpoint "{}" caused an error'.format(endpoint))
            raise e
        with self.test_app:
            self._login('admin')
            self.user.credits = 10000000000
            self.user.save()
            try:
                for endpoint in get_endpoints:
                    r = self.test_app.get('/{}'.format(endpoint))
                    if r.status_code == 403:
                        print('endpoint "{}" failed access'.format(endpoint))
                    self.assertEqual(r.status_code, 200)
            except Exception as e:
                print('endpoint "{}" caused an error'.format(endpoint))
                raise e
            # currently view page not returned
            order = orders.Order(name="Moscow Mule", cost=10, instructions="",
                username="test_admin", order_type="mixed", recipe=[{'test':'test'}],
                time_ordered=time.time(), status='queued')
            order.save()
            self.user.drinks_ordered += 1
            self.user.save()
            self.post_datas['cancel_drink']['order'] = order.id
            try:
                for endpoint in post_endpoints:
                    if r.status_code == 403:
                        print('endpoint "{}" failed access'.format(endpoint))
                    r = self.test_app.post('/{}'.format(endpoint), data=self.post_datas[endpoint])
                    self.assertEqual(r.status_code, 200)
            except Exception as e:
                print('endpoint "{}" caused an error'.format(endpoint))
                raise e


    def tearDown(self):
        pass
        '''
        if mongoengine.connection.get_db().name == TEST_DB_NAME:
            mongoengine.connection.get_db().client.drop_database(TEST_DB_NAME)
        else:
            print('not correct db')
        '''

if __name__ == '__main__':
    unittest.main()
