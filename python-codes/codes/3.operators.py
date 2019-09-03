'''
Arithmetic operators:

+
Addition -Adds values on either side of the operator

-
Subtraction -Subtracts right hand operand from left hand operand


*
Multiplication -Multiplies values on either side of the operator


/
Division -Divides left hand operand by right hand operand


%
Modulus -Divides left hand operand by right hand operand and returns remainder


**
Exponent -Performs exponential (power) calculation on operators


//
Floor Division
The division of operands where the result is the quotient in which the digits after the decimal point are removed.



Note: ++ and -- not supported
'''

print(12+34)

print(23-1)

print(34*2)

print(45/5)

print(45%5)

print(45//5)

print(2**3)

'''
Bitwise operators:

x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

That is, they operate on numbers (normally), but instead of treating that number as if it were a single value, they treat it as if it were a string of bits, written in twos-complement binary

0 is written as "0"
1 is written as "1"
2 is written as "10"
3 is "11"
4 is "100"
5 is "101"
.
.
1029 is "10000000101" == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1
'''
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print(c,"&")

c = a | b;        # 61 = 0011 1101
print(c)

c = a ^ b;        # 49 = 0011 0001
print(c)

c = ~a;           # -61 = 1100 0011
print(c)

c = a << 2;       # 240 = 1111 0000
print(c)

c = a >> 2;       # 15 = 0000 1111
print(c)