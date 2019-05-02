#!/usr/bin/python
#-*-coding: utf-8

import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('soap.db')
	cur = con.cursor()
	myStmt = "go"
	while myStmt != "quit":
		print(chr(27) + "[2J")
		sys.stderr.write("\x1b[2J\x1b[H")
		myStmt = input("Enter SQL statement: ")
		if myStmt != "quit":
			cur.execute(myStmt)
			data = cur.fetchall()
		print("The results are: ")
		for rec in data:
			for field in rec:
				print(field)
			print()
		print()
		myWait = input("Press enter  to continue: ")
		
	con.commit()
	con.close()
	
except lite.Error as e:
	print("Error%s:"%e.args[0])
	sys.exit(1)