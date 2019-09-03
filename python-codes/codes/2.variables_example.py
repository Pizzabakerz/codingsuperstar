# variables

# SYNTAX : variablename = declare

a = 10
a = 10.0
a = "ten"
a = True
a = -1e+3j

# check type
print(a)
print(type(a))

# some special case
a,b = 10,20
print(a)
print(b)


'''
int	        long	                float	        complex
10	        51924361L	            0.0	            3.14j
100	        -0x19323L	            15.20	        45.j
-786	    0122L	                -21.9	        9.322e-36j
080	        0xDEFABCECBDAECBFBAEl	32.3+e18	    .876j
-0490	    535633629843L	        -90.	        -.6545+0J
-0x260	    -052318172735L	        -32.54e100	    3e+26J
0x69	    -4721885298529L	        70.2-E12	    4.53e-7j

'''