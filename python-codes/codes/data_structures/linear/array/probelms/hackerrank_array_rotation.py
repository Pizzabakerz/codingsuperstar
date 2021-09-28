# https://www.hackerrank.com/challenges/array-left-rotation/problem

# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

# The Reversal Algorithm:
# Algorithm : 
 

# rotate(arr[], d, n)
#   reverse(arr[], 1, d) ;
#   reverse(arr[], d + 1, n);
#   reverse(arr[], 1, n);
# Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is : 
 

# Reverse A to get ArB, where Ar is reverse of A.
# Reverse B to get ArBr, where Br is reverse of B.
# Reverse all to get (ArBr) r = BA.
# Example : 
# Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7 
# A = [1, 2] and B = [3, 4, 5, 6, 7] 
 

# Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]

# Right reversal
# rotate(arr[], d, n)
# reverseArray(arr[], 1, n) ;
# reverse(arr[], 0, d-1);
# reverse(arr[], d, n-1);


def reverse_array(array,start,end):      
    import pdb 
    # pdb.set_trace()  
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start = start+1
        end = end-1
    return array

def rotate_array(array,total_rotation):
    length = len(array)-1    
    total_rotation = total_rotation - 1
    Ar = reverse_array(array,0,total_rotation)        
    Br = reverse_array(Ar,total_rotation+1,length)
    Ar_Br = reverse_array(Br,0,length)    
    return Ar_Br


if __name__ == "__main__":
    rotated = rotate_array([1,2,3,4,5],4)    
    print(rotated)