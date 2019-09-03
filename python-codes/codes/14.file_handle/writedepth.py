f = open("con.txt",'w')

f.write("""
    this is file reading method
""")

f.close()

# append
s = open("con_two.txt" , 'a')
s.write("""
    this is file reading method
""")

s.close()