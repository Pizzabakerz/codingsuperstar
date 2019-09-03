def square(val):
    return val*val

# use map to avoid this
square(1)
square(2)
square(3)
square(4)

mytuple = (1,2,3,4)
ans = map(square,mytuple) # map function
print(set(ans))