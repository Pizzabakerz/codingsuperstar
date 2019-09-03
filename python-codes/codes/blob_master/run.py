import pymysql

try :
    con = pymysql.connect('localhost','root','','sample')

    cur = con.cursor()

    cur.execute("select * from images")
    image = cur.fetchall()
    for i,j in image:
        file = open('destination/'+i+".jpg",'wb')
        file.write(j)

except Exception as e:
    print(e)


