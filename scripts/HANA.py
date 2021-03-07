import pyhdb
import pandas as pd
from hdbcli import dbapi

query = "SELECT TOP 1000 * FROM EHS.KG"

#connection = pyhdb.connect('localhost', 30015, 'username', 'password')
connection = pyhdb.connect('tenant.hana.ondemand.com', 30015, 'user', '**') #multiple containers"
cursor = connection.cursor()
#cursor.execute("SELECT top 20 DATE, HIGH FROM SAP_HANA_DEMO.NIFTY_50_DATA")
cursor.execute("SELECT TOP 1000 * FROM SCH.TB")
a = cursor.fetchall()
data = pd.DataFrame(a)
