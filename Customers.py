#I am using sqlite3 for my database it is self contained within this folder.
#To create the database from scratch, I have included the createDatabase function
#https://sqlite.org/index.html
import sqlite3


def createDatabase(cur):
    cur.execute("DROP TABLE IF EXISTS CUSTOMER;")
    cur.execute("DROP TABLE IF EXISTS CORDER;")
    cur.execute("CREATE TABLE CUSTOMER(	ID INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(25), totalNumberGoods INTEGER)") 
    cur.execute("CREATE TABLE CORDER( customerId INTEGER, amountGoodsPurchased INTEGER)")
    arr= cur.fetchall()

def retrieveAllCustomers(cur):
    cur.execute("SELECT * FROM CUSTOMER")
    return cur.fetchall()

def retrieveAllOrders(cur):
    return cur.execute("SELECT * FROM CORDER").fetchall()
     

def insertCustomer(cur, name):
    if(type(name) != str):
        raise ValueError('name not a string')
    data= (name, 0)
    cur.execute("INSERT INTO CUSTOMER (name, totalNumberGoods) VALUES(?,?)", data)

def insertOrder(cur, id, amountGoodsPurchased):
    if(type(id) != int):
        raise ValueError('id not an int')
    if(type(amountGoodsPurchased) != int):
        raise ValueError('amountGoodsPurchased not an int')
    customer_id = cur.execute("SELECT COUNT(*) FROM CUSTOMER WHERE ID = " + str(id)).fetchall()
    if(customer_id[0][0] == 0 ):
        raise ValueError('customer could not be found')
    data = (customer_id[0][0], amountGoodsPurchased)
    cur.execute("INSERT INTO CORDER VALUES(?,?)", data)


# conn = sqlite3.connect('customer.db')
# cursor = conn.cursor()
# createDatabase(cursor)
# insertCustomer(cursor, "Peyton")
# insertCustomer(cursor, "Collin")
# insertOrder(cursor, 1, 6)
# print(retrieveAllOrders(cursor))


