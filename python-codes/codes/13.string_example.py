# string operations
# file operat
# oop

# string
text = " this is my name i am jackson "

for t in text:
    print(t)

tu = text.upper()
print(tu)
print(tu.lower())

print(len(text))

print(max(text))

print(sorted(text))
print(sorted(text,reverse=True))

print(text.count('a'))

print('jack')
print('jack \'s car')

print("jack's")

print('''
multi
line
print
''')

print("""
    multi
    line
    print
""")

print("-----------")

text = " hi this is jackson"

print(text)

# indexing with string
print(text[1])
print(text[-1])

# slice
print(text[0:8])
print(text[-9:-1])

# for loop with string

for i in text:
    print(i)

tu = text.upper()
print(tu)
print(tu.lower())

print(len(text))

print(max(text))

print(sorted(text))
print(sorted(text,reverse=True))

print(text.count('a'))

print("----------------")
# methods in string
print(text)
print(text.strip())

# strip removes the key given if present in begining and end of string
# but not at the middle

text = "apple orange banana"

print(text.strip('a'))

print('---------')

li = [' basic','bonus ',' sample',' data ',' hexagon ']
li_t = [' basic','bonus ',' sample',' data ',' hexagon ']

# for loop to concat the both of the list

for i in range(len(li)):
    print(li[i].strip()+li_t[i].strip())

print('---------')
# split

text = "hi this is jackson"

print(text.split())
print('---------')

text = ['jack_dob','max_min','day_night']

print(text)
clean_one = []
clean_two = []

for i in range(len(text)):
    clean_one.append(text[i].split('_')[0])
    clean_two.append(text[i].split('_')[1])

print(clean_two)
print(clean_one)

print('---------')
# create username with email id

# email = input("enter your email: ")
#
# username = email.split("@")[0]
# company = email.split("@")[1].split('.')[0]
#
# corp = ['accenture','tcs','zest']
#
# if company in corp:
#     print("you are allowed to view the data")
#
# else:
#     print("plese make sure that your company is reg")


# replace

text = "hi my naaaime is jackson"
print(text)
print(text.replace('naaaime','name'))

print("----------")
text = input("enter the text")


mistake = ['except','edition','aloud']

corrections = ['accept','addition','allowed']

process = text.split()
# print(process)

for i in range(len(process)):
    if process[i] in mistake:
        mis_in = mistake.index(process[i])
        text = text.replace(mistake[mis_in],corrections[mis_in])
    else:
        pass

print("corrected word: ",text)
