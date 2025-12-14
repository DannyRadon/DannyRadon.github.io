# Slot Machines Game Code Here ------------------------------------------------

def play_slots(player_data):
    
    slot_wheel = ['BAR', 'Cherry', 'Bell', 'Peach', '7', 'Grape']
    
    mini_game = True
    
    while mini_game:
        
        print("\nYou are now playing Slots!")
        print("\n--- Slots Menu ---")
        
        print("1.) Make a Bet")
        print("2.) Exit Slots")
        
        try:
            p_select = int(input("\nPlease make a selection from the menu: "))
        
        except ValueError:
            p_select = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
        
        if p_select == 1:
            
            bet = 0
            bet_mode = True
            
            while bet_mode:
                
                print("\n--- BETTING MENU ---")
                print("\nCurrent Bet:", bet, "Credits Left: ", player_data['Financials']['Balance'])
                
                print("\n1.) Bet 1 Credit")
                print("2.) Bet 5 Credits")
                print("3.) Bet 10 Credits")
                print("4.) Bet 25 Credits")
                print("5.) Bet 50 Credits")
                print("6.) Bet 100 Credits")
                print("7.) Enter Custom Amount")
                print("8.) Place Bet & Spin")
                
                print("\n9.) Exit Betting Menu")
                
                try:
                    p_bet = int(input("Please choose an option: "))
                
                except ValueError:
                    p_bet = int(input("Invalid Input -- Enter Numbers Only. Please Try Again: "))
                
                if p_bet > player_data['Financials']['Balance']:
                    print("You don't have enough credits to make that bet...")
                
                elif p_bet == 9:
                    break
                
                else:
                    
                    if p_bet == 1:
                        bet += 1
                        player_data['Financials']['Balance'] -= 1
                    
                    elif p_bet == 2:
                        bet += 5
                        player_data['Financials']['Balance'] -= 5                        
                    
                    elif p_bet == 3:
                        bet += 10
                        player_data['Financials']['Balance'] -= 10                        
                    
                    elif p_bet == 4:
                        bet += 25
                        player_data['Financials']['Balance'] -= 25
                    
                    elif p_bet == 5:
                        bet += 50
                        player_data['Financials']['Balance'] -= 50
                    
                    elif p_bet == 6:
                        bet += 100
                        player_data['Financials']['Balance'] -= 100                        
                    
                    elif p_bet == 7:
                        bet = int(input("Enter Bet Amount: "))
                        player_data['Financials']['Balance'] -= bet 
                    
                    elif p_bet == 8:
                        
                        print()
                        
                        rolls = 3
                        combo = []
                        
                        while rolls != 0:
                            
                            s_pick = random.randint(0, len(slot_wheel) - 1)
                            
                            slot_item = slot_wheel[s_pick]
                            combo.append(slot_item)
                            
                            rolls -= 1
                                
                        print(combo)
                        
                        if combo[0] == combo[1] == combo[2]:
                            
                            print("\nWINNER")
                            
                            if combo[0] == '7':
                                
                                pay = bet*50
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay 
                                bet = 0
                            
                            elif combo[0] == 'Cherry':
                                
                                pay = bet*30
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay
                                bet = 0
                            
                            elif combo[0] == 'Bell':
                                
                                pay = bet*25
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay
                                bet = 0
                            
                            elif combo[0] == 'BAR':
                                
                                pay = bet*10
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay
                                bet = 0
                            
                            elif combo[0] == 'Peach':
                                
                                pay = bet*6
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay
                                bet = 0
                            
                            elif combo[0] == 'Grape':
                                
                                pay = bet*4
                                print("You've Won", pay)
                                player_data['Financials']['Balance'] += pay
                                bet = 0
                        
                        elif combo[0] == 'BAR' and combo[1] == 'BAR' or combo[0] == 'BAR' and combo[2] == 'BAR' or combo[1] == 'BAR' and combo[2] == 'BAR':
                            
                            pay = bet*2
                            print("You've Won", pay)
                            player_data['Financials']['Balance'] += pay
                            bet = 0
                                
                        else:
                            
                            print("LOSER")
                            bet = 0
                            
                    else:
                        break        
        else:
            break

# -----------------------------------------------------------------------------