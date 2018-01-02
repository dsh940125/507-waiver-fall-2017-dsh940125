# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

table = input()
if table == 'orders':
    con = input()

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()
if table == 'customers':
    query = "SELECT Id, CompanyName FROM Customer"
    r = cur.execute(query)
    print('ID', '      Customer Name')
    for row in r:
        print (row[0],'    ', row[1])
if table == 'orders' and con.startswith('cust'):
    cust = con[5:]
    query = "SELECT OrderDate FROM [Order] WHERE CustomerId={}".format("'"+cust+"'")
    r = cur.execute(query)
    print('Order Dates')
    for row in r:
        print (row[0])
if table == 'employees':
    query = "SELECT Id, FirstName, LastName FROM Employee"
    r = cur.execute(query)
    print('ID', '      Employee Name')
    for row in r:
        print (row[0],'      ', row[1], ' ', row[2])
if table == 'orders' and con.startswith('emp'):
    emp = con[4:]
    query = "SELECT [Order].OrderDate FROM [Order] JOIN Employee ON [Order].EmployeeId=[Employee].Id WHERE [Employee].LastName={}".format("'"+emp+"'")
    r = cur.execute(query)
    print('Order Dates')
    for row in r:
        print (row[0])
conn.close()    
