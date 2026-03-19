#------------------------------------------------------------------------------
# Program: Untitled Space Game
# Version: 0.00
# Date: March 6th, 2025
#------------------------------------------------------------------------------

# Random Name Generator Function

def generateUniverse():
    
    # Random Name Generation Setup Area
    
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
             'R','S','T','U','V','W','X','Y','Z']
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V',
            'W','X','Y','Z']
    
    """ These lists with characters are used to generate all the random names
    used for each star and planet. They're used in the Planet Gen. and Star Gen.
    blocks below. """
    
    name_prefix = [] 
    starList = []
    
    # Total Stars in Random Universe Generated
    
    starTotal = random.randint(80, 120)
    
    print("\nThere are", starTotal, "stars in this generated universe.") 
    
    """ This area takes a random number from a range to use as the totat star
    count for the randomly generated universe. """
    
    # Random Name Generation Area
    
    for letter in vowels:
        
        for char in alpha:
            
            name_prefix.append(letter + char.lower())
            
            """ This area established the name prefix with two letters; one
            vowel with every alphabetical character. Adds to a list ('prefix') 
            to be used later through concatenation. """
         
    for i in range(starTotal):
        
        charLength = random.randint(3, 5)
        
        preSelector = random.randint(0, len(name_prefix) - 1)
        vowSelector = random.randint(0, len(vowels) - 1)
        vowSelector2 = random.randint(0, len(vowels) -1)
        consSelector = random.randint(0, len(cons) - 1)
        
        # Random Name Generation & Assignment Beings (Star Names)
        
        if charLength == 3:
            
            optSelect = random.randint(1, 3)
            
            if optSelect == 1:
                
                starName = vowels[vowSelector] + cons[consSelector].lower() + vowels[vowSelector2].lower()
            
            elif optSelect == 2:
                
                starName = name_prefix[preSelector] + vowels[vowSelector].lower()
            
            elif optSelect == 3:
                
                starName = cons[consSelector] + name_prefix[preSelector].lower()
            
            else:
                print("Something went wrong here. 3 Char name, out of range.")
            
            starList.append(starName)
            
        elif charLength == 4:
            
            optSelect = random.randint(1, 3)
            
            if optSelect == 1:
                
                starName = cons[consSelector] + name_prefix[preSelector].lower() + vowels[vowSelector].lower()
            
            elif optSelect == 2:
                
                starName = name_prefix[preSelector] + vowels[vowSelector].lower() + cons[consSelector].lower()
            
            elif optSelect == 3:
                
                starName = vowels[vowSelector] + cons[consSelector].lower() + name_prefix[preSelector].lower()
            
            else:
                print("Something went wrong here. 4 Char Name, out of range")
            
            starList.append(starName)
        
        elif charLength == 5:
            
            optSelect = random.randint(1, 3)
            
            if optSelect == 1:
                
                starName = name_prefix[preSelector] + vowels[vowSelector].lower() + cons[consSelector].lower() + vowels[vowSelector].lower()
            
            elif optSelect == 2:
                
                starName = vowels[vowSelector] + cons[consSelector].lower() + name_prefix[preSelector].lower() + vowels[vowSelector].lower()
            
            elif optSelect == 3:
                
                starName = cons[consSelector] + vowels[vowSelector].lower() + name_prefix[preSelector].lower() + vowels[vowSelector].lower()
            
            else:
                print("Something went wrong here with character length select.")
            
            starList.append(starName)
            # End of Random Name Generation for Stars
    
    # Dictionary Created --- Storage of Universe Data
    universeData = {}
    universeData['Star'] = {}
    
    """ This dictionary holds all of the stars generated so far. """
    
    # Random Planet Name Generation Begins & Star/Planet System Assignment Begins
    
    for star in starList:
        
        universeData['Star'][star] = {'Planets': []}
        planetCount = random.randint(3,9)
        
        for planet in range(planetCount):
            
            charLength = random.randint(3, 4)
            
            preSelector = random.randint(0, len(name_prefix) - 1)
            vowSelector = random.randint(0, len(vowels) - 1)
            vowSelector2 = random.randint(0, len(vowels) -1)
            consSelector = random.randint(0, len(cons) - 1) 
            
            if charLength == 3:
                
                optSelect = random.randint(1, 3)
                
                if optSelect == 1:
                    
                    planetName = vowels[vowSelector] + cons[consSelector].lower() + vowels[vowSelector2].lower()
                
                elif optSelect == 2:
                    
                    planetName = name_prefix[preSelector] + vowels[vowSelector].lower()
                
                elif optSelect == 3:
                    
                    planetName = cons[consSelector] + name_prefix[preSelector].lower()
                
                else:
                    print("Something went wrong here. 3 Char name, out of range.")
                
                universeData['Star'][star]['Planets'].append(planetName)
                
            elif charLength == 4:
                
                optSelect = random.randint(1, 3)
                
                if optSelect == 1:
                    
                    planetName = cons[consSelector] + name_prefix[preSelector].lower() + vowels[vowSelector].lower()
                
                elif optSelect == 2:
                    
                    planetName = name_prefix[preSelector] + vowels[vowSelector].lower() + cons[consSelector].lower()
                
                elif optSelect == 3:
                    
                    planetName = vowels[vowSelector] + cons[consSelector].lower() + name_prefix[preSelector].lower()
                
                else:
                    print("Something went wrong here. 4 Char Name, out of range")
                
                universeData['Star'][star]['Planets'].append(planetName)
                    
                if planetName in starList:
                    print("Found a duplicate! between star and planet names")
                    
                else:
                    pass           
    
    # Start Position Randomizer
    
    system_start = random.randint(0, len(universeData) - 1)
    
    # Start Position Assignment to Player
    
    system_start = starList[system_start]
    universeData['player_location'] = system_start
    
    return universeData



