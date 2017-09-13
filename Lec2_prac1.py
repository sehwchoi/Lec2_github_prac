import unittest

def subtract_one(value):
    result = value - 1
    if result < 0:
        return 0
    else:
        return result
    
class FunctionTests(unittest.TestCase):
    def setUp(self):
       pass
       
    def test_subtr_function(self):
        self.assertEqual(subtract_one(3), 2, "Testing if my subtract_one fuction gives me good output")

    def test_neg_number(self):
        self.assertEqual(subtract_one(0)), 0, "Testing function with "
    
    def tearDown(self):

unittest.main(verbosity=2)