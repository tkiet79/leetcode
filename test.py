
def minvalue(my_list):
    min_value = my_list[0]
    for i in range(1,len(my_list) - 1):
        if my_list[i] < min_value:
            min_value = my_list[i]
    return min_value

my_list = [3,5,6,7,6,4,4,5,5,7,8,4,3,23,457,345,2,5,-1,5,45,4,5,5,7,5,3,4,5,6,2,65,45,534532]
print(minvalue(my_list))