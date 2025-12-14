# Black Jack Game -------------------------------------------------------------
import random

def play_blackjack(player_data):
    
    card_deck = []
    
    for face in ['A', 'K', 'Q', 'J']:
        for suite in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            
            pCard = face + " - " + suite
            card_deck.append(pCard)
    
    for i in range(2, 11):
        for suite in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            
            pCard = str(i) + " - " + suite
            card_deck.append(pCard)
    
    mini_game = True
    while mini_game is True:
        
        print("\nYou're now playing BlackJack!")
        
        print("\n--- BlackJack Menu ---")
        print("1.) Place a Bet")
        print("2.) Ask for Spot")
        print("3.) Sitout Hand")
        print("4.) Leave Table")
        
        try:
            game_sel = int(input("\nMake a Selection: "))
        
        except ValueError:
            game_sel = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
        
        if game_sel == 1:
            
            bet = 0
            
            bet_mode = True
            while bet_mode:
                
                if player_data['Financials']['Balance'] >= 1:
                    print("\nYour Credits: ", player_data['Financials']['Balance'])
                    print("Your Bet: ", bet)
                    
                    print("\n--- Betting Menu ---")
                    print("1.) Bet 1 Credit")
                    print("2.) Bet 5 Credits")
                    print("3.) Bet 10 Credits")
                    print("4.) Bet 25 Credits")
                    print("5.) Bet Custom Amount")
                    print("6.) Place Bet")
                    print("7.) Go Back")                
                    
                    try:
                        bet_sel = int(input("\nMake a Bet: "))
                    
                    except ValueError:
                        bet_sel = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
                    
                    if bet_sel > player_data['Financials']['Balance']:
                        print("You can't bet that much.")
                    
                    else:
                        
                        if bet_sel == 1:
                            bet += 1
                            player_data['Financials']['Balance'] -= 1
                        
                        elif bet_sel == 2:
                            bet += 5
                            player_data['Financials']['Balance'] -= 5
                    
                        
                        elif bet_sel == 3:
                            bet += 10
                            player_data['Financials']['Balance'] -= 10
                            
                        
                        elif bet_sel == 4:
                            bet += 25
                            player_data['Financials']['Balance'] -= 25
                            
                        
                        elif bet_sel == 5:
                            try:
                                cbet = int(input("Place Your Bet: "))
                            
                            except ValueError:
                                cbet = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
                                
                            bet += cbet
                            player_data['Financials']['Balance'] -= cbet

                        
                        elif bet_sel == 6:
                            
                            usr_cards = []
                            dlr_cards = []
                            c_counted = []
                            
                            deal_cards = 4
                            dlr_count = 0
                            usr_count = 0
                            
                            
                            bjack_loop = True
                            while bjack_loop:
                                
                                # Card Dealing Begins Here ---------------------
                                
                                while deal_cards != 0:
                                    
                                    if deal_cards > 2:
                                        
                                        rng_sel = random.randint(0, len(card_deck) - 1)
                                        card_sel = card_deck[rng_sel]
                                        
                                        if card_sel in dlr_cards:
                                            rng_sel = random.randint(0, len(card_deck) - 1)
                                            card_sel = card_deck[rng_sel]
                                        
                                        else:
                                            dlr_cards.append(card_sel)
                                            deal_cards -= 1
                                        
                                    
                                    else:
                                        rng_sel = random.randint(0, len(card_deck) - 1)
                                        card_sel = card_deck[rng_sel]
                                        
                                        if card_sel in usr_cards or card_sel in dlr_cards:
                                            rng_sel = random.randint(0, len(card_deck) - 1)
                                            card_sel = card_deck[rng_sel]
                                            
                                        
                                        else:
                                            usr_cards.append(card_sel)
                                            deal_cards -= 1                                            
                                        
                                # Card Calculation Begins Here -----------------
                                
                                """ Starts off with the Player Loop """
                                print("\n--- Your Cards ---")
                                card_loop = True
                                while card_loop:
                                    
                                    for card in usr_cards:
                                        print("|", card, end = " |")
                                
                                        if 'K'in card or 'Q' in card or 'J' in card or card[:2:] == '10':
                                            usr_count += 10
                                        
                                        elif 'A' in card:
                                            usr_count += 11
                                        
                                        else:
                                            usr_count += int(card[0])
                                        
                                        c_counted.append(card)
                                    
                                    usr_cards = []
                                    
                                    if usr_count > 21:
                                        
                                        print("\nDealer: You're BUST buddy...")
                                        break
                                        
                                    elif usr_count == 21: 
                                        
                                        print("\nYou... you were just lucky..") 
                                        print("Player has", usr_count)
                                        break
                                    
                                    else:
                
                                        print()
            
                                        print("\nYou have: ", usr_count)
                                        print("--- Game Menu ---")
                                        print("1.) Hit")
                                        print("2.) Stay")
                                        
                                        try:
                                            hsmove = int(input("\nWill you hit or will you stay? "))
                                        
                                        except ValueError:
                                            hsmove = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
                                        
                                        if hsmove == 1:
                                            rng_sel = random.randint(0, len(card_deck) - 1)
                                            card_sel = card_deck[rng_sel]
                                            
                                            if card_sel in c_counted:
                                                print("Duplicate Card Found --- Line 155", card_sel)
                                                rng_sel = random.randint(0, len(card_deck) - 1)
                                                card_sel = card_deck[rng_sel]
                                            
                                            else:
                                                usr_cards.append(card_sel)
                                        
                                        elif hsmove == 2:
                                            break                                        
                                    
                                deal_loop = True
                                while deal_loop:
                                    print()
                                
                                    for card in dlr_cards:
                                        print("Dealer Flips: ", "|", card, "|")
                                        
                                        if 'K' in card or 'Q' in card or 'J' in card or card[:2:] == '10':
                                            dlr_count += 10
                                        
                                        elif 'A' in card:
                                            dlr_count += 11
                                        
                                        else:
                                            dlr_count += int(card[0])
                                        
                                        c_counted.append(card)
                                        
                                    
                                    dlr_cards = []
                                        
                                    print("Dealer has: ", dlr_count)
                                    
                                    if dlr_count > 21:
                                        
                                        break
                                    
                                    elif dlr_count == 21:
                                        
                                        print("Dealer Wins")
                                        bet = 0
                                        
                                        break
                                    
                                    else:
                                        
                                        if dlr_count <= 16:
                                            
                                            rng_sel = random.randint(0, len(card_deck) - 1)
                                            card_sel = card_deck[rng_sel]
                                            
                                            if card_sel in c_counted:
                                                rng_sel = random.randint(0, len(card_deck) - 1)
                                                card_sel = card_deck[rng_sel]
                                            
                                            else:
                                                dlr_cards.append(card_sel)
                                        
                                        elif dlr_count >= 18:
                                            print("Dealer Holds")
                                            break
                                            
                                        else:
                                            
                                            dlr_rng = random.randint(1, 11)
                                            chance = dlr_rng/10
                                            
                                            if chance > 50:
                                                rng_sel = random.randint(0, len(card_deck) - 1)
                                                card_sel = card_deck[card_sel]
                                                
                                                if card_sel in dlr_cards:
                                                    rng_sel = random.randint(0, len(card_deck) - 1)
                                                    card_sel = card_deck[card_sel]
                                                
                                                else:
                                                    dlr_cards.append(card_sel)
                                            
                                            else:
                                                print("Dealer Holds") 
                                                break
                            
                                if usr_count > dlr_count and usr_count <= 21:

                                    print("\nPlayer Wins", bet*2)
                                    player_data['Financials']['Balance'] += bet * 2
                                    bet = 0
                                   
                                    break
                                    
                                elif usr_count < dlr_count and dlr_count <= 21:
                                    print("\nDealer Wins")
                                    bet = 0
                                   
                                    break
                                
                                elif usr_count < dlr_count and usr_count <= 21 and dlr_count > 21:
                                    print("\nPlayer Wins", bet*2)
                                    player_data['Financials']['Balance'] += bet * 2
                                    bet = 0
                                    break
                                
                                elif dlr_count > usr_count and dlr_count <= 21:
                                    print("\nDealer Wins")
                                    bet = 0
                                
                                elif dlr_count < usr_count and usr_count > 21:
                                    print("\nDealer Wins")
                                    bet = 0
                                    break
                                    
                                elif usr_count == dlr_count:
                                    print("\nNo One Wins")
                                    bet = 0
                                    break
                                
                                else:
                                    print("\nNo One Wins")
                                    bet = 0
                                    break
                                
                                break
                                        
                        elif bet_sel == 7:
                            break                        
                    
        elif game_sel == 2:
            print("Ask an NPC for some money like a bum here...")
        
        elif game_sel == 3:
            print("The NPC Plays itself here")
        
        elif game_sel == 4:
            break


player_data = {'Financials': {
    'Balance': 1000
}}

play_blackjack(player_data)