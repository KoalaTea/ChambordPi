import unittest

TEST_MODULES = [
    'tests.auth_test',
    #'tests.user_test',
    #'tests.test_pages'
    ]

suite = unittest.TestSuite()

for t in TEST_MODULES:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
