# lambda function
# regular expression
# maps

# normal funtiion
def multi(mul): # replace this with lambda
    return mul*5
print(multi(2))


multi = lambda a:a*5 # lambda function
print(multi(2))

# example for lambda funtion as filter
mylist = [1,2,3,4,5,6,7,8,9,0]
list2 = list(filter(lambda x:(x%2 == 0),mylist))
print(list2)