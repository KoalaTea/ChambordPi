import unittest
import app
from app.objects import users
from IPython import embed
from tests.makedatabase import make_database
from bs4 import BeautifulSoup
TEST_DB_NAME = 'ChambordPi_testdb'

def create_app():
    return app.create_app(MONGODB_SETTINGS={'db': TEST_DB_NAME}, LOGIN_DISABLED=False,
        TESTING=True, CSRF_ENABLED=False)

#TODO test alchohol changes
class TestPagesObject(unittest.TestCase):
    cookies = {}
    @classmethod
    def setUpClass(self):
        make_database(TEST_DB_NAME)
        self.test_app = create_app().test_client()
        self.test_app.testing = True

    # todo fix this so that we do not remake users
    def _login(self, role):
        roles = ["user"]
        if role != "user":
            roles.append(role)
        users.create_user("test_{}".format(role), "testpassword")
        self.user = users.User.objects.get(username='test_{}'.format(role))
        self.user.roles = roles
        self.user.save()

        login_data = {'username': 'test_{}'.format(role), 'password': 'testpassword'}
        r = self.test_app.get('/login')
        soup = BeautifulSoup(r.data, 'html.parser')
        csrf_token = soup.find('input', {'id': 'csrf_token'})['value']
        login_data['csrf_token'] = csrf_token

        r = self.test_app.post("/login", data=login_data)
        #embed()
