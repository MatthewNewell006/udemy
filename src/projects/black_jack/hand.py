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

test_deck = Deck()
test_deck.shuffle()

# Player
test_player = Hand()

# Deal one card form the deck Card(suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(test_deck.deal())

test_player.value