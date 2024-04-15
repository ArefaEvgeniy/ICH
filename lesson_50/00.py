import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit'}

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()
