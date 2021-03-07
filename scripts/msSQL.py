import mysql.connector
import MySQLdb
import json
import pyodbc 
import pandas as pd 

a_c = [{ "h": "host1.com" , "u" : "user",   "p":"***" , "n": "host1"},
       { "h": "host2.com" , "u" : "user",   "p":"***" , "n": "host2"} ]
db = 'DB'
l_sqli = 1
def QU_EX(query, sys = 0 ):
    l_rmph = a_c[sys]["h"] 
    l_rmpu = a_c[sys]["u"]
    l_rmpp = a_c[sys]["p"]
    l_rmpn = a_c[sys]["n"]
    l_sqldb = "DB"
    # cnxn = pyodbc.connect("Driver={SQL Server};Server=serverName;UID=UserName;PWD=Password;Database=RCO_DW;")
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=" + l_rmph + ";"
                      "UID=" + l_rmpu + ";"
                      "PWD=" + l_rmpp + ";"
                      "Database=" + db + ";"
                      "Trusted_Connection=no;")
    print(query)
    cursor = cnxn.cursor()
    cursor.execute(query)
    arow = []
    for row in cursor:
        arow.append(row)
        #print('row = %r' % (row,))
    print( len(arow) ) 
    return arow

def DL_MinMax ( sch, tab, fkey, sys = 0 ):
    q_ex = "SELECT MIN( " + fkey + " ), MAX( " + fkey + " ) "
    q_ex = q_ex +  " FROM " + sch + "." + tab   
    a_rows = QU_EX( q_ex, sys )
    return a_rows    

a_mm = DL_MinMax("schema", "T_table", "T_ID" , 1  )
print("min = {:5} / max = {:,} ".format(a_mm[0][0], a_mm[0][1] ) )