# if you are writting a file it dont mean the file should exist

st = """

Java
A suite of computer software products and specifications from Sun Microsystems 
for developing apps that can run on many different types of computers.

     """


# write
f = open('/Users/jacksonjegatheesan/PycharmProjects/meena/file_operations/write/test.txt','w')

f.write(st)

f.close()


# append

f  = open('/Users/jacksonjegatheesan/PycharmProjects/meena/file_operations/write/test_two.txt','a')

f.write(st)

f.close()