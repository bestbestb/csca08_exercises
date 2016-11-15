def transpose(strlist):
    
    ''' (list of str) -> list of str
    Return a list of m strings, where m is the length of a longest string
    in strlist, if strlist is not empty, and the i-th string returned
    consists of the i-th symbol from each string in strlist, but only from
    strings that have an i-th symbol, in the order corresponding to the
    order of the strings in strlist.
    Return [] if strlist contains no nonempty strings.
    >>> transpose([])
    >>> []
    >>> transpose([''])
    >>> []
    >>> transpose(['transpose', '', 'list', 'of', 'strings'])
    >>> ['tlos', 'rift', 'asr', 'nti', 'sn', 'pg', 'os', 's', 'e']
    '''


     # create an empty list to use as a result
    result = []
    useless = []
     
    # loop through every element in the input list
    for element in strlist:
        ch_result = ' '
    # loop through each character in the string
        for character in element:
            # 2 cases to deal with here:
          # case 1: the result list has a string at the correct index,
        
            if character != " ":
                ch_result = character + ch_result
                
           
                
               
            # just add this character to the end of that string         
     
        # case 2: the result list doesn't have enough elements,
            if character == " ":
                
                useless.append(character)
        result.append(character)
               
# need to create a new element to store this character
    return result