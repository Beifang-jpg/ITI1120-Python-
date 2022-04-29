# Description of game:
# http://www.classicgamesandpuzzles.com/Old-Maid.html

# In this implementaion the computer is always the dealer

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the first character represents a rank and 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are rank and 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    l = len(deck)

    while (l>1):
        other.append(deck.pop())
        dealer.append(deck.pop())
        new = len(deck)
        l = new
    
    other.append(deck.pop()) # deal the last remaing card


    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    l.sort()
    s = l
    total_num = len(l)
    current_cardnum = 0
    # print(s)

    while(current_cardnum < total_num):

        if (current_cardnum == (total_num -1 )):
            no_pairs.append(s[current_cardnum])
            current_cardnum = current_cardnum + 1
            # print("last")

        else:
            card_first = s[current_cardnum]
            card_second = s[current_cardnum + 1]
            if(card_first[:-1] == card_second[:-1]):
                current_cardnum = current_cardnum + 2
                # print("pair")

            else:
                no_pairs.append(s[current_cardnum])
                current_cardnum = current_cardnum + 1
                # print("+1")

    random.shuffle(no_pairs)
    # print(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in deck:
        print(i, end=' ')
    print("")
    print("")

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
    Precondition: n>=1
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    # Assume usering will not put in things like "abc" or ""
    print("I have", n, "cards. If 1 stands for my first card and")
    print(n, "for my last card, which of my cards would you like?")

    valid = False
    position=int(input("Give me an integer between 1 and "+str(n)+": ").strip())
    if(position >= 1 and position <= n):
        valid = True

    while (valid == False):
        position = int(input("Invalid number. Please enter integer between 1 and "+str(n)+": ").strip())
        if(position >= 1 and position <= n):
            valid = True
        else:
            pass
    # print("position is" + str(position))
    return position



def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE


    Human_play = True 
    while (len(dealer)>0 and len(human))>0:
        if (Human_play == True):
            print("***********************************************************")
            print("Your turn.")
            print("")
            print("Your current deck of cards is:")
            print_deck(human)

            card_amount = len(dealer)

            card_position = get_valid_input(card_amount)




            card_picked = dealer[card_position-1]
            dealer.remove(card_picked)

            AAA = ["st", "nd", "rd", "th" ,"th", "th", "th","th", "th","th"]
            if (card_position > 9):
                BBB = 9
            else:
                BBB = card_position
                   
            print("You asked for my " + str(card_position) + AAA[BBB] + " card.")

            print("Here it is. It is" + str(card_picked))

            human.append(card_picked)
            print("")
            print("With " + str(card_picked) + " added, your current deck of cards is:")
            print_deck(human)

            print("And after discarding pairs and shuffling, your deck is:")
            new_human = remove_pairs(human)
            human = new_human
            print_deck(human)

            wait_for_player()
            Human_play = False
          
        else:
            print("***********************************************************")
            print("My turn.")
            print("")

            card_position = random.randint(0,len(human)-1)

            card_picked = human[card_position]
            human.remove(card_picked)
            dealer.append(card_picked)

            dealer = remove_pairs(dealer)

            AAA = ["st", "nd", "rd", "th" ,"th", "th", "th","th", "th","th"]
            if (card_position > 9):
                BBB = 9
            else:
                BBB = card_position
                   
            print("I took your " + str(card_position+1) + AAA[BBB] + " card.")

            wait_for_player()
            Human_play = True
               
          
    if (len(human)==0):
        print("***********************************************************")
        print("Ups. You do not have any more cards")
        print("Congratulations! You, Human, win")
    else:
        print("Ups. I do not have any more cards")
        print("You lost! I, Robot, win")

	 

# main
play_game()
