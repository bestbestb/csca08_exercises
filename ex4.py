def insert(listA, listB, index):
    '''(str or list, str or list, int) -> str or list
    return a copy of listA with listB inserted into it, given listA, listB, and
    in index.
     >>> insert([1, 2, 3], [4, 5, 6], 3)
     [1, 2, 4, 5, 6, 3]
     >>> insert(["a", "2", "b"], [4, 5, 6], 3)
     ['a', '2', 4, 5, 6, 'b']
     >>> insert(["a", "2", "b"], [1, 2, 3], 3)
     ['a', '2', 1, 2, 3, 'b']
     >>> insert(["a", "2", "b"], ["a, "b", "c"], 3)
     ['a', '2', 'a', 2, 3, 'b']
     >>> insert(["a", "z", "b"], [5, "b", "c"], 2)
     ['a', 'z', 5, 'b', 'c', 'b']
    '''
    # take the front part and bottom part of listA and merge with listB
    result = listA[:index] + listB + listA[index:]
    return result


def up_to_first(listA, objectB):
    '''(list or str, str) -> list or str
    returns  a copy of the list up to (but not including) the first occurrence
    of that object, or all of the elements if that object is not in the list.
    >>> up_to_first([1,2,3,5,7], 2)
    [1]
    >>> up_to_first([1,2,3,5,7,9], 3)
    [1, 2]
    >>> up_to_first([1,3,3,5,9,9,11], 3)
    [1]
    >>> up_to_first("d", "a")
    'd'
    '''
    # consider when the object is in listA
    if objectB in listA:
        # take the index of the object
        indexB = listA.index(objectB)
        result = listA[:indexB]
        return result
    else:
        result = listA
    return result


def cut_list(listA, index):
    '''
    (list or str, int) -> list or str
    given a list and an index, returns a copy of the list, but with the
    items before and after the index swapped.
    >>> cut_list([1,2,3,5,7], 2)
    [3, 5, 7, 1, 2]
    >>> cut_list(["a","b",3,5,7], 2)
    [3, 5, 7, 'a', 'b']
    >>> cut_list(["a","b",3,"c",7], 2)
    [3, 'c', 7, 'a', 'b']
    >>> cut_list(["a","b",3,"c",7], 4)
    [7, 'a', 'b', 3, 'c']
    '''
    # add the bottom part and front part together
    return listA[(index+1):] + listA[(index):(index+1)] + listA[:index]
