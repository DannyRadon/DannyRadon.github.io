#------------------------------------------------------------------------------#
# Name: Dave & Dan's Dangerous Dig
# Version: 0.65 Alpha
# Date: May 31st 2025 (Started) --- June 18th 2025 (Current)
#------------------------------------------------------------------------------#

#-------------- Notes: --------------------------------------------------------#
#
#      Swap out all hard coded values of tile sizes and resolutions sizes with 
#    the tuple sets found in the game_data dictionary, so it can be changed from
#    the options menu.
#
#    LEFT TO DO:
#
#    - Add in More Collectible Items for Player
#    - Refactor the Entire Codebase for Niceness
#    - Implement Sound Options in Options Menu
#    - Fix the "Flying Jump" Issue
#    - Put in Monster NPC Sprites
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Import Pool

import sys
import subprocess

try:
    import pygame

except ModuleNotFoundError:

    print("PyGame Module Not Found -- Would You Like to Install PyGame? (Y/N) ")
    user_in = input("").lower()

    if user_in == 'y' or user_in == 'yes':

        subprocess.check_call([

            sys.executable, "-m", "pip", "install", "pygame==2.6.1"

        ])
        import pygame

    elif user_in == 'n' or user_in == 'no':
        print("Unable to Load 'Dan & Dave's Dangerous Dig' -- PyGame 2.6.1 Required")

import pickle
import random


# Screen Resolution Initialization

s_width = 1024
s_height = 768


# Font Rendering Initialization

pygame.font.init()
font = pygame.font.SysFont('8514oem', 26)
font2 = pygame.font.SysFont('8514oem', 33)
menu_font = pygame.font.SysFont('8514oem', 66)


# Player Data Dictionary Initialization

player_data = {'Health': 7,
               'Score': 0,
               'Lives': 3,
               'Items': ['Dynamite', None],
               'Curr_Item': None,
               'Coins': 0,
               'Spawn': (42, 1),
               'Sprite Data': None,
               'Character': None,
               'Map Track': None,
               'On Ground': True
               
               }

# Game Data Dictionary Initialization

game_data = {'Diff': 'Easy',
             'Video': {'Resolution': (s_width, s_height),
                       'Tile Size': 44},
             'Sound': {'Music Volume': 100,
                       'SFX Volume': 100}
             }
                       


# Compiling Levels Function

def compile_map(file):
    
    with open(file, 'r') as level:
        
        row_ind = 0
        game_world = []
        
        for row in level:
            
            row = row.strip()
            
            row_data = []
            tile_ind = 0
            
            for tile in row:
                
                if tile == '#':
                    tile = 0
                    player_data['Spawn'] = (tile_ind, row_ind)
                
                if tile == '^':
                    tile = 11
                
                if tile == '&':
                    tile = 12
                
                if tile == '$':
                    tile = 13
                    
                row_data.append(int(tile))
                tile_ind += 1
                
            game_world.append(row_data)
            row_ind += 1
        
    return game_world



# Loading Levels Function

def load_map(game_data, map_ind, map_list):
    
    map_diff = game_data['Diff']
    
    curr_map = map_list[map_ind]        
    
    # File Directory for Levels
    map_dir = 'levels/'
    
    # Easy Mode
    if game_data['Diff'] == 'Easy':
        
        map_sel = map_dir + map_list[map_ind] + "_E.txt"
        game_world = compile_map(map_sel)
    
    # Medium Mode
    elif game_data['Diff'] == 'Medium':
        
        map_sel = map_dir + map_list[map_ind] + "_M.txt"
        game_world = compile_map(map_sel) 
    
    # Hard Mode
    elif game_data['Diff'] == 'Hard':
        
        map_sel = map_dir + map_list[map_ind] + "_H.txt"
        game_world = compile_map(map_sel)       
    
    return game_world


def save_game(player_data, game_world, npc_list):
    
    with open("Saved Games/save_game.txt", "w") as save_file:
        
        row_ind = 0
        tile_ind = 0
        
        for row in game_world:
            for tile in row:
                
                for npc_enemy in npc_list:
                    
                    npc_pos_x = int(npc_enemy.x_pos)
                    npc_pos_y = int(npc_enemy.y_pos)
                    
                    if npc_pos_x == tile_ind and npc_pos_y == row_ind:
                        tile = 5
                
                tile_ind += 1
                
                save_file.write(str(tile))
                
            tile_ind = 0
            row_ind += 1                
            
            save_file.write("\n")    
    
    with open ("Saved Games/save_data.pkl", "wb") as save_data:
        
        pickle.dump(player_data, save_data)
    


def load_game():
    
    save_game = "save_game.txt"     
    
    # Save Directory for Levels
    save_dir = 'Saved Games/'
    
    save_file = save_dir + save_game
    game_world = compile_map(save_file)
    
    with open ("Saved Games/save_data.pkl", "rb") as saved_data:
        
        player_data = pickle.load(saved_data)
    
    return game_world, player_data    
    


# Game World & Tile Initialization

tile_size = 44



# Player Position & Direction Initialization

def player_init(player_data):
    
    player_Locx = player_data['Spawn'][0]
    player_Locy = player_data['Spawn'][1]
    
    player_newLocx = 0
    player_newLocy = 0
    
    player_Dirx = 0
    player_Diry = 1
    
    player_data['Sprite Data'] = player_Dirx
    
    return player_Locx, player_Locy, player_newLocx, player_newLocy, player_Dirx, player_Diry


# Active Object List Pools


prj_list = []
fx_list = []
npc_list = []
witem_list = []

msg_timer = 0


# Action - Throwable Item Function Initialization 

class Projectile:
    
    def __init__(self, prj_xPos, prj_yPos, prj_dir, prj_throw):
        
        self.prj_xPos = prj_xPos
        self.prj_yPos = prj_yPos
        
        self.prj_xVel = 0.5 * player_Dirx
        self.prj_yVel = 0.5
        self.grav = 0.1
        
        self.prj_dir = prj_dir
        self.angle = 0
        
        self.prj_throw = player_data['Curr_Item']
        self.prj_img = None
        
        self.active = True
        
    
    def update_prj(self, game_world, npc_list):
        
        if not self.active:
            return
        
        self.prj_xPos += self.prj_xVel
        
        self.prj_yVel -= self.grav
        
        self.prj_yPos -= self.prj_yVel
        
        prj_xPosNext = self.prj_xPos + 1
        prj_yPosNext = self.prj_yPos + 1
        
        self.angle -= 45
        
        if self.prj_throw == 'Pickaxe':
            
            try:
                if game_world[int(self.prj_yPos)][int(self.prj_xPos)] in (1, 3):
                    self.active = False
            
            except IndexError:
               
                print("Crash --- Projectile X Init:", self.prj_xPos)
                print("Crash --- Projectile Y Init:", self.prj_yPos)
        
        elif self.prj_throw == 'Dynamite':
            
            
            next_x = int(self.prj_xPos + self.prj_xVel)
            next_y = int(self.prj_yPos - self.prj_yVel)  
            
        
            if 0 <= next_y < len(game_world) and 0 <= next_x < len(game_world[0]):
                
        
                if game_world[int(self.prj_yPos)][next_x] in (1, 3):
                    self.prj_xVel *= -1
                    
                    if self.prj_xVel < 0:
                        self.prj_xVel += 0.1
                    
                    elif self.prj_xVel > 0:
                        self.prj_xVel -= 0.1       
            
        
                if game_world[next_y][int(self.prj_xPos)] in (1, 3):
                    self.prj_yVel *= -0.7  
                    
                    
                    if self.prj_yVel > 0:
                        self.prj_yVel -= 0.15                    
            
             
                    if abs(self.prj_yVel) < 0.1:
                        
                        self.prj_yVel = 0
                        self.prj_xVel = 0
                        
                        for monster in npc_list:
                            
                            if abs(self.prj_xPos - monster.x_pos) <= 2 and abs(self.prj_yPos - monster.y_pos) < 2:
                                monster.alive = False
                                player_data['Score'] += 300
                        
                        for crate in witem_list:
                            
                            if abs(self.prj_xPos - crate.x_pos) <= 2 and abs(self.prj_yPos - crate.y_pos) < 2:
                                crate.broken = True
                        
                        self.active = False
                                    
            else:
                prj.active = False
                

        for monster in npc_list:
            
            if round(self.prj_xPos) == round(monster.x_pos) and round(self.prj_yPos) == round(monster.y_pos):
                self.active = False
                monster.alive = False
                player_data['Score'] += 300



    def draw_prj(self, game_world):
        
        if self.prj_throw == 'Pickaxe':
            self.prj_img = prj_axe
            self.prj_img = pygame.transform.rotate(self.prj_img, self.angle)     
        
        if self.prj_throw == 'Dynamite':
            self.prj_img = dyn_r
            self.prj_img = pygame.transform.rotate(self.prj_img, self.angle)
        
        game_screen.blit(self.prj_img, (self.prj_xPos * tile_size - camera_x, self.prj_yPos * tile_size - camera_y))




