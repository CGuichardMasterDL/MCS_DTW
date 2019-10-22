# -*- coding: utf-8 -*-

from .context import mcs_dtw
import unittest


class TestBasic(unittest.TestCase):

    def test_basic_true(self):
        self.assertTrue(True)

    def test_basic_import(self):
        self.assertTrue(mcs_dtw.is_imported())


if __name__ == '__main__':
    unittest.main()
