import unittest
import tests.test_csv_printer as test_csv_printer


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(test_csv_printer)
    unittest.TextTestRunner(verbosity=2).run(suite)