import pdb 
def find_minimum_value_maximum_value(list_data):
    minimum_value = None
    maximum_value = None
    
    pointer_2 = len(list_data)-1
    pointer_1 = 0    
    
    while pointer_2 > pointer_1:        
        if minimum_value == None and maximum_value == None:
            if list_data[pointer_1] > list_data[pointer_2]:
                maximum_value = list_data[pointer_1]
                minimum_value = list_data[pointer_2]
            else:
                minimum_value = list_data[pointer_1]
                maximum_value = list_data[pointer_2]
        else:
            if maximum_value < list_data[pointer_1]: maximum_value = list_data[pointer_1]
            if maximum_value < list_data[pointer_2]: maximum_value = list_data[pointer_2]

            if minimum_value > list_data[pointer_2]: minimum_value = list_data[pointer_2]
            if minimum_value > list_data[pointer_1]: minimum_value = list_data[pointer_1]

        pointer_1 = pointer_1+1
    return minimum_value,maximum_value


if __name__ == "__main__":
    minimum_value,maximum_value = find_minimum_value_maximum_value([603, 419, 140, 518, 599, 773, 720, 576, 848, 155])
    print(f"minimum_value: {minimum_value} | maximum_value: {maximum_value}")