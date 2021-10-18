from Customers import *

import unittest
from unittest.mock import MagicMock,Mock

class CustomersTest(unittest.TestCase):
    #Mock
    def test_retrieve_orders(self):
        cur = Mock()
        cur.execute("SELECT * FROM CORDER").fetchall = MagicMock(return_value=[(1, 6), (3,9)])
        self.assertEqual(retrieveAllOrders(cur),[(1, 6), (3,9)])

    #Spy
    def test_regular_insert_customer(self):
        cur = Mock()
        insertCustomer(cur, "Peyton")
        self.assertEqual(str(cur.mock_calls[0])[76:-6],"Peyton")
    
    #Mock #Spy
    def test_regular_insert_order(self):
        cur = Mock()
        cur.execute("SELECT COUNT(*) FROM CUSTOMER WHERE ID = 1").fetchall = MagicMock(return_value=[(1,)])
        insertOrder(cur, 1, 1)
        self.assertEqual(str(cur.mock_calls[3])[48:-2],"1, 1")

    #Dummy
    def test_wrong_type_insert_customer(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            insertCustomer(cur, 13)

    #Mock
    def test_customer_not_found_order(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            cur.execute("SELECT COUNT(*) FROM CUSTOMER WHERE id = 13").fetchall = MagicMock(return_value=[(0,)])
            insertOrder(cur, 13, 1)

    #Dummy
    def test_wrong_type_insert_id_string_order(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            insertOrder(cur, "hi", 1)
    
    
    #Dummy
    def test_wrong_type_insert_id_float_order(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            insertOrder(cur, 3.4, 1)

    #Dummy
    def test_wrong_type_insert_amount_string_order(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            insertOrder(cur, 1, "1")

    #Dummy
    def test_wrong_type_insert_amount_float_order(self):
        with self.assertRaises(ValueError):
            cur = Mock()
            insertOrder(cur, 1, 3.4)
            

if __name__ == '__main__':
    unittest.main()