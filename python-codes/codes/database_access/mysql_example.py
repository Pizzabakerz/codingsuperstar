import sqlite3

conn = sqlite3.connect('sqlitedb/database.db')

cur = conn.cursor()


try:
    name = input()
    gender = input()
    phone = input()
    email = input()
    query = "INSERT INTO DETAILS VALUES ('{}','{}','{}','{}')".format(name,gender,phone,email)
    cur.execute(query)
    conn.commit()
    print("inserted sucessfully")

except Exception as e:
    print(e)

finally:
    conn.close()