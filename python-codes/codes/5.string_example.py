# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


str = 'coding is in my blood haha!'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


# concatinate
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# iterate on letters
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


print('a' in 'program')

# string format

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# old method

x = 12.3456789
print('The value of x is %3.2f' %x)

# string functions

print("JaCkson".lower())

print("JaCkson".upper())

print("This will split all words into a list".split())
# ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
#'This will join all words into a string'
print('Happy New Year'.find('ew'))
#7
print('Happy New Year'.replace('Happy','Brilliant'))
#'Brilliant New Year'