def percent_to_gpv(mark):
    '''(int) -> float
    return the grade point value, given a percantage mark.
    REQ: mark >= 0
    REQ: mark <= 100
    >>> percent_to_gpv(100)
    4.0
    >>> percent_to_gpv(0)
    0.0
    >>> percent_to_gpv(74)
    3.0
    '''
    
    #return the corresponding GPA if the mark is within the mark range.
    if mark >= 0 and mark <= 49:
        return 0.0
    elif mark > 49 and mark <=52:
        return 0.7
    elif mark > 52 and mark <=56:
        return 1.0
    elif mark > 56 and mark <=59:
        return 1.3    
    elif mark > 59 and mark <=62:
        return 1.7
    elif mark > 62 and mark <=66:
        return 2.0   
    elif mark > 66 and mark <=69:
        return 2.3    
    elif mark > 69 and mark <=72:
        return 2.7
    elif mark > 72 and mark <=76:
        return 3.0
    elif mark > 76 and mark <=79:
        return 3.3
    elif mark > 79 and mark <=84:
        return 3.7
    elif mark > 84 and mark <=100:
        return 4.0
    
def card_namer(value, suit):
    '''(str,str) -> str
    return the full name of a poker card given two character strings value and suit.
    >>> card_namer('T', 'C')
    '10 of Clubs'
    >>> card_namer('J', 'A')
    'CHEATER!'
    >>> card_namer('3', 'D')
    '3 of Diamonds'
    '''
    # assign the new names to the strings
    if value == 'A':
        value = 'Ace'
   
    elif value == 'T':
        value = '10'
    elif value == 'J':
        value = 'Jack'
    elif value == 'Q':
        value = 'Queen'
    elif value == 'K':
        value = 'King'
        
       
        
    if suit == 'D':
        suit = 'Diamonds'
    elif suit == 'C':
        suit = 'Clubs'
    elif suit == 'H':
        suit = 'Hearts'
    elif suit == 'S':
        suit = 'Spades'
         
    # check if the suit input is one of these four
    if suit in ['Diamonds', 'Clubs' , 'Hearts' , 'Spades']:
        return value+' '+'of'+' '+suit 
    #if not return 'CHEATER!'
    else:    
        return 'CHEATER!'
        
    
    

        
    
        
        


       
        
        
    
    

    
    
    
 
