'''
SYNTAX:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


print() Parameters
objects - object to the printed. * indicates that there may be more than one object
end - end is printed at last
flush - If True, the stream is forcibly flushed. Default value: False

'''

print("Python is fun.")

print("python is alwasys fun"*3)

print("flushing....",flush=True)

print('line one',end='\t')
print('line two')

# single quote

print('this is jack')
print('this is jack\'s car')

# double quote

print("this is jack")
print("this is jack;s car")

# multi line print
print('''
this
is
multi 
line
''')

print("""
this 
is
also
multi
line
""")

# print number

print(12)
print(12.0)
print(12+2j)

# print bool
print(True)
print(False)

# print multiple things
print("jack","son",12)
