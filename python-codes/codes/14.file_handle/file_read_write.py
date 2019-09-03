f = open('sample.txt' , 'r')

d = f.read()
print(d)
f.close()


# rb to read image pdf video anything like that
i = open('facebook.png','rb')

id = i.read()

print(id)

i.close()


# write a file

wf = open('write_text.txt','w')
wf.write(d)
wf.close()

wi  = open('write_image.png','wb')
wi.write(id)

wi.close()