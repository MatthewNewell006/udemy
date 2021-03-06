import random

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' )

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
         'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


playing = True


class Cards():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    
    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    
    def __init__(self):
        self.cards = []    # start with an empty list as we did in the Deck class
        self.value = 0     # start with zero value
        self.aces = 0      # add an attribute to handle the aces
    
    def add_card(self, card):
        # card passed in
        # from Deck.deal() ---> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        # track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        # If total.value > 21 and I still have an ace
        # Then change my ace to be a 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __inti__(self, total = 100):
        self.total = total    # This can be set to a default value or supplied by a user input
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry. Please provide an integer. ')
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    
    global playing    # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s. ')    # Hit # hh # stand
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealers Turn.")
            playing = False
        else:
            print("Sorry I didn't understand that. Please enter h or s only")
            continue
        break

def player_busts(player, dealer, chips):
    print("Bust Player!")
    chips.lose_bet()
    
def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("Player Wins! Dealer Busts!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()
    
def push(player, dealer):
    print("Player and Dealer tie. Push!")