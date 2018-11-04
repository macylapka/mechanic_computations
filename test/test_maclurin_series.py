import unittest
import sys
sys.path.append('series/')
sys.path.append('utils/')
import maclaurin
import utils

class test_maclaurin_series(unittest.TestCase):

  def test_maclaurin_series_0(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 0), 1)

  def test_maclaurin_series_1(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 1), 0.7660444431189781)

  def test_maclaurin_series_2(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 2), 0.7386768418212236)

  def test_maclaurin_series_3(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 3), 0.7322740394191096)

  def test_maclaurin_series_4(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 4), 0.7304015754171275)

  def test_maclaurin_series_5(self):
    self.assertEqual(maclaurin.maclaurin_series(utils.f1(50, 25, 20), 5), 0.7297882727154748)
