import unittest
from multiply import multiplication
class MultiplyTestcase(unittest.Test case):
  
  def test_1(self):

    result = multiplication(3,4)

    self.assertEqual(result, 12)

  def test_2(self):

    result = multiplication(3,-4)

    self.assertEqual(result, -12)

  if __name__ == '__main__':
    unittest.main()
