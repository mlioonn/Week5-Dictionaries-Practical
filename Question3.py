"""
In the module week5_exercises.py, write a function map_list(keys, values) that takes two list of the same length as parameters
and returns a dictionary where the keys are the elements from the list keys and the values are the elements from the list values. 
The mapping follows the lists indices. The function returns None if the two lists do not have the same length.    
"""

def map_list(keys, values):
    if len(keys) != len(values):
        return None
    else:
        return dict(zip(keys, values))
print(map_list(['un', 'two'], [1,2]))


"""
The Advanced bit:
An issue may arise if the list keys as duplicate elements as the keys must be unique. 
Rewrite the function so that the method returns None and print an error message if keys 
has duplicates. Note that having duplicate values in the values list is fine    
"""


def map_list(keys, values):
    if len(keys) != len(values):
        return None
    
    mapDict = {}
    for index in range(len(keys)):
        if keys[index] not in mapDict:
            mapDict[keys[index]] = values[index]
        else:
            return None
        
    return mapDict
            
print(map_list(['un', 'two'], [1,2]))
