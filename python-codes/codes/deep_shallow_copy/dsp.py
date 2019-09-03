import copy

# sample
li1 = [1, 2, [3, 5], 4]
li2 = copy.deepcopy(li1)

li2[2][0] = 7
print(li2)
print(li1)

# shallow copy
li1 = [1, 2, [3, 5], 4]
print(li2)
li2 = copy.copy(li1)

li2[2][0] = 7
print(li2)
print(li1)