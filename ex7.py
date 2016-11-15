def create_dict(my_file):
    ''' (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}

    takes one parameter, an open file handle (remember ex5, this is
    an open file handle, not the name of a file), and returns a dictionary that
    maps a string to a list of strings and ints.


    '''
    # make an empty dictationary for use
    result_dict = {}
    # for each line in the file
    for line in my_file:
        # remove space
        orig_list = line.split()
        # key is the first element
        key = orig_list[0]
        # elements after the key forms a list
        new_list = orig_list[1:]
        # name the first element
        list_0 = new_list[0]
        # map first element to second and second to first
        new_list[0] = new_list[1]
        new_list[1] = list_0
        # name the other elements
        list_2 = new_list[2]
        list_3 = new_list[3]
        list_4 = new_list[4]
        # switch place of the three elements
        new_list[2] = list_4
        new_list[3] = int(list_2)
        new_list[4] = list_3
        # map the new list back to the dictationary
        result_dict[key] = new_list

    return result_dict


def update_field(my_dict, user, field, value):

    ''' (dict of {str: [str, str, str, int, str]}) -> dict of \
    {str: [str, str, str, int, str]}
    takes 4 parameters: A dictionary in the format created by
    the previous function, a username, the name of a field), and a new value
    to replace the current value of the specified field.

    REQ: field must be One of: ¡¯LAST¡¯, ¡¯FIRST¡¯, ¡¯E-MAIL¡¯, ¡¯AGE¡¯ or ¡¯GENDER¡¯

    >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@christmas.np', \
450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 999, \
'M']}
    True

    >>> my_dict = {'bobr':['bob', 'ryan', 'bob@christmas.np', 210, 'M']}
    >>> update_field(my_dict, 'bobr', 'E-MAIL', 'bob@utoronto.ca')
    >>> my_dict == {'bobr': ['bob', 'ryan', 'bob@utoronto.ca', 210, 'M']}
    True

    '''
    # name the list of the given user
    list_user = my_dict[user]
    # map the correspnding value to the given fields
    if field == 'LAST':
        list_user[0] = value
    if field == 'FIRST':
        list_user[1] = value
    if field == 'E-MAIL':
        list_user[2] = value
    if field == 'AGE':
        list_user[3] = value
    if field == 'GENDER':
        list_user[4] = value
    # map the list back to the dictationary
    my_dict[user] = list_user


if (__name__ == '__main__'):
    # make sure the file you open and ex7.py are in the same directory
    my_file = open("ex7_data.txt", "r")
    print(create_dict(my_file))
    my_file.close()
