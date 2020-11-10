# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:28:04 2020

@author: taisb
"""
#import os
#old_dir = os.getcwd()
#os.chdir("C:/Users/taisb/Documents/Python Scripts/Poker")

from objects import Deck, Player, Computer, Table, Chips, Pot
from functions import take_bet, computer_bet, check_rank, computer_wins, player_wins

game_on = True


   
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
            player.show()
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
                computer_wins(computer_cards, computer_rank, player_bets, player_chips)
            elif computer_score < player_score:
                player_wins(player_cards, player_rank, player_chips, pot, player_bets)
            
            # finish this round
            break 
            
    else:
        print(f"You finished with {player_chips.total} chips")
        print("Come again!")
        break
    
    
#os.chdir(old_dir)
