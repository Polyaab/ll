   import unittest
   from even_odd import is_even

   class TestEvenOdd(unittest.TestCase):

       def test_even(self):
           self.assertTrue(is_even(2))
           self.assertTrue(is_even(0))
           self.assertTrue(is_even(-4))

       def test_odd(self):
           self.assertFalse(is_even(3))
           self.assertFalse(is_even(-1))

   if __name__ == '__main__':
       unittest.main()
   
