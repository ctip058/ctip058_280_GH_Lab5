import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(5, 6)
        self.assertEqual(result, 11, "Add function returned an incorrect result")
        
    def test_add_base_below_10(self):
        '''Tests the optional parameter for a base below 10'''
        result = maths.add(5, 6, 2)
        self.assertEqual(result, "1011", "Add function returned an incorrect result for the base")
        
    def test_add_base_above_10(self):
        '''Tests the optional parameter for a base above 10'''
        result = maths.add(5, 6, 16)
        self.assertEqual(result, "B", "Add function returned an incorrect result for the base")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, 5, "Fibonacci function returned an incorrect result")

    def test_convert_base_2(self):
        '''Tests the convert_base with base 2'''
        result = maths.convert_base(10, 2)
        self.assertEqual(result, "1010", "Convert base function did not convert to base 2")
        
    def test_convert_base_3(self):
        '''Tests the convert_base with base 3'''
        result = maths.convert_base(11, 3)
        self.assertEqual(result, "102", "Convert base function did not convert to base 3")
        
    def test_convert_base_4(self):
        '''Tests the convert_base with base 4'''
        result = maths.convert_base(12, 4)
        self.assertEqual(result, "30", "Convert base function did not convert to base 4")
        
    def test_convert_base_5(self):
        '''Tests the convert_base with base 5'''
        result = maths.convert_base(13, 5)
        self.assertEqual(result, "23", "Convert base function did not convert to base 5")
        
    def test_convert_base_6(self):
        '''Tests the convert_base with base 6'''
        result = maths.convert_base(14, 6)
        self.assertEqual(result, "22", "Convert base function did not convert to base 6")
        
    def test_convert_base_7(self):
        '''Tests the convert_base with base 7'''
        result = maths.convert_base(15, 7)
        self.assertEqual(result, "21", "Convert base function did not convert to base 7")
        
    def test_convert_base_8(self):
        '''Tests the convert_base with base 8'''
        result = maths.convert_base(16, 8)
        self.assertEqual(result, "20", "Convert base function did not convert to base 8")
        
    def test_convert_base_9(self):
        '''Tests the convert_base with base 9'''
        result = maths.convert_base(17, 9)
        self.assertEqual(result, "18", "Convert base function did not convert to base 9")
        
    def test_convert_base_11(self):
        '''Tests the convert_base with base 11'''
        result = maths.convert_base(40, 11)
        self.assertEqual(result, "37", "Convert base function did not convert to base 11")
        
    def test_convert_base_12(self):
        '''Tests the convert_base with base 12'''
        result = maths.convert_base(47, 12)
        self.assertEqual(result, "3B", "Convert base function did not convert to base 12")
        
    def test_convert_base_13(self):
        '''Tests the convert_base with base 13'''
        result = maths.convert_base(54, 13)
        self.assertEqual(result, "42", "Convert base function did not convert to base 13")
        
    def test_convert_base_14(self):
        '''Tests the convert_base with base 14'''
        result = maths.convert_base(61, 14)
        self.assertEqual(result, "45", "Convert base function did not convert to base 14")
        
    def test_convert_base_15(self):
        '''Tests the convert_base with base 15'''
        result = maths.convert_base(68, 15)
        self.assertEqual(result, "48", "Convert base function did not convert to base 15")
        
    def test_convert_base_16(self):
        '''Tests the convert_base with base 16'''
        result = maths.convert_base(75, 16)
        self.assertEqual(result, "4B", "Convert base function did not convert to base 16")
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
