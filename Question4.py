"""
In the module week5_exercises.py, implement reverse_dictionary(dico) a function that reverse the mapping between keys and values.
The parameter dico is a dictionary where the keys and values are all immutable. The function should return a dictionary 
where the pair key1:value1 in dico becomes the pair value1:key1.
The Advanced bit:
An issue may arise again if the dictionary dico has duplicate elements in its values. 
Rewrite the function so that the method returns None and prints an error message if that is the case.


"""

def reverse_dictionary(dico):
    reversedDic = dict()
    for key in dico:
        value = dico[key]
        if value not in reversedDic:
            reversedDic[value] = key
        else:
            return None
    return reversedDic
print(reverse_dictionary({'one':1, 'two':2}))