def item_throw(player_data, game_world):
    
    if player_data['Curr_Item'] in ('Pickaxe', 'Dynamite'):
        
        prj_throw = player_data['Curr_Item']
        
        projectile = Projectile(player_Locx, player_Locy, player_Dirx, prj_throw)
        prj_list.append(projectile)
        
        return projectile




def item_use(player_data):
    
    item_sel = player_data['Curr_Item']
    
    if player_data['Health'] < 7:
        
        if item_sel == 'Water':
            
            if player_data['Health'] + 1 > 7:
                
                player_data['Health'] = 7
                player_data['Items'].remove(item_sel)
                player_data['Curr_Item'] = player_data['Items'][-1]
                
                msg_box = font.render("You drank some Water! +1 HP", False, (255, 255, 255))
                msg_rect = msg_box.get_rect()
        
                msg_rect.x = (s_width * 0.025)
                msg_rect.y = (s_height * 0.025)   
                    
                msg_timer = 30               
            
            else:
                
                player_data['Health'] += 1
                player_data['Items'].remove(item_sel)
                player_data['Curr_Item'] = player_data['Items'][-1]
                
                msg_box = font.render("You drank some Water! +1 HP", False, (255, 255, 255))
                msg_rect = msg_box.get_rect()
        
                msg_rect.x = (s_width * 0.025)
                msg_rect.y = (s_height * 0.025)   
                    
                msg_timer = 30                
        
        
    
        elif item_sel == 'h_kit':
            
            if player_data['Health'] + 3 > 7:
                
                player_data['Health'] = 7
                player_data['Items'].remove(item_sel)
                player_data['Curr_Item'] = player_data['Items'][-1]
                
                msg_box = font.render("You used a First Aid Kit! - +3 HP", False, (255, 255, 255))
                msg_rect = msg_box.get_rect()
        
                msg_rect.x = (s_width * 0.025)
                msg_rect.y = (s_height * 0.025)   
                    
                msg_timer = 30                
            
            else:
                
                player_data['Health'] += 3
                player_data['Items'].remove(item_sel)
                player_data['Curr_Item'] = player_data['Items'][-1]
                
                msg_box = font.render("You used a First Aid Kit! - +3 HP", False, (255, 255, 255))
                msg_rect = msg_box.get_rect()
        
                msg_rect.x = (s_width * 0.025)
                msg_rect.y = (s_height * 0.025)   
                    
                msg_timer = 30
                
    
    else:
        msg_box = font.render("You're already at Full Health!", False, (255, 255, 255))
        msg_rect = msg_box.get_rect()
        
        msg_rect.x = (s_width * 0.025)
        msg_rect.y = (s_height * 0.025)   
                    
        msg_timer = 30
        
        
    return msg_box, msg_rect, msg_timer
    
    




# Screen Initialization

pygame.init()


game_screen = pygame.display.set_mode((s_width, s_height))
menu_screen = pygame.display.set_mode((s_width, s_height))

pygame.display.set_caption("D&Ds Dangerous Dig")




# Sprite & Texture Initializing Pool

border = pygame.image.load("g_assets/platform.jpg")
border = pygame.transform.scale(border, (tile_size, tile_size))

plat_1 = (142, 68, 85)

dave_spr_l = pygame.image.load("g_assets/d_dave_l.png")
dave_spr_lw = pygame.image.load("g_assets/d_dave_l_walk.png")
dave_spr_l_jf1 = pygame.image.load("g_assets/d_dave_l_JF1.png")
dave_spr_l_jf2 = pygame.image.load("g_assets/d_dave_l_JF2.png")
dave_spr_r = pygame.image.load("g_assets/d_dave_r.png")
dave_spr_rw = pygame.image.load("g_assets/d_dave_r_walk.png")
dave_spr_r_jf1 = pygame.image.load("g_assets/d_dave_r_JF1.png")
dave_spr_r_jf2 = pygame.image.load("g_assets/d_dave_r_JF2.png")


dave_hud = pygame.image.load("g_assets/splash_dave.png")
dave_life = pygame.image.load("g_assets/splash_dave.png")
dave_spr_l = pygame.transform.scale(dave_spr_l, (tile_size * 2, tile_size * 2))
dave_spr_r = pygame.transform.scale(dave_spr_r, (tile_size * 2, tile_size * 2))
dave_spr_lw = pygame.transform.scale(dave_spr_lw, (tile_size * 2, tile_size * 2))
dave_spr_rw = pygame.transform.scale(dave_spr_rw, (tile_size * 2, tile_size * 2))

dave_hud = pygame.transform.scale(dave_hud, (300, 300))
dave_life = pygame.transform.scale(dave_life, (30, 30))
dave_spr = dave_spr_r

dan_spr_l = pygame.image.load("g_assets/d_dan_l.png")
dan_spr_r = pygame.image.load("g_assets/d_dan_r.png")
dan_hud = pygame.image.load("g_assets/splash_dan.png")
dan_life = pygame.image.load("g_assets/splash_dan.png")
dan_spr_l = pygame.transform.scale(dan_spr_l, (tile_size * 2, tile_size * 2))
dan_spr_r = pygame.transform.scale(dan_spr_r, (tile_size * 2, tile_size * 2))
dan_hud = pygame.transform.scale(dan_hud, (290, 290))
dan_life = pygame.transform.scale(dan_life, (30, 30))
dan_spr = dan_spr_r




hud_img = pygame.image.load("g_assets/hud_3.jpg")
hud_img = pygame.transform.scale(hud_img, (s_width, s_height * 0.20))

item_gold = pygame.image.load("g_assets/coin.png")
item_gold = pygame.transform.scale(item_gold, (tile_size * 0.75, tile_size * 0.75))
gold_hud = pygame.transform.scale(item_gold, (30, 30))

item_water = pygame.image.load("g_assets/water.png")
item_water = pygame.transform.scale(item_water, (tile_size, tile_size))
hud_water = item_water
hud_water = pygame.transform.scale(hud_water, (60, 60))

