import pyodbc

cnxn_str = ("Driver=FreeTDS;"
            "Server=computer,1433;"
            "Database=tempdb;"
            "UID=sa;"
            "PWD=test123;")
cnxn = pyodbc.connect(cnxn_str)

cur = cnxn.cursor()

'''txt = (
"CREATE TABLE SensorData ("
        "[node-id] TEXT NOT NULL,"
        "gps TEXT NOT NULL,"
        "protocol TEXT NOT NULL,"
        "date TEXT NOT NULL,"
        "[sensor-id] TEXT NOT NULL,"
        "value TEXT NOT NULL,"
        "magnitude TEXT NOT NULL,"
        "[gate-id] TEXT NOT NULL,"
        "[network-id] TEXT NOT NULL"
");"
)

print(txt)
cur.execute(txt)

cur.commit()'''

cur.execute("SELECT * FROM SensorData")
for row in cur:
    print(row)
    
cnxn.close()