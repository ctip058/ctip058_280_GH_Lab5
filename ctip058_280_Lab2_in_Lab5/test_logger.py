import unittest     # Import the Python unit testing framework
from logger import Logger       # Our code to test
    
some = ""

def set_some(a_string):
    global some
    some = a_string

class LoggerTest(unittest.TestCase):
    '''Unit tests for our logger functions. '''
       
    def test_info(self):
        '''Tests the info function'''
        log = Logger(set_some)
        log.info("text")
        self.assertEqual(some, "[INFO] text", "Info function didn't log correctly")
        
    
    def test_error(self):
        '''Tests the error function'''
        log = Logger(set_some)
        log.error("text")
        self.assertEqual(some, "[WARNING] text", "Error function didn't log correctly")
        