item_hkit = pygame.image.load("g_assets/health_kit.png")
item_hkit = pygame.transform.scale(item_hkit, (tile_size, tile_size))
hud_hkit = item_hkit
hud_hkit = pygame.transform.scale(hud_hkit, (50, 50))

item_key = pygame.image.load("g_assets/key.png")
item_key = pygame.transform.scale(item_key, (50, 50))
hud_key = item_key
hud_key = pygame.transform.scale(hud_key, (80, 80))

axe_l = pygame.image.load("g_assets/pickaxe_l.png")
axe_r = pygame.image.load("g_assets/pickaxe_r.png")
axe_l = pygame.transform.scale(axe_l, (tile_size, tile_size))
axe_r = pygame.transform.scale(axe_r, (tile_size, tile_size))
item_axe = axe_r

menu_cursor = axe_r

hud_axe = axe_r
hud_axe = pygame.transform.scale(hud_axe, (60, 60))
prj_axe = axe_r

dyn_l = pygame.image.load("g_assets/dynamite_l.png")
dyn_l_held = pygame.image.load("g_assets/dynamite_l.png")
dyn_r = pygame.image.load("g_assets/dynamite_r.png")
dyn_r_held = dyn_r

dyn_l = pygame.transform.scale(dyn_l, (tile_size, tile_size))
dyn_r = pygame.transform.scale(dyn_r, (tile_size, tile_size))
dyn_r_held = pygame.transform.scale(dyn_r_held, (tile_size / 2, tile_size / 2))
dyn_l_held = pygame.transform.scale(dyn_l_held, (tile_size / 2, tile_size / 2))
item_dyn = dyn_r

hud_dyn = dyn_r
hud_dyn = pygame.transform.scale(hud_dyn, (60, 60))

w_lad = pygame.image.load("g_assets/ladder.png")
w_lad = pygame.transform.scale(w_lad, (tile_size, tile_size))

w_crate = pygame.image.load("g_assets/crate.png")
w_crate = pygame.transform.scale(w_crate, (tile_size, tile_size))

w_bldr = pygame.image.load("g_assets/boulder.png")
w_bldr = pygame.transform.scale(w_bldr, (tile_size, tile_size))


backg_pri = pygame.image.load("g_assets/Designer.jpeg")
backg_pri = pygame.transform.scale(backg_pri, (s_width, s_height))

menu_splash = pygame.image.load("g_assets/menu_splash_fin.png")
menu_splash = pygame.transform.scale(menu_splash, (s_width, s_height))


splash_text = menu_font.render("Press Any Key to Start", False, (142, 68, 85))
splash_rect = splash_text.get_rect(center=(s_width * 0.5, s_height * 0.75))


menu_options = pygame.image.load("g_assets/menu_options.jpg")
menu_options = pygame.transform.scale(menu_options, (s_width, s_height))

options_text = menu_font.render("Options Placeholder Text", False, (255, 255, 255))
options_rect = options_text.get_rect()

options_rect.x = s_width * 0.10
options_rect.y = s_height * 0.25

menu_main = pygame.image.load("g_assets/menu_main.jpg")
menu_main = pygame.transform.scale(menu_main, (s_width, s_height))

opts_menu = pygame.image.load("g_assets/menu_options.jpg")
opts_menu = pygame.transform.scale(opts_menu, (s_width, s_height))

s_opts_menu = pygame.image.load("g_assets/platform.jpg")
s_opts_menu = pygame.transform.scale(s_opts_menu, (s_width, s_height))

menu_cred = pygame.image.load("g_assets/menu_credits.jpg")
menu_cred = pygame.transform.scale(menu_cred, (s_width, s_height))



player_color = (87, 117, 103)
enemy_color = (253, 0, 0)

exit_hole = (45, 8, 11)



# Music & SFX Initialization Pool ----------------------------------------------


#pygame.mixer.music.load("music/something2.mp3")
#pygame.mixer.music.play(-1)





# Game Clock Initialized

game_clock = pygame.time.Clock()







# Class Creation Area ----------------------------------------------------------


