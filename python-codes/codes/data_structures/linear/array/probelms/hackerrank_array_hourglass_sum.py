# https://www.hackerrank.com/challenges/2d-array/problem

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    unknown_maxima = None
    out_ptr = 0    
    iter_out = len(arr)-2

    while out_ptr < iter_out:
        in_ptr = 0
        itr_in = len(arr[out_ptr])-2
        while in_ptr < itr_in:
            known_maxima = arr[out_ptr][in_ptr]+arr[out_ptr][in_ptr+1]+arr[out_ptr][in_ptr+2]+arr[out_ptr+1][in_ptr+1]+arr[out_ptr+2][in_ptr]+arr[out_ptr+2][in_ptr+1]+arr[out_ptr+2][in_ptr+2]                        
            if unknown_maxima == None:                
                unknown_maxima = known_maxima
            elif unknown_maxima < known_maxima:
                unknown_maxima = known_maxima              
            in_ptr = in_ptr+1                    
        out_ptr = out_ptr+1
    return unknown_maxima
        

if __name__ == '__main__':    

    arr = [
            [1,1,1,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,0,2,4,4,0],
            [0,0,0,2,0,0],
            [0,0,1,2,4,0],
            ]
    arr2 = [
        [-1,-1,0,-9,-2,-2],
        [-2,-1,-6,-8,-2,-5],
        [-1,-1,-1,-2,-3,-4],
        [-1,-9,-2,-4,-4,-5],
        [-7,-3,-3,-2,-9,-9],
        ]
    arr3 = [
        [-1,1,-1,0,0,0],
        [0,-1,0,0,0,0],
        [-1,-1,-1,0,0,0],
        [0,-9,2,-4,-4,0],
        [-7,0,0,-2,0,0],
    ]
    result = hourglassSum(arr3)
    print(result)
