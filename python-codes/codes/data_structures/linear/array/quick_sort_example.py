# given an unsorted array

# steps
# arrange the array in an order that 
#   1.anything to right of the array is greater to the pointer
#   2.anything to left is lesser to the pointer
# https://www.youtube.com/watch?v=MZaf_9IZCrc&t=197s

# https://www.youtube.com/watch?v=ZHVk2blR45Q
import pdb

def partition_for_quick_sort(array):
    # this pointer jumps
    pointer_1 = -1

    # this pointer moves
    pointer_2 = 0

    # this is the pivot which is always the last element in our case
    pivot_pointer_3 = len(array) - 1

    # the pivot pointer is always runs up to last element but not the last element
    
    while pointer_2 <= pivot_pointer_3-1:            
        if array[pointer_2] > array[pivot_pointer_3]:
            pointer_2 = pointer_2+1

        elif array[pointer_2] < array[pivot_pointer_3]:
            pointer_1 = pointer_1+1

            temp = array[pointer_2]
            array[pointer_2] = array[pointer_1]
            array[pointer_1] = temp            

            pointer_2 = pointer_2+1
        
        else:
            pointer_2 = pointer_2+1
    
    # array.insert(pointer_1+1,array[pivot_pointer_3])   
    # this is actually what to be done but since insertion takes another operation we can just swap

    temp = array[pointer_1]
    array[pointer_1] = array[pivot_pointer_3]
    array[pivot_pointer_3] = temp
    # now anything to right array[pivot_pointer_3] is greater to array[pivot_pointer_3]
    # and anything to right array[pivot_pointer_3] is lesser to array[pivot_pointer_3]

    return array
        
if __name__=='__main__':

    unsorted_array = [4,51,2,6,8,9,7]
    partioned_array = partition_for_quick_sort(unsorted_array)
    print(partioned_array)