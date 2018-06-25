# these should be the only imports you need
import sys
import sqlite3

def connection(database):
	try:
		connection = sqlite3.connect(database)
		return connection
	except:
		print(e)
	return none
def employeesdata(connection):
	cur = connection.cursor()
	cur.execute("SELECT ID, FirstName, LastName FROM Employee")
	table = cur.fetchall()
	print("ID", "\t", "Employee Name")
	for row in table:
		print(str(row[0]) + "\t" + str(row[1]) + " " + str(row[2]))
def customerdata(connection):
	cur = connection.cursor()
	cur.execute("SELECT ID, CompanyName FROM Customer")
	table = cur.fetchall()
	print("ID", "\t", "Customer Name")
	for row in table:
		print(str(row[0]), "\t", str(row[1]))
def orderEmpLN(connection, EmpLN):
	cur = connection.cursor()
	cur.execute('''SELECT OrderDate FROM "Order", "Employee" WHERE "Order".EmployeeId="Employee".Id AND "Employee".LastName="''' + str(EmpLN) + "\"")
	table = cur.fetchall()
	print("OrderDate")
	for row in table:
		print(str(row[0]))
def CIDdata(connection, CID):
	cur = connection.cursor()
	cur.execute("SELECT OrderDate FROM \"Order\" WHERE CustomerId=?", (CID,))
	table = cur.fetchall()
	print("OrderDate")
	for row in table:
		print(str(row[0]))
def main():
	database = "./Northwind_small.sqlite"
	#Establishing a Database connection
	conn = connection(database)
	if(len(sys.argv)>1):
		with conn:
			if(sys.argv[1] == "customers"):
				customerdata(conn)
			elif(sys.argv[1]=="employees"):
				employeesdata(conn)
			elif(sys.argv[1] =="orders"):
				if(sys.argv[2][0] == "c" or sys.argv[2][0] == "C"):
					CIDdata(conn, sys.argv[2][5:])
				elif(sys.argv[2][0] == "e" or sys.argv[2][0] == "E"):
					orderEmpLN(conn, sys.argv[2][4:])
				else:
					print("Please enter a valid argument")
	else:
		print("Error")
main()
