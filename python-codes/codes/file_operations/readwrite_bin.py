# read and write image

f = open('files/python_pdfcover.jpg', 'rb')
data  = f.read()
f.close()

f = open('write/image.jpg','wb')
f.write(data)
f.close()

# read write pdf

f = open('files/pythonlearn.pdf', 'rb')
data = f.read()
f = open('write/documentpdf.pdf','wb')
f.write(data)
f.close()

# read write video
f = open('files/rabbit.mp4', 'rb')
data = f.read()
f.close()
f = open('write/video.mp4','wb')
f.write(data)