"""
    In a module called week5_exercises.py, write a function concat_dico(dico1, dico2) that takes 
    two dictionaries as parameters and returns a single dictionary containing the pairs from both dictionaries. 
    An important requirement is that both dictionaries are NOT modified by the function.

"""

"""def concat_dico(dico1, dico2):
    mergedDic = dico1 | dico2  #создает новый словарь и объеденяет два предыдущих
    print(mergedDic)


concat_dico({'one':1, 'two':2, 'three':3}, {'four':4, 'five':5})"""



"""def concat_dico(dico1, dico2):
    result = {}
    for x, y in dico1.items():
        result[x] = y
    for x, y in dico2.items():
        result[x] = y
    print(result)
concat_dico({'one':1, 'two':2, 'three':3}, {'four':4, 'five':5})"""


"""
An issue may arise when both dictionaries share a least one common key. 
Rewrite the function so that the method stores the values in a list if dico1 
and dico2 share a common key
"""



def concat_dico(dico1, dico2):
    mergedDic = dict()
    for key, value in dico1.items():
        mergedDic[key] = value 
    for key, value in dico2.items():
        if key in mergedDic:
            mergedDic[key] = [dico1[key], dico2[key]]
        else: 
            mergedDic[key] = value
    print(mergedDic)


concat_dico({'one':1, 'two':2, 'five':5}, {'two':10, 'five':5})