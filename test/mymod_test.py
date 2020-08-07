# writting some code using unittest to test enlarge function works

import unittest
from my_lamdata.mymod import enlarge

class TestMymod(unittest.TestCase):

    def test_enlarge(self):
        
        self.assertEqual(enlarge(9), 900)

if __name__ == '__main__':
    unittest.main()