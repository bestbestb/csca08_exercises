def copy_me(listA):
    ''' (list) -> list
    returns a copy of the list with the following
    changes:
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word "List"

    >>> copy_me(['a', 2, 2.5, True, [2,3]])
    ['A', 3, 3.5, False, 'List']

    >>> copy_me([1,1,1])
    [2, 2, 2]
    '''
    # make an empty list
    listB = []
    # start loop
    for element in listA:
        # if element is a string
        if type(element) == str:
            # new element is the upper case of the string
            new_element = element.upper()
            # appened the string to the new list
            listB.append(new_element)
        # if the element is an integer or float
        elif (type(element) == int) or (type(element) == float):
            # add 1
            new_element = element + 1
            listB.append(new_element)
        # if the element is a boolean
        elif type(element) == bool:
            # not(True) == False, not(False) == True
            new_element = not(element)
            listB.append(new_element)
        # if the element is a list
        elif type(element) == list:
            # assign "List" to the new element.
            new_element = "List"
            listB.append(new_element)
    return listB


def mutate_me(listA):
    ''' list -> nonetype
    takes as input a list, returns None, and changes the input list in the
    following ways:
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word "List"

    >>> listA = ['a', 2, 2.5, True, [2,3]]
    >>> mutate_me(listA)
    >>> listA
    ['A', 3, 3.5, False, 'List']

    >>> listA = [1, 2, 2.5, 3, [2,3]]
    >>> mutate_me(listA)
    >>> listA
    [2, 3, 3.5, 4, 'List']
    '''
    # get the range of the index
    index_range = range(len(listA))
    # start the loop for each index
    for element_index in index_range:
        # original elements of the list
        element = listA[element_index]
        # if the element is a string
        if type(element) == str:
            # uppercase it and return the new element to its index
            listA[element_index] = element.upper()

        # if the element is an integer or float
        elif (type(element) == int) or (type(element) == float):
            # plus 1 and return the new element to its index
            listA[element_index] = element + 1

        # if the element is a boolean
        elif type(element) == bool:
            #  not(True) == False, not(False) == True;
            # return the new element to its index
            listA[element_index] = not(element)
        # if the element is a list
        if type(element) == list:
            # return "List" to its index
            listA[element_index] = "List"
