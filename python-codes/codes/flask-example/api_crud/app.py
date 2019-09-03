from flask import Flask,request,render_template
import sqlite3
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route('/')
@app.route('/create/<value>')
def create(value):
    print(value.split('+'))
    temp = value.split('+')
    con = sqlite3.connect('database/student')
    cur = con.cursor()
    cur.execute("INSERT INTO STUDENT_DETAILS VALUES('%s',%d,'%s')" % (temp[0],int(temp[1]),temp[2]))
    con.commit()

    sql = "SELECT * FROM STUDENT_DETAILS"
    cur.execute(sql)
    rows = cur.fetchall()
    data = []
    for row in rows:
        temp = OrderedDict()
        temp["id"] = str(row[0])
        temp["Name"] = row[1]
        temp['dept'] = row[2]
        data.append(temp)
    return json.dumps(data)

@app.route('/delete/<value>')
def delete(value):
    print(value)
    con = sqlite3.connect('database/student')
    cur = con.cursor()
    sql = "DELETE FROM STUDENT_DETAILS WHERE ID = %d" % (int(value))
    print(sql)
    cur.execute(sql)
    con.commit()

    sql = "SELECT * FROM STUDENT_DETAILS"
    cur.execute(sql)
    rows = cur.fetchall()
    data = []
    for row in rows:
        temp = OrderedDict()
        temp["id"] = str(row[0])
        temp["Name"] = row[1]
        temp['dept'] = row[2]
        data.append(temp)
    return json.dumps(data)

@app.route('/update/<value>')
def update(value):
    print(value.split('+'))
    temp = value.split('+')

    con = sqlite3.connect('database/student')
    cur = con.cursor()
    sql = "UPDATE STUDENT_DETAILS SET NAME ='%s',ID=%d,DEPT='%s' WHERE ID = %d" % (temp[0], int(temp[1]), temp[2], int(temp[3]))
    cur.execute(sql)
    con.commit()

    sql = "SELECT * FROM STUDENT_DETAILS"
    cur.execute(sql)
    rows = cur.fetchall()
    data = []
    for row in rows:
        temp = OrderedDict()
        temp["id"] = str(row[0])
        temp["Name"] = row[1]
        temp['dept'] = row[2]
        data.append(temp)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)