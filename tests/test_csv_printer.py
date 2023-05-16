"""Tests of the CSVPrinter.

Author: Thanatibordee Sihaboonthong
"""

import unittest
from SDlab_exercise1_1.csv_printer import CSVPrinter

def setUpModule():
    print('Running setUpModule')

def tearDownModule():
    print('Running tearDownModule')

class TestCSVPrinter(unittest.TestCase):
    """Tests of the CSVPrinter class."""

    @classmethod
    def setUpClass(cls):
        """Set up an CSVPrinter before each test."""
        print('Running setUpClass')

        cls.csv_printer = CSVPrinter("sample.csv")

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    def setUp(self):
        print('Running setUp')

    def tearDown(self):
        print('Running tearDown')

    def test_read1(self):
        """TestMethod1: All the lines should be dealt with by the CSVPrinter."""
        print('Running test_read1')

        l = self.csv_printer.read()

        self.assertEqual(len(l), 3)

    def test_read2(self):
        """TestMethod2: Separated elements in each line should be returned."""
        print('Running test_read2')
        
        expected = [['value1A', ' value1B', ' value1C'], ['value1A', ' value2B', ' value2C'], ['value1A', ' value3B', ' value3C']]

        l = self.csv_printer.read()

        for i, line in enumerate(l):
            self.assertEqual(len(line), 3)
            for j, element in enumerate(line):
                self.assertEqual(element, expected[i][j])

    def test_read3(self):
        """TestMethod3: CSVPrinter should throw an exception when it receives an input file that does not exist"""
        print('Running test_read3')
        
        with self.assertRaises(FileNotFoundError):
            self.csv_printer.file_name = "invalid.csv"
            l = self.csv_printer.read()

    