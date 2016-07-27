import unittest
from series import maclaurin
from utils  import functions

class test_maclaurin_factor(unittest.TestCase):

  def test_maclaurin_factor_0(self):
    self.assertEqual(maclaurin.maclaurin_factor(0), 1)

  def test_maclaurin_factor_1(self):
    self.assertEqual(maclaurin.maclaurin_factor(1), 0.5)

  def test_maclaurin_factor_2(self):
    self.assertEqual(maclaurin.maclaurin_factor(2), -0.125)

  def test_maclaurin_factor_3(self):
    self.assertEqual(maclaurin.maclaurin_factor(3), 0.0625)

  def test_maclaurin_factor_4(self):
    self.assertEqual(maclaurin.maclaurin_factor(4), -0.0390625)

  def test_maclaurin_factor_5(self):
    self.assertEqual(maclaurin.maclaurin_factor(5), 0.02734375)

