import re


'''
METACHAR:

[] - set of ch to match
. match any single char except new line

\ treats meta chas ordinary char

| either or - seperator

^ match starting

$ end of string

{} match specific number or pattern

() match group of pattern

* matches zero or more patter from its left

+ matches one or more pattern from its left

'''

'''
SPECIAL SEQUENCES:
\A return if the pattern is start of string
\b return if the pattern is begining or end of the word
\B return if the pattern is not begining or not end of the word
\d return where the pattern contains digits
\D return string does not contains digits
\s return string with white space
\S return string without white space
\w return contain word
\W return does not contain word
\Z match end of the string
'''

'''
1.re.findall()
2.re.search()
3.re.split()
4.re.sub()
'''

text = 'asdfg12345asdfg12345ASDFG'

a = re.compile('\d')
print(a.findall(text))

date = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
test_str= """
     fsf2010/08/27sdfsdfsd
     dsf sfds f2010/08/26 fsdf 
     asdsds 2009-02-02 afdf
     """
print(date.findall(test_str))

date = re.compile(r'\d{2}[-/.]\d{2}[-/.]\d{4}')
test_str= """
     fsf20/08/2007sdfsdfsd
     dsf sfds f22/08/2006 fsdf 
     asdsds 09-02-1002 afdf
     asdsds 09.02.1002 afdf
     """
print(date.findall(test_str))

v = re.compile(r'my$')
print(v.findall("this is my this is my"))

v = re.compile(r'\Bh')
print(v.findall("this is my this is my"))

v = re.compile(r'\bh')
print(v.findall("hthis is my thish is my"))

v = re.compile(r'\Ah')
print(v.findall("hthis is my thish is my"))

v = re.compile(r'\whi')
print(v.findall("hthis is my thish is my"))

v = re.compile(r'\W0')
print(v.findall("hthis 0 is0 my thish is my"))

v = re.compile(r'my\Z')
print(v.findall("hthis 0 is0 my thish is my"))


# text from to
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

p = re.compile('[0-9]')
print(p.findall("Aye, 23said Mr. 345Gibenson 54Stark"))

# split
import re

# Splitting will occurs only once, at '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 2))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here jackfson', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))

# sub

print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced.
print(re.sub('ub', '~*', 'Subject has Uber booked already subject'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked subject already', count=1, flags=re.IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

print(re.sub(r'AND', ' & ', 'Baked Beans And Spandam', flags=re.IGNORECASE))

