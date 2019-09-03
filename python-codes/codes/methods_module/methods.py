'''
METHODS ARE OF 4 TYPES

method with return with parameter
method with return without parameter
method without return with parameter
method without return without parameter
'''

# method with return with parameter
def add(a,b):
    c = a+b
    return c

# hold the value
res = add(1,2)
print(res)
print(add(1,2))

# direct print
print(res)

print('-----------------')

# method without return without parameter

def check():
    print("this function works")

# this function is not returning i can't hold or direct print the value
# also i cant give any argument

check()
# print(check()) # this give me none because it is a void(empty) function

print('-----------------')

#method with return without parameter
def pi():
    return 3.14

p = pi()
print(p)

print(pi())

#method without return with parameter

def mul(a,b):
    print(a*b)

mul(12,3)

print("---------------")
# formal and actual parameter

def area(r,pi=3.14):
    return pi*(r**2)

res = area(5)
print(res)




