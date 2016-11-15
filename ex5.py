def function_names(my_file):
    ''' (io.TextIOWrapper) -> list of str
    takes as a parameter a file open for reading, and returns a list
of all of the function names in that file.
    '''
    # make an empty list
    result = []
    # start the loop
    for line in my_file:
        # if the line starts with "def"
        if line.startswith('def '):
            # find the index of "("
            b = line.find('(')
            # make the new list
            result.append(line[4:b])
    return result


def justified(my_file):
    ''' (io.TextIOWrapper) -> bool
    takes as a parameter a file open for reading, and returns a boolean
    which is true if and only if every line in that ﬁle is left-justiﬁed.
    '''
    # start the loop
    for line in my_file:
        # if the line starts with a space
        if line.startswith(' '):
            return False
    return True

if (__name__ == '__main__'):
    # make sure the file you open and ex5.py are in the same directory
    my_file = open("ex4.py", "r")
    print(justified(my_file))
    my_file.close()
