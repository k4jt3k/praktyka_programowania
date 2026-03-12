import unittest
from my_code import *


class TestMyMethods ( unittest . TestCase ):

    def test_one ( self ):
        self.assertEqual (Add('1') , 1)

    def test_two (self):
        self.assertEqual (Add('1,1') , 2)

    def test_three (self):
        self.assertEqual (Add('1,2,3,4,5') , 15)

    def test_four (self):
        self.assertEqual (Add('1\n2,3') , 6)

    #def test_five (self):
        #self.assertNotEqual (Add('1,\n') , 1)
    

unittest.main(argv=['first-arg-is-ignored'], exit=False)