class EnemyNPC:
    
    def __init__(self, x_pos, y_pos):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.npc_dir_x = 1
        self.npc_dir_y = None    # Implementation for Later Use 
        
        self.x_pos_next = None
        self.y_pos_next = None
        
        self.alive = True
        
    
    def draw(self, game_screen, enemy_color, tile_size):
        pygame.draw.rect(game_screen, enemy_color, (self.x_pos * tile_size - camera_x, self.y_pos * tile_size - camera_y, tile_size // 2, tile_size))
    
    
    
    def update(self, game_world):
        
        self.x_pos_next = self.x_pos + (0.25 * self.npc_dir_x)                     # Horizontal Movement -- Decimal used for speed multiplier per frame
        self.y_pos_next = self.y_pos + 1                                           # Used for "Gravity"
        
        vrt_chk = self.y_pos + 1                                                   # Used for checking for "Air"
        
        if game_world[int(self.y_pos)][int(self.x_pos_next)] in (1, 3):
            self.npc_dir_x = self.npc_dir_x * (-1)
        
        if game_world[int(vrt_chk)][int(self.x_pos_next + (self.npc_dir_x / 2))] == 0:
            self.npc_dir_x = self.npc_dir_x * (-1)
        
        if 0 <= self.y_pos < len(game_world) and 0 <= self.x_pos_next < len(game_world[0]):
            if game_world[int(self.y_pos)][int(self.x_pos_next)] in (0, 2, 4, 6, 7, 9, 11):
                
                self.x_pos = self.x_pos_next
        
        if 0 <= self.y_pos_next < len(game_world) and 0 <= self.x_pos < len(game_world[0]):
            if game_world[int(self.y_pos_next)][int(self.x_pos)] in (0, 2, 4, 6, 7, 9, 11):
                
                self.y_pos = self.y_pos_next
        
        self.y_pos_next += 1




class Crate:
    
    def __init__(self, x_pos, y_pos, w_crate):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.type = 'Crate'
        
        self.item_list = [2, 7, 9]
        
        self.item_rnd = random.randint(0, len(self.item_list) - 1)
        self.item_sel = self.item_list[self.item_rnd]
        
        self.broken = False
    
    def draw_crate(self):
        
        game_screen.blit(w_crate, (self.x_pos * tile_size - camera_x, self.y_pos * tile_size - camera_y))
        
    
    def update(self):
        
        if self.broken:
            
            game_world[self.y_pos][self.x_pos] = self.item_sel
              

class Boulder: 
    
    def __init__(self, x_pos, y_pos, w_bldr):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.type = 'Boulder'
        
        self.broken = False
    
    def draw_bldr(self):
        game_screen.blit(w_bldr, (self.x_pos * tile_size - camera_x, self.y_pos * tile_size - camera_y))
    
    def update(self):
        
        if self.broken:
            game_world[self.y_pos][self.x_pos] = 0
        





# Code building Area ----------------------------------------------------------#


# Boolean Pool

game_loop = True
splash = True
opts_on = False
running = False
credits = False


# Main Program Loop

while game_loop:
    
    # Splash Screen Loop
    
    if splash:
        
        while splash:
            
            game_clock.tick(10)
                    
            menu_screen.blit(menu_splash, (0, 0))
            menu_screen.blit(splash_text, splash_rect)    
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    menu_on = True
                    splash = False
            
            pygame.display.update() 
        
    
    # Main Menu Loop
        
    if menu_on:
        
        menu_list = ['New Game', 'Load Game', 'Options', 'Credits', 'Exit Game']
        menu_ind = 0
        
        while menu_on:
            
            menu_screen.blit(menu_main, (0, 0))
            
            # Main Menu Keyboard Handling
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    game_on = False
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        menu_ind = (menu_ind - 1) % len(menu_list)
                        
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        menu_ind = (menu_ind + 1) % len(menu_list)
                     
                    if event.key == pygame.K_RETURN:
                        
                        # New Game Initialization
                        
                        if menu_list[menu_ind] == 'New Game':
                            
                            
                            # Character Selection Loop
                            
                            map_ind = 0
                            player_data['Map Track'] = map_ind
                            
                            char_setup = True
                            while char_setup:
                                        
                                        
                                # Character Selection Menu Graphics Rendering
                                
                                menu_screen.blit(menu_main, (0, 0))
                                menu_screen.blit(dan_hud, (s_width * 0.10, s_height * 0.31))
                                menu_screen.blit(dave_hud, (s_width * 0.6, s_height * 0.3))
                                
                                char_txt = menu_font.render('Choose a Character', False, (55, 55, 55))
                                dan_txt = menu_font.render('Dan', False, (55, 55, 55))
                                dave_txt = menu_font.render('Dave', False, (55, 55, 55))
                                
                                char_rect = char_txt.get_rect()
                                dan_rect = dan_txt.get_rect()
                                dave_rect = dave_txt.get_rect()
                                
                                char_rect.x = s_width * 0.27
                                char_rect.y = s_height * 0.75
                                
                                dan_rect.x = s_width * 0.20
                                dan_rect.y = s_height * 0.25
                                
                                dave_rect.x = s_width * 0.70
                                dave_rect.y = s_height * 0.25
                                
                                danHud_rect = dan_hud.get_rect()
                                daveHud_rect = dave_hud.get_rect()
                            
                                menu_screen.blit(char_txt, char_rect)
                                menu_screen.blit(dan_txt, dan_rect)
                                menu_screen.blit(dave_txt, dave_rect)
                                
                                # Character Selection Screen Keyboard Handling
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        game_on = False
                                    
                                    if event.type == pygame.KEYDOWN:
                                        
                                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                            
                                            dan_hud = pygame.transform.scale(dan_hud, (305, 305))
                                            dave_hud = pygame.transform.scale(dave_hud, (260, 260))
                                            char_sel = 0
                                        
                                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                            
                                            dan_hud = pygame.transform.scale(dan_hud, (260, 260))
                                            dave_hud = pygame.transform.scale(dave_hud, (310, 310))
                                            char_sel = 1
                                        
                                        if event.key == pygame.K_RETURN:
                                            
                                            if char_sel == 0:
                                                player_data['Character'] = 'Dan'
                                            
                                            elif char_sel == 1:
                                                player_data['Character'] = 'Dave'
                                            
                                                
                                            char_setup = False
                                            menu_on = False
                                            running = False
                                            diff_screen = True
                                    
                                pygame.display.update()     
                            
                            # Difficulty Selection Loop
                            
                            diff_list = ['Easy', 'Medium', 'Hard']
                            diff_ind = 0
                            diff_sel = diff_list[diff_ind]
                            
                            while diff_screen:
                                
                                menu_screen.blit(menu_main, (0, 0))
                                
                                # Difficulty Selection Screen Keyboard Handling
                                
                                for event in pygame.event.get():
                                    
                                    if event.type == pygame.QUIT:
                                        game_on = False
                                    
                                    if event.type == pygame.KEYDOWN:
                                        
                                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                                            
                                            diff_ind = (diff_ind - 1) % len(diff_list)
                                            
                                            diff_sel = diff_list[diff_ind]
                                        
                                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                            
                                            diff_ind = (diff_ind + 1) % len(diff_list)
                                            
                                            diff_sel = diff_list[diff_ind]
                                        
                                        if event.key == pygame.K_RETURN:
                                            
                                            game_data['Diff'] = diff_sel
                                            
                                            map_list = ['map1', 'map2', 'map3']
                                            map_ind = 0
                                            
                                            game_world = load_map(game_data, map_ind, map_list)                                            
                                    
                                            diff_screen = False
                                            running = True
                                            
                                
                                # Difficulty Selection Screen Graphics Rendering
                                
                                diff_txt = menu_font.render('Choose Difficulty', False, (55, 55, 55))
                                diff_rect = diff_txt.get_rect()
                                
                                diff_rect.x = s_width * 0.3
                                diff_rect.y = s_height * 0.3                            
                                menu_screen.blit(diff_txt, diff_rect)
                                
                                menu_sp = 30
                                
                                for difficulty in diff_list:
                                    
                                    lvl_txt = menu_font.render(difficulty, False, (55, 55, 55))
                                    lvl_rect = lvl_txt.get_rect()
                                    
                                    lvl_rect.x = s_width * 0.4
                                    lvl_rect.y = s_height * 0.38 + menu_sp
                                    
                                    menu_screen.blit(lvl_txt, lvl_rect)
                                    
                                    if difficulty == diff_list[diff_ind]:
                                        menu_screen.blit(menu_cursor, (lvl_rect.x - 44, lvl_rect.y))                                    
                                    
                                    menu_sp += 50
                    
                                pygame.display.update()
                        
                        # Load Game Initialization
                        
                        elif menu_list[menu_ind] == 'Load Game':
                            game_world, player_data = load_game()
                            map_ind = player_data['Map Track']
                            map_list = ['map1', 'map2', 'map3']
                            menu_on = False
                            running = True
                        
                        # Options Screen Switch
                        
                        elif menu_list[menu_ind] == 'Options':
                            opts_on = True
                            menu_on = False
                        
                        # Credits Screen Switch
                        
                        elif menu_list[menu_ind] == 'Credits':
                            credits = True
                            menu_on = False
                        
                        # Close the Program
                        
                        elif menu_list[menu_ind] == 'Exit Game':
                            menu_on = False
                            running = False
                            splash = False
                    
            # Main Menu Rendering
            menu_sp = 30
            for menu_sel in menu_list:
                
                main_text = menu_font.render(menu_sel, False, (55, 55, 55))
                main_rect = main_text.get_rect()
                
                main_rect.x = s_width * 0.10
                main_rect.y = s_height * 0.33 + menu_sp       
                
                menu_screen.blit(main_text, main_rect)
                
                if menu_sel == menu_list[menu_ind]:
                    menu_screen.blit(menu_cursor, (main_rect.x - 44, main_rect.y))
                
                menu_sp += 50
            
        
            pygame.display.update()
            
            
            
            
    # Options Menu Screen
    if opts_on:
        
        opts_list = ['Game Options', 'Video Options', 'Sound Options', 'Go Back']
        opts_ind = 0
        s_opts_ind = 0
        
        while opts_on:
            
            menu_screen.blit(menu_options, (0, 0))
            
            
            # Options Menu Keyboard Handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    opts_on = False
                    
                
                if event.type == pygame.KEYDOWN:
                        
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        opts_ind = (opts_ind - 1) % len(opts_list)
                        
                            
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        opts_ind = (opts_ind + 1) % len(opts_list)
                        
                        
                    if event.key == pygame.K_RETURN:
                        
                        
                        
                        # Game Options Screen
                        
                        if opts_list[opts_ind] == 'Game Options':
                            
                            game_opts = True
                            g_opts = ['Game Difficulty', 'Go Back']
                            g_opts_ind = 0
                            
                            while game_opts:
                                
                                menu_screen.blit(s_opts_menu, (0, 0))
                                
                                
                                # GAME Options Screen Keyboard Input Capture
                                for event in pygame.event.get():
                                    
                                    if event.type == pygame.QUIT:
                                        game_on = False
                                    
                                    if event.type == pygame.KEYDOWN:
                                        
                                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                                            menu_ind = (g_opts_ind - 1) % len(g_opts)
                                            
                                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                            g_opts_ind = (g_opts_ind + 1) % len(g_opts)
                                         
                                        if event.key == pygame.K_RETURN:
                                            
                                            # Changing Difficulty in Menu
                                            if g_opts[g_opts_ind] == 'Game Difficulty':
                                                
                                                diffs = ['Easy', 'Normal', 'Hard']
                                                
                                                curr_diff = game_data['Diff']
                                                
                                                diff_ind = diffs.index(curr_diff)
                                                
                                                
                                                if diff_ind + 1 > len(diffs):
                                                
                                                    diff_ind = 0
                                                    next_diff = diffs[diff_ind]
                                                
                                                else:
                                                    next_diff = diffs[(diff_ind + 1) % len(diffs)]
                                                    
                                                
                                                game_data['Diff'] = next_diff
                                                
                                            
                                            # Returning to Previous Menu
                                            
                                            elif g_opts[g_opts_ind] == 'Go Back':
                                                
                                                game_opts = False
                                                
                                                
                                                
                                            
                                # Render / Printing GAME Options Screen
                                menu_sp = 30
                                for option in g_opts:
                                    
                                    if option == 'Game Difficulty':
                                        opt_text = menu_font.render(option + ':' + "   " + game_data['Diff'], False, (255, 255, 255))
                                    
                                    elif option == 'Go Back':
                                        opt_text = menu_font.render(option, False, (255, 255, 255))
                                    
                                    
                                    opt_rect = opt_text.get_rect()
                                    
                                    opt_rect.x = s_width * 0.25
                                    opt_rect.y = s_height * 0.50 + menu_sp       
                                    
                                    menu_screen.blit(opt_text, opt_rect)
                                    
                                    if option == g_opts[g_opts_ind]:
                                        menu_screen.blit(menu_cursor, (opt_rect.x - 44, opt_rect.y))
                                    
                                    menu_sp += 50                                    
                                
                                pygame.display.update()
                            
                           
                           

                        # Video Options Screen
                        
                        elif opts_list[opts_ind] == 'Video Options':
                            
                            vid_opts = True
                            
                            v_opts = ['Screen Resolution', 'Tile Size', 'Go Back']
                            v_opts_ind = 0
                            
                            while vid_opts:
                                
                                menu_screen.blit(s_opts_menu, (0, 0))
                                
                                
                                # Video Options Screen Keyboard Input Capture
                                for event in pygame.event.get():
                                    
                                    if event.type == pygame.QUIT:
                                        game_on = False
                                    
                                    if event.type == pygame.KEYDOWN:
                                        
                                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                                            v_opts_ind = (v_opts_ind - 1) % len(v_opts)
                                            
                                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                            v_opts_ind = (v_opts_ind + 1) % len(v_opts)
                                         
                                        if event.key == pygame.K_RETURN:
                                            
                                            # Changing Resolution in Video Options Menu
                                            if v_opts[v_opts_ind] == 'Screen Resolution':
                                                
                                                res_list = [(640, 480), (800, 600), (1024, 768)]
                                                
                                                curr_res = game_data['Video']['Resolution']
                                                
                                                res_ind = res_list.index(curr_res)
                                                
                                                
                                                if res_ind + 1 > len(res_list):
                                                
                                                    res_ind = 0
                                                    next_res = res_list[res_ind]
                                                
                                                else:
                                                    next_res = res_list[(res_ind + 1) % len(res_list)]
                                                    
                                                
                                                game_data['Video']['Resolution'] = next_res
                                                
                                                s_width = next_res[0]
                                                s_height = next_res[1]
                                                
                                                
                                            # Return to Previous Menu
                                            
                                            elif v_opts[v_opts_ind] == 'Go Back':
                                                
                                                vid_opts = False
                                                
                                                
                                                
                                            
                                # Render / Printing GAME Options Screen
                                menu_sp = 30
                                for option in v_opts:
                                    
                                    if option == 'Screen Resolution':
                                        opt_text = menu_font.render(option + ':' + "   " + str(game_data['Video']['Resolution']), False, (255, 255, 255))
                                    
                                    elif option == 'Tile Size':
                                        opt_text = menu_font.render(option + ':' + "   " + str(game_data['Video']['Tile Size']), False, (255, 255, 255))
                                    
                                    else:
                                        opt_text = menu_font.render(option, False, (255, 255, 255))
                                    
                                    
                                    opt_rect = opt_text.get_rect()
                                    
                                    opt_rect.x = s_width * 0.20
                                    opt_rect.y = s_height * 0.40 + menu_sp       
                                    
                                    menu_screen.blit(opt_text, opt_rect)
                                    
                                    if option == v_opts[v_opts_ind]:
                                        menu_screen.blit(menu_cursor, (opt_rect.x - 44, opt_rect.y))
                                    
                                    menu_sp += 50                                    
                                
                                pygame.display.update()
                            
                        
                        
                        # Sound Options Screen
                        elif opts_list[opts_ind] == 'Sound Options':
                            print("Sound Options...")
                        
                        
                        
                        # Return
                        elif opts_list[opts_ind] == 'Go Back':
                            opts_on = False
                            menu_on = True
                            
                            
                            
            
            # Options Menu Rendering               
            menu_sp = 30
            for opt_sel in opts_list:
                        
                main_text = menu_font.render(opt_sel, False, (255, 255, 255))
                main_rect = main_text.get_rect()
                        
                main_rect.x = s_width * 0.33
                main_rect.y = s_height * 0.33 + menu_sp       
                        
                menu_screen.blit(main_text, main_rect)
                        
                if opt_sel == opts_list[opts_ind]:
                    menu_screen.blit(menu_cursor, (main_rect.x - 44, main_rect.y))
                
                    
                menu_sp += 50    
            
            pygame.display.update()
            
    
    # Credits Screen      
    if credits:
        
        menu_screen.blit(menu_cred, (0, 0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_on = False
            
            if event.type == pygame.KEYDOWN:
                credits = False
                menu_on = True
        
        
        
        pygame.display.update()
        
            
    # Gameplay Code          
    if running: 
        
        player_Locx, player_Locy, player_newLocx, player_newLocy, player_Dirx, player_Diry = player_init(player_data)
        player_yVel = 0
        cooldown = 0
        
        anim_index = 0
        anim_timer = 0
        anim_speed = 5  # Adjust as needed for speed; 5 works well for 15 FPS        
        
        if player_data['Character'] == 'Dan':
            sprite = dan_spr_r
            spr_list = [dan_spr_r, dan_spr_rw]
        
        elif player_data['Character'] == 'Dave':
            sprite = dave_spr_r
            spr_list = [dave_spr_r, dave_spr_rw, dave_spr_l, dave_spr_lw]
            
        while running:
            
            game_clock.tick(15)
            
            game_screen.blit(backg_pri, (0,0))
            
            # Check for Player Quitting the Game
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Check Health for Game Over
            
            if player_data['Health'] <= 0:
                print("GAME OVER!")
                running = False
            
            # Player Key Input Handling Area
            
            key_in = pygame.key.get_pressed()
            
            if key_in[pygame.K_w]:
             
                if game_world[int(player_Locy)][int(player_newLocx)] == 11:
                    player_newLocy = player_Locy - 0.5
                    
            
            if key_in[pygame.K_a]:
                
                player_newLocx = player_Locx - 0.5
                
                if player_data['Character'] == 'Dan':
                    
                    for anim in spr_list:
                        
                        if anim == dan_spr_l:
                            sprite = dan_spr_l
                        
                        elif anim == dan_spr_lw:
                            sprite = dan_spr_lw
                
                elif player_data['Character'] == 'Dave':
                    
                    for anim in spr_list:
                        
                        if anim == dave_spr_l:
                            sprite = dave_spr_l
                        
                        elif anim == dave_spr_lw:
                            sprite = dave_spr_lw
                            
                
                
                player_Dirx = -1
                
                if player_data['Curr_Item'] == 'Pickaxe':
                    item_axe = axe_l
                
                if player_data['Curr_Item'] == 'Dynamite':
                    item_dyn = dyn_l_held
                    
            
            if key_in[pygame.K_s]:
               
                pass
            
            if key_in[pygame.K_d]:
                
                player_newLocx = player_Locx + 0.5
                
                if player_data['Character'] == 'Dan':
                    
                    for anim in spr_list:
                        
                        if anim == dan_spr_r:
                            sprite = dan_spr_r
                        
                        elif anim == dan_spr_rw:
                            sprite = dan_spr_rw                    
                
                elif player_data['Character'] == 'Dave':
                    
                    for anim in spr_list:
                        
                        if anim == dave_spr_r:
                            sprite = dave_spr_r
                        
                        elif anim == dave_spr_rw:
                            sprite = dave_spr_rw                    
                
                player_Dirx = 1
                
                
                if player_data['Curr_Item'] == 'Pickaxe':
                    item_axe = axe_r
                
                if player_data['Curr_Item'] == 'Dynamite':
                    item_dyn = dyn_r_held
              
              
                
            # JUMP! 
            
            if key_in[pygame.K_SPACE]:
                
                gnd_chk = game_world[int(player_Locy + 1)][int(player_Locx)]
                
                if 0 <= gnd_chk < len(game_world) and 0 <= player_Locx < len(game_world[0]):
                    
                    if gnd_chk == 1:
                        
                        player_data['On Ground'] = True
                        player_newLocy = int(player_newLocy)
                        
                    
                    else:
                        player_data['On Ground'] = False
                    
                    if player_data['On Ground']:
                        
                        player_yVel = 4
                        
                        for i in range(1, 5):
                            
                            jp_chk = game_world[int(player_Locy - i)][int(player_Locx)]
                            
                            if jp_chk != 0:
                                player_yVel = i - 1
                                break
                               
                        
                        player_newLocy -= player_yVel
           
            
            # ATTACK & USE --- Throw & Action
            
            if key_in[pygame.K_RETURN]:
                
                if player_data['Curr_Item'] in ('Pickaxe', 'Dynamite'):
                    item_throw(player_data, game_world)
                
                elif player_data['Curr_Item'] in ('Water', 'h_kit'):
                    msg_box, msg_rect, msg_timer = item_use(player_data)
                
                elif game_world[int(player_Locy)][int(player_Dirx * (player_Locx + 1))] == 3:
                    
                    if 'Key' in player_data['Items']:
                        
                        npc_list = []
                        prj_list = []
                        
                        map_ind += 1
                        game_world = load_map(game_data, map_ind, map_list)
                    
                    else:
                        print("You Need the Key to Open this Door")
                        
            
            # Pause Screen
            
            if key_in[pygame.K_ESCAPE]:
                
                pause = True
                p_ind = 0
                while pause:
                    
                    p_list = ['Resume Game', 'Save Game', 'Load Game', 'Options', 'Quit']
                    
                    
                    pause_hud = pygame.transform.scale(hud_img, (s_width, s_height))
                    
                    menu_screen.blit(pause_hud, (0, 0))
                    
                    for event in pygame.event.get():
                        
                        if event.type == pygame.QUIT:
                            game_on = False
                        
                        if event.type == pygame.KEYDOWN:
                            
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                p_ind = (p_ind - 1) % len(p_list)
                            
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                p_ind = (p_ind + 1) % len(p_list)
                                
                            if event.key == pygame.K_RETURN:
                                
                                if p_list[p_ind] == 'Resume Game':
                                    pause = False
                                
                                if p_list[p_ind] == 'Save Game':
                                    save_game(player_data, game_world, npc_list)
                                
                                if p_list[p_ind] == 'Load Game':
                                    game_world, player_data = load_game()
                                
                                if p_list[p_ind] == 'Options':
                                    pass
                                
                                if p_list[p_ind] == 'Quit':
                                    
                                    running = False
                                    pause = False
                                    menu_on = True
                    
                    
                    # Rendering the Pause Screen
                    menu_sp = 30
                    for p_opt in p_list:
                        
                        pause_text = menu_font.render(p_opt, False, (255, 255, 255))
                        pause_rect = pause_text.get_rect()
                        
                        pause_rect.x = s_width * 0.33
                        pause_rect.y = s_height * 0.33 + menu_sp
                        
                        menu_screen.blit(pause_text, pause_rect)
                        
                        if p_opt == p_list[p_ind]:
                            menu_screen.blit(menu_cursor, (pause_rect.x - 44, pause_rect.y))
                        
                        menu_sp += 50
                    
                    pygame.display.update()
    
            
            # Previous Item in Inventory
            if key_in[pygame.K_LEFT]:
                
                if len(player_data['Items']) == 0:
                    pass
                
                else:
                    curr_item = player_data['Curr_Item']
                    item_ind = player_data['Items'].index(curr_item)
                    
                    if item_ind - 1 < 0:
                        item_ind = len(player_data['Items'])
                        
                    player_data['Curr_Item'] = player_data['Items'][item_ind - 1]
                    
            
            # Next Item in Inventory
            if key_in[pygame.K_RIGHT]:
                
                if len(player_data['Items']) == 0:
                    pass
                
                else:
                    curr_item = player_data['Curr_Item']
                    item_ind = player_data['Items'].index(curr_item)
                    
                    if item_ind + 1 >= len(player_data['Items']):
                        item_ind = -1
                    
                    player_data['Curr_Item'] = player_data['Items'][item_ind + 1]
                    
                    
                    
            # Collision Checking & New Value Acceptance/Rejection
            
            if 0 <= int(player_Locy) < len(game_world) and 0 <= int(player_newLocx) < len(game_world[0]):
                
                if game_world[int(player_Locy)][int(player_newLocx)] in (0, 2, 4, 6, 7, 8, 9, 11) and game_world[int(player_Locy - 1)][int(player_newLocx)] in (0, 2, 4, 6, 7, 8, 9, 11):
                    
                    player_Locx = player_newLocx
                    
                    if game_world[int(player_Locy)][int(player_newLocx)] in (2, 4, 6, 7, 8, 9):
                        
                        if game_world[int(player_Locy)][int(player_newLocx)] == 2:
                            
                            player_data['Score'] += 250 
                            
                            if player_data['Coins'] + 1 == 100:
                                
                                player_data['Lives'] += 1
                                player_data['Coins'] = 0
                            
                            else:
                                player_data['Coins'] += 1
                            
                            msg_box = font2.render("You picked up a Gold Coin!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30
                        
                        
                        elif game_world[int(player_Locy)][int(player_newLocx)] == 4 or game_world[int(player_Locy - 1)][int(player_newLocx)] == 4:
                            
                            player_data['Items'].append('Key')
                            player_data['Score'] += 100
                            
                            msg_box = font2.render("You picked up a Key!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_Locy)][int(player_newLocx)] == 6 or game_world[int(player_Locy - 1)][int(player_newLocx)] == 6:
                            
                            player_data['Items'].append('Pickaxe')
                            player_data['Curr_Item'] = 'Pickaxe'
                            
                            msg_box = font2.render("You got a Pickaxe!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_Locy)][int(player_newLocx)] == 7 or game_world[int(player_Locy - 1)][int(player_newLocx)] == 7:
                            
                            if player_data['Health'] < 7:
                                
                                if player_data['Health'] + 1 > 7:
                                    player_data['Health'] = 7
                                    msg_box = font2.render("You got some Water! - +1 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                                
                                else:
                                    player_data['Health'] += 1
                                    msg_box = font2.render("You got some Water! - +1 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                            
                            else:
                                
                                player_data['Items'].append('Water')
                                player_data['Curr_Item'] = 'Water'
                                msg_box = font2.render("You picked up some Water!", False, (255, 255, 255))
                                msg_rect = msg_box.get_rect()
                            
                                msg_rect.x = (s_width * 0.025)
                                msg_rect.y = (s_height * 0.025)   
                            
                                msg_timer = 30
                                
                                
                        elif game_world[int(player_Locy)][int(player_newLocx)] == 8 or game_world[int(player_Locy - 1)][int(player_newLocx)] == 8:
                            
                            player_data['Items'].append('Dynamite') 
                            player_data['Curr_Item'] = 'Dynamite'
                            
                            msg_box = font2.render("You picked up Dynamite!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_Locy)][int(player_newLocx)] == 9 or game_world[int(player_Locy - 1)][int(player_newLocx)] == 9:
                            
                            if player_data['Health'] < 7:
                                
                                if player_data['Health'] + 3 > 7:
                                    player_data['Health'] = 7
                                    msg_box = font2.render("You got a First Aid Kit! - +3 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                                
                                else:
                                    player_data['Health'] += 3
                                    msg_box = font2.render("You got a First Aid Kit - +3 HP!", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                            
                            else:
                                player_data['Items'].append('h_kit')
                                player_data['Curr_Item'] = 'h_kit'
                                msg_box = font2.render("You picked up a First Aid Kid!", False, (255, 255, 255))
                                msg_rect = msg_box.get_rect()
                            
                                msg_rect.x = (s_width * 0.025)
                                msg_rect.y = (s_height * 0.025)   
                            
                                msg_timer = 30                        
                            
                        
                        
                        
                        game_world[int(player_Locy)][int(player_newLocx)] = 0
                        
            
            # Check if next Y position is within bounds
            
            if 0 <= int(player_newLocy) < len(game_world) and 0 <= int(player_Locx) < len(game_world[0]):
                
                if game_world[int(player_newLocy)][int(player_Locx)] in (0, 2, 4, 6, 7, 8, 9, 11) and game_world[int(player_newLocy - 1)][int(player_Locx)] in (0, 2, 4, 6, 7, 8, 9, 11):
                    
                    player_Locy = player_newLocy
                    
                    if game_world[int(player_newLocy)][int(player_Locx)] in (2, 4, 6, 7, 8, 9) or game_world[int(player_newLocy - 1)][int(player_Locx)] in (2, 4, 6, 7, 8, 9):
                        
                        if game_world[int(player_newLocy)][int(player_Locx)] == 2 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 2:
                            
                            player_data['Score'] += 250
                            
                            if player_data['Coins'] + 1 == 100:
                                
                                player_data['Lives'] += 1
                                player_data['Coins'] = 0
                            
                            else:
                                
                                player_data['Coins'] += 1
                            
                            msg_box = font2.render("You picked up a Gold Coin!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect() 
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                   
                        
                        elif game_world[int(player_newLocy)][int(player_Locx)] == 4 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 4:
                            
                            player_data['Items'].append('Key')
                            player_data['Score'] += 100
                            
                            msg_box = font2.render("You picked up a Key!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_newLocy)][int(player_Locx)] == 6 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 6:
                            
                            player_data['Items'].append('Pickaxe')
                            player_data['Curr_Item'] = 'Pickaxe'
                            
                            msg_box = font2.render("You got a Pickaxe!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_newLocy)][int(player_Locx)] == 7 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 7:
                            
                            if player_data['Health'] < 7:
                                
                                if player_data['Health'] + 1 > 7:
                                    player_data['Health'] = 7
                                    msg_box = font2.render("You got some Water! - +1 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                                
                                else:
                                    player_data['Health'] += 1
                                    msg_box = font2.render("You got some Water! - +1 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                            
                            else:
                                player_data['Items'].append('Water')   
                                player_data['Curr_Item'] = 'Water'
                                msg_box = font2.render("You picked up some Water!", False, (255, 255, 255))
                                msg_rect = msg_box.get_rect()
                            
                                msg_rect.x = (s_width * 0.025)
                                msg_rect.y = (s_height * 0.025)   
                            
                                msg_timer = 30                        
                        
                        elif game_world[int(player_newLocy)][int(player_Locx)] == 8 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 8:
                            player_data['Items'].append('Dynamite')
                            player_data['Curr_Item'] = 'Dynamite'
                            msg_box = font2.render("You picked up Dynamite!", False, (255, 255, 255))
                            msg_rect = msg_box.get_rect()
                            
                            msg_rect.x = (s_width * 0.025)
                            msg_rect.y = (s_height * 0.025)   
                            
                            msg_timer = 30                    
                        
                        elif game_world[int(player_newLocy)][int(player_Locx)] == 9 or game_world[int(player_newLocy - 1)][int(player_Locx)] == 9:
                            
                            if player_data['Health'] < 7:
                                
                                if player_data['Health'] + 3 > 7:
                                    player_data['Health'] = 7
                                    msg_box = font2.render("You picked up a First Aid Kit! - +3 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                                
                                else:
                                    player_data['Health'] += 3   
                                    msg_box = font2.render("You picked up a First Aid Kit! - +3 HP", False, (255, 255, 255))
                                    msg_rect = msg_box.get_rect()
                            
                                    msg_rect.x = (s_width * 0.025)
                                    msg_rect.y = (s_height * 0.025)   
                            
                                    msg_timer = 30                            
                            
                            else:
                                player_data['Items'].append('h_kit')   
                                player_data['Curr_Item'] = 'h_kit'
                                msg_box = font2.render("You picked up a First Aid Kit!", False, (255, 255, 255))
                                msg_rect = msg_box.get_rect()
                            
                                msg_rect.x = (s_width * 0.025)
                                msg_rect.y = (s_height * 0.025)   
                            
                                msg_timer = 30                       
                        
                        
                        game_world[int(player_newLocy)][int(player_Locx)] = 0
                        game_world[int(player_newLocy - 1)][int(player_Locx)] = 0
                    
                
                else:
                    player_newLocy = player_Locy
            
            if not player_data['On Ground']:
                player_yVel += 0.025
            
            player_newLocy = int(player_newLocy)
            player_newLocy += 1
            
            camera_x = player_Locx * tile_size - (s_width // 2)
            camera_y = player_Locy * tile_size - (s_height // 2)  
            
            play_pixel_x = (player_Locx * tile_size) - camera_x
            play_pixel_y = (player_Locy * tile_size) - camera_y
            play_pixel_y -= (dave_spr.get_height() - tile_size)
            
            # Graphic Rendering Area ------------------------------------------
            
            for row_ind in range(len(game_world)):
                for tile_ind in range(len(game_world[row_ind])):
                    
                    
                    if game_world[row_ind][tile_ind] == '#':
                        player_Locx == tile_ind
                        player_Locy == row_ind
                        player_data['Spawn'] = (player_Locx, player_Locy)
                        
                        game_world[row_ind][tile_ind] = 0
                    
                    if game_world[row_ind][tile_ind] == 1:
             
                        game_screen.blit(border, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 2:
                        game_screen.blit(item_gold, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                        
                    
                    if game_world[row_ind][tile_ind] == 3:
                        pygame.draw.rect(game_screen, exit_hole, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y, tile_size, tile_size))
                        
                    if game_world[row_ind][tile_ind] == 4:
                        game_screen.blit(item_key, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    
                    if game_world[row_ind][tile_ind] == 5:
                        
                        monster = EnemyNPC(tile_ind, row_ind)
                        npc_list.append(monster)
                        game_world[row_ind][tile_ind] = 0
                        
                    if game_world[row_ind][tile_ind] == 6:
                        game_screen.blit(item_axe, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 7:
                        game_screen.blit(item_water, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 8:
                        game_screen.blit(item_dyn, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 9:
                        game_screen.blit(item_hkit, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 11:
                        game_screen.blit(w_lad, (tile_ind * tile_size - camera_x, row_ind * tile_size - camera_y))
                    
                    if game_world[row_ind][tile_ind] == 12:
                        
                        prop_rock = Boulder(tile_ind, row_ind, w_bldr)
                        witem_list.append(prop_rock)
                    
                    if game_world[row_ind][tile_ind] == 13:
                        
                        rng_crate = Crate(tile_ind, row_ind, w_crate)
                        witem_list.append(rng_crate)
                        
                        
                    
                    
            anim_timer += 1
            if anim_timer >= anim_speed:
                
                if player_Dirx > 0:
                    sprite = dave_spr_r
                
                else:
                    sprite = dave_spr_l
                
                anim_timer = 0            
         
            game_screen.blit(sprite, (((s_width // 2) - tile_size, (s_height // 2) - tile_size)))   
            
            if cooldown > 0:
                cooldown -= 1
                
            for enemy in npc_list:
                
                if not enemy.alive:
                    npc_list.remove(enemy)
                    continue
                
                if round(player_Locx) == round(enemy.x_pos) and round(player_Locy) == round(enemy.y_pos):

                    if cooldown == 0:
                        player_data['Health'] -= 1
                        cooldown = 15        
                
                enemy.update(game_world)
                enemy.draw(game_screen, enemy_color, tile_size)
            
            
            for prj in prj_list:
                
                prj.update_prj(game_world, npc_list)
                
                if not prj.active:
                    prj_list.remove(prj)
                
                prj.draw_prj(game_world)    
            
            
            
            for w_item in witem_list:
                
                w_item.update()
                
                if w_item.broken:
                    witem_list.remove(w_item)
                
                if w_item.type == 'Crate':
                    w_item.draw_crate()
                
                if w_item.type == 'Boulder':
                    w_item.draw_bldr()

                
                
            
                    
            game_screen.blit(hud_img, (0, int(s_height - (int(s_height * 0.20))))) # This one draws the HUD
            
        
            h_bar_x = (s_width - (int(s_width * 0.91))) 
            h_bar_y = s_height - (int(s_height * 0.122)) 
            
            for h_bar in range(player_data['Health']):
        
                h_bar_x += 20
                pygame.draw.rect(game_screen, (250, 80, 0), (h_bar_x, h_bar_y, 16, 32))    
            
            
            text_surface = font.render("Health", False, (255, 255, 255))
            text_rect = text_surface.get_rect()
            
            item_txt = font.render("Item", False, (255, 255, 255))
            item_rect = item_txt.get_rect()
            
            coin_txt = font2.render(str(player_data['Coins']), False, (255, 255, 255))
            coin_rect = coin_txt.get_rect()
            
            life_txt = font2.render(str(player_data['Lives']), False, (255, 255, 255))
            life_rect = life_txt.get_rect()
            
            key_txt = font.render("Key", False, (255, 255, 255))
            key_rect = key_txt.get_rect()
            
            score_txt = font.render("Score", False, (255, 255, 255))
            score_val = player_data['Score']
            score_val = str(score_val)
            value_txt = font.render(score_val, False, (255, 255, 255))
            
            score_rect = score_txt.get_rect()
            value_rect = value_txt.get_rect()
            
            
            x_temp = 1.10
            h_bar_ysub = 6.5
            
            text_rect.x = s_width - (int(s_width * 0.85))
            text_rect.y = s_height - (int(s_height * 0.165))
            
            score_rect.x = (s_width - int(s_width * 0.21))
            score_rect.y = (s_height - int(s_height * 0.165))
            
            value_rect.x = (s_width - int(s_width * 0.19))
            value_rect.y = (s_height - int(s_height * 0.11))
            
            item_rect.x = (s_width - int(s_width * 0.43))
            item_rect.y = (s_height - int(s_height * 0.165))
            
            key_rect.x = (s_width - int(s_width * 0.60))
            key_rect.y = (s_height - int(s_height * 0.165))
            
            coin_rect.x = s_width * 0.5
            coin_rect.y = s_height * 0.025
            
            life_rect.x = s_width * 0.5
            life_rect.y = s_height * 0.03
            
            game_screen.blit(text_surface, text_rect)
            game_screen.blit(score_txt, score_rect)
            game_screen.blit(value_txt, value_rect)
            game_screen.blit(item_txt, item_rect)
            game_screen.blit(key_txt, key_rect)
            game_screen.blit(coin_txt, coin_rect)
            game_screen.blit(gold_hud, (s_width * 0.5 - 40, s_height * 0.020))
            
            if player_data['Character'] == 'Dan':
                game_screen.blit(dan_life, (s_width * 0.5 - 40, s_height * 0.066))
                game_screen.blit(life_txt, (s_width * 0.5, s_height * 0.066))
            
            elif player_data['Character'] == 'Dave':
                game_screen.blit(dave_life, (s_width * 0.5 - 40, s_height * 0.066))
                game_screen.blit(life_txt, (s_width * 0.5, s_height * 0.066))
            
            if msg_timer > 0:
                game_screen.blit(msg_box, msg_rect)
                msg_timer -= 1
            
            
            if 'Key' in player_data['Items']:
                game_screen.blit(hud_key, ((s_width - (int(s_width * 0.625)), (s_height - int(s_height * 0.14)))))
                
            
            if player_data['Curr_Item'] == 'Pickaxe':
                
                game_screen.blit(hud_axe, ((s_width - (int(s_width * 0.445)), (s_height - int(s_height * 0.13)))))
                
                if item_axe == axe_r:
                    game_screen.blit(item_axe, (((s_width // 2), (s_height // 2) - (tile_size // 2))))
                
                if item_axe == axe_l:
                    game_screen.blit(item_axe, (((s_width // 2) - tile_size, (s_height // 2) - (tile_size // 2))))
                    
                    
            
            if player_data['Curr_Item'] == 'Dynamite':
                game_screen.blit(hud_dyn, ((s_width - (int(s_width * 0.445)), (s_height - int(s_height * 0.13)))))
                
                
                if item_dyn == dyn_r_held:
                    game_screen.blit(item_dyn, (((s_width // 2), (s_height // 2))))
                
                if item_dyn == dyn_l_held:
                    game_screen.blit(item_dyn, (((s_width // 2) - (tile_size // 2), (s_height // 2))))
                    
            
            if player_data['Curr_Item'] == 'Water':
                game_screen.blit(hud_water, ((s_width - (int(s_width * 0.445)), (s_height - int(s_height * 0.13)))))
            
            if player_data['Curr_Item'] == 'h_kit':
                game_screen.blit(hud_hkit, ((s_width - (int(s_width * 0.445)), (s_height - int(s_height * 0.13)))))
                    
            
            
                
                    
            pygame.display.flip()
            
            
            

# End
