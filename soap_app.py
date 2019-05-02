#!/usr/bin/python3
#-*-coding: utf-8

import sqlite3 as lite
import sys
import os

field_width = 15

def clear_screen():
    os.system('clear') if os.name == 'posix' else os.system('cls')


clear_screen()
print("""
        
             _____ ____  ___    ____ 
            / ___// __ \/   |  /  __\\
            \__ \/ / / / /| | / /_/ /
           ___/ / /_/ / ___ |/ ____/ 
          /____/\____/_/  |_/_/      

""")

input("          Press any key to continue")


con = None
try:
    con = lite.connect('soap.db')
    cur = con.cursor()
    myStmt = "go"
    while myStmt != "quit":
        clear_screen()
        myStmt = input("Enter SQL statement:\n")
        if myStmt != "quit":
            try:
                cur.execute(myStmt)
                data = cur.fetchall()
                print("\n\nResults:\n")
                for col in cur.description:
                    print(f'{col[0]:{field_width}.{field_width}}', end=' ')
                print()
                for _ in cur.description:
                    print('-' * (field_width - 1), end='  ')
                print()
                for rec in data:
                    for field in rec:
                        print(f'{str(field):{field_width}.{field_width}}', end=' ')
                    print()
                print()
            except Exception as e:
                print('\nError: ',e)
                print('\nUse "quit" to exit.')
            input("\nPress any key to continue")
            
    con.commit()
    con.close()
        
except lite.Error as e:
    print("Error%s:"%e.args[0])
    sys.exit(1)