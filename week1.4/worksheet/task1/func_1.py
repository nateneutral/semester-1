
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function:
    This Function calculates the average of a list on integers.
    It returns the average.

    args:
        list of integers
    returns:
        integer, the average of the list of integers
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 

"""
a)
 
Examine the code and write a
 
dosctring for that function.

b)
 
What would be a meaningful name for func_1?
listAvg()
"""