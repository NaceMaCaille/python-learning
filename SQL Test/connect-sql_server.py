import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-QRG8AL4'
DATABASE_NAME = 'turtle'

сonnection_string = f"""

        DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
"""

conn = pyodbc.connect(сonnection_string)
print(conn)

cursor = conn.cursor()
cursor.execute("select * from Orders where OrderId = 3")
row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()