# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

def createConnection(dbfile):
	try:
		conn = sqlite3.connect(dbfile)
		return conn
	except:
		print(e)
	return none

def getCustomers(conn):
	cur = conn.cursor()
	cur.execute("SELECT ID, CompanyName FROM Customer")
	table = cur.fetchall()

	print("ID", "\t", "Customer Name")
	for row in table:
		print(str(row[0]), "\t", str(row[1]))

def getEmployees(conn):
	cur = conn.cursor()
	cur.execute("SELECT ID, FirstName, LastName FROM Employee")
	table = cur.fetchall()
	print("ID", "\t", "Employee Name")
	for row in table:
		print(str(row[0]) + "\t" + str(row[1]) + " " + str(row[2]))

def getOrdersByCID(conn, CID):
	cur = conn.cursor()
	cur.execute("SELECT OrderDate FROM \"Order\" WHERE CustomerId=?", (CID,))
	table = cur.fetchall()
	print("OrderDate")
	for row in table:
		print(str(row[0]))

def getOrderByEmpLN(conn, EmpLN):
	cur = conn.cursor()
	cur.execute('''SELECT OrderDate FROM "Order", "Employee" WHERE "Order".EmployeeId="Employee".Id AND "Employee".LastName="''' + str(EmpLN) + "\"")
	table = cur.fetchall()
	print("OrderDate")
	for row in table:
		print(str(row[0]))

def main():
	database = "./Northwind_small.sqlite"
	#Establishing a Database connection
	conn = createConnection(database)
	if(len(sys.argv)>1):
		with conn:
			if(sys.argv[1] == "customers"):
				getCustomers(conn)

			elif(sys.argv[1]=="employees"):
				getEmployees(conn)

			elif(sys.argv[1] =="orders"):
				if(sys.argv[2][0] == "c" or sys.argv[2][0] == "C"):
					getOrdersByCID(conn, sys.argv[2][5:])
				elif(sys.argv[2][0] == "e" or sys.argv[2][0] == "E"):
					getOrderByEmpLN(conn, sys.argv[2][4:])
				else:
					print("Please enter a valid argument")
	else:
		print("No valid argument found, please try again")

main()
