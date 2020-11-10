# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:28:04 2020

@author: taisb
"""
import random
from collections import Counter
game_on = True

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",\
         "King", "Ace"]
values= {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, \
         "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

######## OBJECTS

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
        

class Deck:
    def __init__(self):
        self.full_deck = []
        for suit in suits:
            for rank in ranks:
                self.full_deck.append(Card(suit, rank))
        
    def shuffle(self):
        random.shuffle(self.full_deck)
        
    def deal(self):
        return self.full_deck.pop()
    
    
class Player:
     def __init__(self):
         self.hand = []
         
     def add_card(self, card):
         self.hand.append(card)
         
     def show(self):
        print("YOUR HAND:\n")
        for card in self.hand:
            print(card, "\n")
       
            
class Computer:
     def __init__(self):
         self.hand = []
         
     def add_card(self, card):
         self.hand.append(card)
         
     def show(self):
        print("COMPUTER'S HAND':\n")
        for card in self.hand:
            print(card, "\n")
    
    
class Table:
    def __init__(self):
        self.table = []
        
    def add_card(self, card):
        self.table.append(card)
    
    def show_three(self):
        print("TABLE'S CARDS':\n")
        for i in range(0, 3):
            print(self.table[i], "\n")
        print("---")
        print("---")
        
    def show_one(self):
        print("TABLE'S CARDS:\n")
        for i in range(0, 4):
            print(self.table[i], "\n")
        print("---")
    
    def show_two(self):
        print("TABLE'S CARDS:\n")
        for card in self.table:
            print(card, "\n")
        
        
class Chips:
    def __init__(self):
        self.initial = int(input("With how many chips would you like to start? "))
        self.total = self.initial
        
    def win_bet(self, pot):
        self.total += pot
        
    def lose_bet(self, bet):
        self.total -= bet
        
        
class Pot:
    def __init__(self):
        self.total = 0
        
    def add_pot(self, bet):
        self.total += bet
        

####### FUNCTIONS

#def bet_or_fold(chips):
#    while True:
#        try:
#            answer = input("Would you like to bet or fold? B/F ").upper()
#           if answer == "B":
#                take_bet(chips)
#                break
#            elif answer == "F":
#                return "over"
#            else:
#                print("Please enter B or F.")
#        except:
#            print("Please enter B or F.")


def take_bet(chips):
    while True:
        try:
            bet = int(input("How many chips would you like to bet on this round? "))
        except ValueError:
            print("Please enter the number of chips you would like to bet on this round." )
        else:
            if chips.total < bet:
                print("Sorry, you don't have that many chips.")
            else:
                break
    return bet  


def computer_bet(computer_chips, pot):
    prob = [0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.08, 0.06, 0.04, 0.02]
    bet_values = range(0, 50, 5)
    bet = random.choices(bet_values, prob)
    pot.add_pot(bet)
    print("\n")
    print(f"The computer has bet {bet} chips")
    print(f"The pot now is worth {pot.total} chips")
    print("\n")

    
def royal_flush(cards, values = values):
    player_cards = []
    straight_values = straight_flush(cards)
    if straight_values != False:
        straight_values = straight_values[-1]
    else:
       return False
    if straight_values == "10, 11, 12, 13, 14":
        player_cards.append(values[cards[0].rank])
        player_cards.append(values[cards[1].rank])           
        return max(player_cards)*100000, "Royal Straight Flush"
    else:
        return False
  
    
def straight_flush(cards, values=values):
    suits = []
    flush_cards = []
    player_cards = []
    for card in cards:
        suits.append(card.suit)
    counter = Counter(suits)
    for suit, count in counter.items():
        if count >= 5:
            flush_suit = suit
            break
        else:
            return False
    for card in cards:
        if card.suit == flush_suit:
            flush_cards.append(card)
    straight_fun = straight(flush_cards)
    if straight_fun != False:
        straight_fun_cards = straight_fun[-1]
        straight_fun_cards_values = straight_fun_cards.split(", ")
        for value in straight_fun_cards_values:
            if (values[cards[0].rank] == int(value)) and (cards[0].suit == flush_suit):
                player_cards.append(value)
            elif (values[cards[1].rank] == int(value)) and (cards[1].suit == flush_suit):
                player_cards.append(value)
        print(player_cards)
        if len(player_cards) != 0:
            return int(max(player_cards))*10000, "Straight Flush: ", straight_fun_cards
        else:
            return False
    else:
        return False
    
  
def four_of_a_kind(cards, values = values):
    ranks = []
    for card in cards:
        ranks.append(card.rank)
    counter = Counter(ranks)
    for rank, count in counter.items():
        if count == 4 and (rank == cards[0].rank or rank == cards[1].rank):
            return values[rank]*1000, "Four of a Kind: ", rank
        else:
            return False
    
    
def full_house(cards, values = values):
    ranks = []
    player_cards = []
    for card in cards:
        ranks.append(card.rank)
    counter = Counter(ranks)
    for rank1, count1 in counter.items():
        if count1 == 3 and rank1 == cards[0].rank:
            player_cards.append(values[cards[0].rank])
            rank_1 = cards[0].rank
        elif count1 == 3 and rank1 == cards[1].rank:
            player_cards.append(values[cards[1].rank])
            rank_1 = cards[1].rank
    for rank2, count2 in counter.items():
        if count2 == 2 and rank2 == cards[0].rank:
            player_cards.append(values[cards[0].rank])
            rank_2 = cards[0].rank
        elif count2 == 2 and rank2 == cards[1].rank:
            rank_2 = cards[1].rank
            player_cards.append(values[cards[1].rank])
    for key in counter:
        value = counter[key]
        if value == 3:
            rank_1 = key
        elif value == 2:
            rank_2 = key
    if len(player_cards) == 2:
        return max(player_cards)*100, "Full House: ", rank_1 + " and " + rank_2
    else:
        return False
    
    
def flush(cards, values = values):
    suits = []
    flush_value = []
    for card in cards:
        suits.append(card.suit)
    counter = Counter(suits)
    for suit, count in counter.items():
        if count >= 5 and (suit == cards[0].suit or suit == cards[1].suit):
            flush_value.append(values[cards[0].rank])
            flush_value.append(values[cards[1].rank])
            return max(flush_value)*10, "Flush: ", suit
        else:
            return False
    
    
def straight(cards, values = values):
    cards_values = []
    straight_cards = []
    straight_values = []
    for card in cards:
        value = values[card.rank]
        cards_values.append(value)
    cards_values.sort()
    cards_values = list(set(cards_values))
    if 14 in cards_values and 2 in cards_values and 3 in cards_values and 4 in cards_values and 5 in cards_values:
        straight_values = [values[cards[0].rank], values[cards[1].rank]]
        return max(straight_values), "Straight: ", "1, 2, 3, 4, 5"
    if len(cards_values) > 4:
        for c in range(0, len(cards_values)-4):
            if cards_values[c] + 1 == cards_values[c+1]:
                if cards_values[c+1] + 1 == cards_values[c+2]:
                    if cards_values[c+2] + 1 == cards_values[c+3]:
                        if cards_values[c+3] +1 == cards_values[c+4]:
                            straight_cards.append(cards_values[c])
                            straight_cards.append(cards_values[c+1])
                            straight_cards.append(cards_values[c+2])
                            straight_cards.append(cards_values[c+3])
                            straight_cards.append(cards_values[c+4])
                            if (values[cards[0].rank] or values[cards[1].rank]) in straight_cards:
                                straight_values = [values[cards[0].rank], values[cards[1].rank]]
                                return max(straight_values), "Straight: ", str(cards_values[c]) + ", " + \
                                 str(cards_values[c+1]) +  ", " + str(cards_values[c+2]) + \
                                     ", " + str(cards_values[c+3]) + ", " + str(cards_values[c+4])
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False
                    
   
def three_of_a_kind(cards, values = values):
    ranks = []
    for card in cards:
        ranks.append(card.rank)
    counter = Counter(ranks)
    for rank, count in counter.items():
        if count == 3 and (rank == cards[0].rank or rank == cards[1].rank):
            return values[rank]*0.1, "Three of a Kind: ", rank
        else:
            return False
    
    
def two_pairs(cards, values = values):
    ranks = []
    pairs = []
    for card in cards:
        ranks.append(card.rank)
    counter = Counter(ranks)
    for rank, count in counter.items():
        if count == 2 and (rank == cards[0].rank or rank == cards[1].rank):
            pairs.append(rank)
    if len(pairs) == 2:
        pairs_print = pairs[0] + " and " + pairs[1]
        pairs_value = [values[pairs[0]], values[pairs[1]]]
        return max(pairs_value)*0.01, "Two Pairs: ", pairs_print
    else:
        return False
    
    
def one_pair(cards, values = values):
    ranks = []
    pair = []
    pair_rank = ""
    for card in cards:
        ranks.append(card.rank)
    counter = Counter(ranks)
    for rank, count in counter.items():
        if count == 2 and (rank == cards[0].rank or rank == cards[1].rank):
            pair.append(values[rank])
            pair_rank = rank
    if len(pair) == 1:
        return pair[0]*0.001, "One Pair: ", pair_rank 
    else:
        return False
    
    
def high_card(cards, values = values):
    max_value = 0
    max_card = ""
    for card in cards[0:2]:
        value = values[card.rank]
        if value > max_value:
            max_value = value
            max_card = card
    return max_value*0.0001, "High Card: ", max_card.rank  
    

def check_rank(cards):
    if royal_flush(cards) != False:
        return royal_flush(cards)
    elif straight_flush(cards) != False:
        return straight_flush(cards)[:-1]
    elif four_of_a_kind(cards) != False:
        return four_of_a_kind(cards)[:-1]
    elif full_house(cards) != False:
        return full_house(cards)[:-1]
    elif flush(cards) != False:
        return flush(cards)[:-1]
    elif straight(cards) != False:
        return straight(cards)[:-1]
    elif three_of_a_kind(cards) != False:
        return three_of_a_kind(cards)[:-1]
    elif two_pairs(cards) != False:
        return two_pairs(cards)[:-1] 
    elif one_pair(cards) != False:
        return one_pair(cards)[:-1]
    elif high_card(cards) != False:
        return high_card(cards)[:-1]


def winning_cards(rank, cards):
    if rank[:-2] == "Royal Flush":
        return rank + royal_flush(cards)[-1]
    elif rank[:-2] == "Straight Flush":
        return rank + straight_flush(cards)[-1]
    elif rank[:-2] == "Four of a Kind":
        return rank + four_of_a_kind(cards)[-1]
    elif rank[:-2] == "Full House":
        return rank + full_house(cards)[-1]
    elif rank[:-2] == "Flush":
        return rank + flush(cards)[-1]
    elif rank[:-2] == "Straight":
        return rank + straight(cards)[-1]
    elif rank[:-2] == "Three of a Kind":
        return rank + three_of_a_kind(cards)[-1]
    elif rank[:-2] == "Two Pairs":
        return rank + two_pairs(cards)[-1]
    elif rank[:-2] == "One Pair":
        return rank + one_pair(cards)[-1]
    elif rank[:-2] == "High Card":
        return rank + high_card(cards)[-1]
    
    
def computer_wins(computer_cards, player_bets, player_chips):
    print("Computer wins!")
    print(winning_cards(computer_rank, computer_cards))
    print(f"You lost a total of {player_bets} chips in this round")
    player_chips.lose_bet(player_bets)
    print(f"You currently have {player_chips.total} chips")
      

def player_wins(player_cards, player_chips, pot, player_bets):
    print("You win!")
    print(winning_cards(player_rank, player_cards))
    print(f"You won a total of {pot.total} chips in this round")
    winnings = pot.total - player_bets
    player_chips.win_bet(winnings)
    print(f"You currently have {player_chips.total} chips")
    
    
######## GAME LOGIC     

print("LET'S PLAY POKER!")
player_chips = Chips() # create chips
computer_chips = player_chips

while game_on:
    playing = input("Would you like to play a round of poker? Y/N ").upper()
    if playing == "Y":
        while True: # start new round
            
            pot = Pot() # start the pot
            
            game_deck = Deck()  # create deck
            game_deck.shuffle()
            
            # deal player's, computer's and table's cards
            player = Player()
            player.add_card(game_deck.deal())
            player.add_card(game_deck.deal())
            player_bets = 0
            
            computer = Computer()
            computer.add_card(game_deck.deal())
            computer.add_card(game_deck.deal())
            
            table = Table()
            i = 0
            while i != 3:
                table.add_card(game_deck.deal())        
                i += 1
            game_deck.deal()
            table.add_card(game_deck.deal()) 
            game_deck.deal()
            table.add_card(game_deck.deal()) 
            
            # show player's hand
            player.show()
            
            # take first bet and add it to the pot
            first_bet = take_bet(player_chips)
            pot.add_pot(first_bet)
            player_bets += first_bet
            
            # take computer bet
            computer_bet(computer_chips.total, pot)
            
            # show first 3 table cards
            table.show_three()
            
            # take second bet
            answer = input("Would you like to bet, pass, fold or go all in? B/P/F/A ").upper()
            while answer not in ["B", "P", "F", "A"]:
                answer = input("Please enter B, P, F, A.").upper()
            if answer == "B":
                second_bet = take_bet(player_chips)
                pot.add_pot(second_bet)
                player_bets += second_bet
            elif answer == "P":
                pass
            elif answer == "F":
                player_chips.lose_bet(player_bets)
                break
            elif answer == "A":
                second_bet = player_chips.total
                pot.add_pot(second_bet)
                player_bets += second_bet
               
            # take computer bet 
            computer_bet(computer_chips.total, pot)
            
            # show another table card
            player.show()
            table.show_one()
            
            # take third bet
            answer = input("Would you like to bet, pass, fold or go all in? B/P/F/A ").upper()
            while answer not in ["B", "P", "F", "A"]:
                answer = input("Please enter B, P, F, A.").upper()
            if answer == "B":
                third_bet = take_bet(player_chips)
                pot.add_pot(third_bet)
                player_bets += third_bet
            elif answer == "P":
                pass
            elif answer == "F":
                player_chips.lose_bet(player_bets)
                break
            elif answer == "A":
                third_bet = player_chips.total
                pot.add_pot(third_bet)
                player_bets += third_bet
                
            # take computer bet
            computer_bet(computer_chips.total, pot)
            
            # show final table card
            player.show()
            table.show_two()
            
            # take last bet
            answer = input("Would you like to bet, pass, fold or go all in? B/P/F/A ").upper()
            while answer not in ["B", "P", "F", "A"]:
                answer = input("Please enter B, P, F, A.").upper()
            if answer == "B":
                final_bet = take_bet(player_chips)
                pot.add_pot(final_bet)
                player_bets += final_bet
            elif answer == "P":
                pass
            elif answer == "F":
                player_chips.lose_bet(player_bets)
                break
            elif answer == "A":
                final_bet = player_chips.total
                pot.add_pot(final_bet)
                player_bets += final_bet
                
            # take computer bet 
            computer_bet(computer_chips.total, pot)
       
            # merge cards
            player_cards = player.hand + table.table
            computer_cards = computer.hand + table.table
            
            #player score and rank
            player_score, player_rank = check_rank(player_cards)
            
            # computer score and rank
            computer_score, computer_rank = check_rank(computer_cards)
            
            # see who wins
            if computer_score > player_score:
                computer_wins(computer_cards, player_bets, player_chips)
            elif computer_score < player_score:
                player_wins(player_cards, player_chips, pot, player_bets)
            
            # finish this round
            break 
            
    else:
        print(f"You finished with {player_chips.total} chips")
        print("Come again!")
        break
