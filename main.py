def move_zero(array):
    for i in array:
        if 0 in array:
            array.remove(0)
            array.append(0)
    return array

print(move_zero([1,2,0,3,4,0,5,6,0,7,8,0,9]))