import unittest

def check():
    return "specific_value"

class Test(unittest.TestCase):
    def test_check(self):
        self.assertEqual(check(), "specific_value2") # This will throw an error since the return of check() isn't the same as the provider value
        self.assertEqual(check(), "specific_value") # This won't throw an error
        
if __name__ == '__main__':
    unittest.main()