# Main Game Base Code Function --- USED FOR TESTING ----------------------------

def mainGame():
    universeData = generateUniverse()
    
    print("The Game Begins...")
    print(len(universeData), "stars in this universe")
    print()
    print("You wake up...")
    print("You're laying in bed inside an unlit dormitory unit...")
    
    player_move = input("What's your next move? ")
    
universeData = generateUniverse()
print(universeData)

for star in universeData['Star']:
    
    if star == 'player_location':
        pass
    
    else:
        sys_size = len(universeData['Star'][star]['Planets'])
        
        
        if sys_size == 2 or sys_size == 3:
            
            type_rng = random.randint(0, 8)
            
            
            if 0 <= type_rng <= 1:
                
                star_type = 'Red Giant'
                planet_types = ['Ice Giant', 'Gas Giant']
            
            elif 2 <= type_rng <= 4:
                
                star_type = 'Sun-Like'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
            elif 5 <= type_rng <= 6:
                
                star_type = 'Orange Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
            elif 7 <= type_rng <= 8:
                
                star_type = 'Red Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
        
        elif sys_size == 4 or sys_size == 5 or sys_size == 6:
            
            type_rng = random.randint(0, 9)
            
            
            if 0 <= type_rng <= 4:
                
                star_type = 'Red Giant'
                planet_types = ['Ice Giant', 'Gas Giant']
                
            elif 5 <= type_rng <= 7:
                
                star_type = 'Sun-Like'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
                
            elif type_rng == 8:
                
                star_type = 'Orange Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
            elif type_rng == 9:
                
                star_type = 'Red Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
        
        elif sys_size == 7 or sys_size == 8 or sys_size == 9:
            
            type_rng = random.randint(0, 9)
            
            if 0 <= type_rng <= 1:
                
                star_type = 'Red Giant'
                planet_types = ['Gas Giant', 'Ice Giant']
            
            elif 2 <= type_rng <= 7:
                
                star_type = 'Sun-Like'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
            elif type_rng == 8:
                
                star_type = 'Orange Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
            
            elif type_rng == 9:
                
                star_type = 'Red Dwarf'
                planet_types = ['Rocky Terrestrial', 'Super Earth', 'Gas Giant', 'Ice Giant']
                
            
        universeData['Star'][star]['Type'] = star_type
            
        list_copy = universeData['Star'][star]['Planets']
        universeData['Star'][star]['Planets'] = {}
        
        G = (6.67*10)**(-11)
        erad = 6371000
        emas = 5.972 * (10**27)
        
        for planet in list_copy:
                
            ptype_rng = random.randint(0, len(planet_types) - 1)
            ptype_sel = planet_types[ptype_rng]
            
            if ptype_sel == 'Rocky Terrestrial':
                
                size_rng = random.uniform(0.3, 1.5)
                
                if size_rng <= 0.8:
                    mass = size_rng**(3.0)
                
                else:
                    mass = size_rng**(3.5)
                
                grav = (G * (mass * emas)) / (size_rng * erad)
            
            elif ptype_sel == 'Super Earth':
                
                size_rng = random.uniform(1.6, 2.2)
                mass = size_rng**(3.5)
                grav = (G * (mass * emas)) / (size_rng * erad)
            
            elif ptype_sel == 'Gas Giant':
                
                size_rng = random.uniform(3.0, 30.0)
                
                
                if size_rng <= 15:
                    mass = size_rng**(2.3)
                
                else:
                    ptype_sel = 'Super Gas Giant'
                    mass = size_rng**(2.1)
                
                
                grav = (G * (mass * emas)) / (size_rng * erad)
            
            elif ptype_sel == 'Ice Giant':
                
                size_rng = random.uniform(2.0, 6.0)
                mass = size_rng**(2.1)
                grav = (G * (mass * emas)) / (size_rng * erad)
            
            else:
                print("Something happened here with the size generation...")
                
                
                
                
            universeData['Star'][star]['Planets'][planet] = {'Name': planet,
                                                        'Type': ptype_sel,
                                                        'Comp': 'Fill Data Here',
                                                        'Size': size_rng,
                                                        'Mass': mass,
                                                        'Temp': 'Fill Data Here',
                                                        'Grav': grav,
                                                        'Host': star,
                                                        'NAVS': list_copy,
                                                        'Stations': None}
        
             
