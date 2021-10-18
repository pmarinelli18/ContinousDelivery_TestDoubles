from SumIntegers import *

import unittest
from unittest.mock import MagicMock,Mock

class SumIntegersTest(unittest.TestCase):
    #Mock #Spy
    def test_regular_output_without_newline(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['2\n', '1\n', '3\n', '1'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"7")

    #Mock #Spy
    def test_regular_output_with_newline(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['2\n', '1\n', '3\n', '1\n'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"7")

    #Mock #Spy
    def test_regular_negative_integer(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['2\n', '-1\n', '3\n', '1'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"5")

    #Mock #Spy
    def test_regular_positive_integer(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['2\n', '+1\n', '3\n', '1'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"7")

    #Mock #Spy
    def test_regular_output_with_random_enters(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['2\n', '1\n', '\n', '3\n', '1\n'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"7")

    #Mock #Spy
    def test_empty_file(self):
        f = Mock()
        f.readlines = MagicMock(return_value=['\n', '\n'])
        getTotal(f)
        self.assertEqual(str(f.mock_calls[1])[19:-2],"0")

    #Mock
    def test_non_digit_character(self):
        with self.assertRaises(ValueError):
            f = Mock()
            f.readlines = MagicMock(return_value=['2\n', '1\n', '3\n', 'hi'])
            getTotal(f)

    #Mock
    def test_closed_file(self):
        with self.assertRaises(ValueError):
            f = Mock()
            f.closed = True
            getTotal(f)

if __name__ == '__main__':
    unittest.main()