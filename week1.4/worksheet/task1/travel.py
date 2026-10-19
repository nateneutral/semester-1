
def calculate_travel_distance(tank_capacity, km_per_litre): 
    '''  
    This function calculates the distance a vehicle can travel based on tank  
    capacity (ie how many litres of fuel in tank) and the number of  
    kilometres a vehicle can travel per litre, and returns the  
    distance, rounded to two decimal points. 
    ''' 

    f_capacity = float(tank_capacity) 
    f_kml = float(km_per_litre) 
    distance = round(f_capacity * f_kml, 2) 
    return distance 


#print(calculate_travel_distance(tank_capacity = 25, 2.0 ))
print(calculate_travel_distance(30.2, km_per_litre=3.3))
"""
a.
 
Will the program still run if an integer is passed to either tank_capacity or km_per_litre, eg
print(calculate_travel_distance(10, 3)) or print(calculate_travel_distance(20.5, 2))?
 
Explain.
Yes, as int can be implicitly converted to float
b.
 
Will the program still run with the following function calls? Please explain.

i.
 
print(calculate_travel_distance(tank_capacity=25, 2.0))
no, as the keyword argument must follow the positional argument
ii.
 
print(calculate_travel_distance(30.2, km_per_litre=3.3))
"""