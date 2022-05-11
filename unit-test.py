import test
import unittest

class Testclass(unittest.TestCase):
  def test_add(x):
    x.assertEqual(test.add(), 3)

if __name__ == "__main__":
  unittest.main()