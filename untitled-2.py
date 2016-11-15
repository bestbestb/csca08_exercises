JOKER1 = 27
JOKER2 = 28
def move_joker_2(deck):
    ''' (list of int) -> NoneType
    The parameter represents a deck of cards.  This is step 2 of the algorithm.
    Find JOKER2 and move it two cards down. Treat the deck as circular.
    
    >>> deckA = [1, 2, JOKER2, 4, 5]
    >>> move_joker_2(deckA)
    >>> deckA
    [1, 2, 4, 5, JOKER2]
    
    >>> deckA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, JOKER1, JOKER2, 26]
    >>> move_joker_2(deckA)
    >>> deckA
    
    [1, JOKER2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, JOKER1, 26]
    
    
    >>> deckA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, JOKER1, 26, JOKER2]
    >>> move_joker_2(deckA)
    >>> deckA
    
    [1, 28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 26]
    
    '''
    
    
    deck_length = len(deck)
    bot_card_index = len(deck) - 1   
    
    # case 1, if joker2 is at bottom of the deck
    
    if deck[bot_card_index] == JOKER2:
        deck.remove(JOKER2)
        first_card = deck[0]
        deck[0] = JOKER2
        deck.reverse()
        deck.append(first_card)
        deck.reverse()
        
    elif deck[bot_card_index - 1] == JOKER2:
        deck.remove(JOKER2)
        deck.reverse()
        deck.append(JOKER2)
        deck.reverse()
        
    else:
        joker_index = deck.index(JOKER2)
        swapcards(deck, JOKER2)
        swapcards(deck, JOKER2)
        
        
        