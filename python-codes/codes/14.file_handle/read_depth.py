f = open('sample.txt' ,'r')

# whole = f.read()
#
# print(whole)

print("---------------------------------")
only_oneline = f.readline()

print(only_oneline)
print("---------------------------------")
specified_lines = f.readlines()

print(specified_lines)