print("\nUniverse Loaded...") 
print(universeData, "-- DEBUG From Universe Generation Script")

for star in universeData['Star']:
    
    if star == 'player_location':
        pass
    
    else:
        for planet in universeData['Star'][star]['Planets']:
            
            if planet == 'player_location':
                pass
            
            else:
            
                type_check = universeData['Star'][star]['Planets'][planet]['Type']
                
                if type_check == 'Rocky Terrestrial' and universeData['Star'][star]['Type'] == 'Red Giant':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.1, 250)
                    
                    
                    
                
                elif type_check == 'Rocky Terrestrial' and universeData['Star'][star]['Type'] == 'Sun-Like':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.1, 50)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.1 <= dist_check < 0.5:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Volcanic'
                    
                    elif 0.5 <= dist_check < 0.85:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Desert'
                    
                    elif 0.85 <= dist_check < 2.5:
                        
                        sel_rng = random.randint(0, 2)
                        
                        if sel_rng == 0:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Earth Like)'
                        
                        elif sel_rng == 1:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Ocean)'
                        
                        elif sel_rng == 2:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Desert)'
                    
                    elif 2.5 <= dist_check < 5.0:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Ocean)'
                    
                    elif 5.0 <= dist_check < 30:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Icy Rock)'
                    
                    elif 30 <= dist_check <= 50:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Cryo-Volcanic)'
                            
                    
                
                
                elif type_check == 'Rocky Terrestrial' and universeData['Star'][star]['Type'] == 'Orange Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.05, 12)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.05 <= dist_check < 0.1:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Volcanic'
                    
                    elif 0.1 <= dist_check < 1:
                        
                        rng_sel = random.randint(0, 2)
                        
                        if rng_sel == 0:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Earth-Like)'
                        
                        elif rng_sel == 1:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Desert)'
                        
                        elif rng_sel == 2:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Ocean)'
                    
                    elif 1 <= dist_check < 3:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Ocean)'
                    
                    elif 3 <= dist_check < 10:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Icy Rock)'
                    
                    elif 10 <= dist_check <= 12:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Cryo-Volcanic)'
                        
                    
    
                    
                elif type_check == 'Rocky Terrestrial' and universeData['Star'][star]['Type'] == 'Red Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.01, 1.5)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.01 <= dist_check < 0.05:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Volcanic'
                    
                    elif 0.05 <= dist_check < 0.3:
                        
                        rng_sel = random.randint(0, 3)
                            
                        if rng_sel == 0:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Earth-Like)'
                            
                        elif rng_sel == 1:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Ocean)'
                        
                        elif rng_sel == 2:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Temperate (Desert)'
                        
                        elif rng_sel == 3:
                            universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Ocean)'
                    
                    elif 0.3 <= dist_check < 1.:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Icy Rock)'
                    
                    elif 1.0 <= dist_check <= 1.5:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Rocky - Frozen (Cryo-Volcanic)'
                    
                    
                        
                
                elif type_check == 'Super Earth' and universeData['Star'][star]['Type'] == 'Red Giant':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(2, 15)
                    
                elif type_check == 'Super Earth' and universeData['Star'][star]['Type'] == 'Sun-Like':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.5, 4)
                
                
                elif type_check == 'Super Earth' and universeData['Star'][star]['Type'] == 'Orange Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.3, 2)
                
                elif type_check == 'Super Earth' and universeData['Star'][star]['Type'] == 'Red Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.1, 1)
                    
                    
        
                
                elif type_check == 'Gas Giant' and universeData['Star'][star]['Type'] == 'Red Giant':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(5, 150)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 5 <= dist_check < 30:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Hot Jupiter'
                    
                    elif 30 <= dist_check < 100:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Standard'
                    
                    elif 100 <= dist_check <= 150:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Super Jupiter'
                        
                
                elif type_check == 'Gas Giant' and universeData['Star'][star]['Type'] == 'Sun-Like':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.02, 30) 
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.02 <= dist_check < 3:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Hot Jupiter'
                    
                    elif 3 <= dist_check < 20:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Standard'
                    
                    elif 20 <= dist_check <= 30:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Super Jupiter'
                        
                    
                
                elif type_check == 'Gas Giant' and universeData['Star'][star]['Type'] == 'Orange Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.01, 8) 
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.01 <= dist_check < 1:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Hot Jupiter'
                    
                    elif 1 <= dist_check < 5:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Standard'
                    
                    elif 5 <= dist_check <= 8:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Super Jupiter'
                        
                        
                
                elif type_check == 'Gas Giant' and universeData['Star'][star]['Type'] == 'Red Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.005, 2)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.005 <= dist_check < 0.3:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Hot Jupiter'
                    
                    elif 0.3 <= dist_check < 0.5:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Standard'
                    
                    elif 0.5 <= dist_check <= 2:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Gas - Super Jupiter'
                
    
                
                elif type_check == 'Super Gas Giant' and universeData['Star'][star]['Type'] == 'Red Giant':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(10, 100)
                
                elif type_check == 'Super Gas Giant' and universeData['Star'][star]['Type'] == 'Sun-Like':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(5, 20)
                
                elif type_check == 'Super Gas Giant' and universeData['Star'][star]['Type'] == 'Orange Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(3, 10)  
                
                elif type_check == 'Super Gas Giant' and universeData['Star'][star]['Type'] == 'Red Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(1, 5) 
                
    
                
                
                elif type_check == 'Ice Giant' and universeData['Star'][star]['Type'] == 'Red Giant':
                    
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(30, 200)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 30 <= dist_check < 100:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - (Neptune-Like)'
                    
                    elif 100 <= dist_check <= 200:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - (Super Ice Giant)'
                        
                    
                    
                
                elif type_check == 'Ice Giant' and universeData['Star'][star]['Type'] == 'Sun-Like':
                    
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(5, 50) 
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 5 <= dist_check < 20:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Regular (Neptune-Like)'
                    
                    elif 20 <= dist_check <= 50:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Super Giant'      
                        
                        
                        
                
                elif type_check == 'Ice Giant' and universeData['Star'][star]['Type'] == 'Orange Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(2, 15)
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 2 <= dist_check < 5:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Regular (Neptune-Like)'
                    
                    elif 5 <= dist_check <= 15:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Super Giant'   
                        
                        
                        
                        
                elif type_check == 'Ice Giant' and universeData['Star'][star]['Type'] == 'Red Dwarf':
                    universeData['Star'][star]['Planets'][planet]['Star Dist'] = random.uniform(0.5, 3)  
                    
                    dist_check = universeData['Star'][star]['Planets'][planet]['Star Dist']
                    
                    if 0.5 <= dist_check < 1:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Regular (Neptune-Like)'
                    
                    elif 1 <= dist_check <= 3:
                        universeData['Star'][star]['Planets'][planet]['Type'] = 'Ice Giant - Super Giant'                    
                    
"""                
with open("universe_data.json", "w", encoding="utf-8") as f:
    json.dump(universeData, f, indent=4) 
"""
