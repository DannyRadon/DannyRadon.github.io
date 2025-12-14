#-------------------------------------------------------------------------------
# Name: Danny Radon
# Course: CMPT 103 - AS02
# Work: Project - Message Encipher/Decipher Program
# 
# Academic Integrity Pledge: I, Danny Radon, hereby pledge that the work done 
#                          in this midterm is that of my own and no one else's.
#                                                       D.R.
#-------------------------------------------------------------------------------

# Table Creation Function

def build_table():

    tabula_rect = []
    
    tabula_rect.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alpha_line = tabula_rect[0]
    
    while alpha_line[0] != "Z":
        alpha_line = alpha_line[1:] + alpha_line[0]
        tabula_rect.append(alpha_line)
    
    table = tabula_rect
    
    return table


# Message Encipher Function

def encipher(table, message, key):
   
    table = build_table()
    
    alpha_line = table[0]
    
    ciph_chars = []    

    message = message.upper()
    
    for space in message:
        message = message.replace(" ", "")    
    
    message = list(message)
    
    key = key.upper()
    key = list(key)
    
    msg_length = len(message)
    key_length = len(key)
    
    if key_length is not msg_length:
        
        for char in range(len(message) - key_length):
            key.append(key[char % key_length]) 
   
    for pos in range(len(message)):
        
        ciph_col = message[pos]
        ciph_row = key[pos]
        
        ciph_col_pos = alpha_line.find(ciph_col)
        ciph_row_pos = alpha_line.find(ciph_row)
        
        ciph_char_row = table[ciph_row_pos]
        cipher_char = ciph_char_row[ciph_col_pos]
        
        ciph_chars.append(cipher_char)
        
    message = "".join(message)
    key = "".join(key)
    cipher = "".join(ciph_chars)
    
    print("\nYour Message: ", message)
    print("Your New Cipher:  ", cipher)
    
    return key, cipher


# Message Decipher Function

def decipher(table, key, cipher):
    
    key = key.upper()
    key = list(key)
    
    cipher = cipher.upper()
    
    table = build_table()
    alpha_line = table[0]
    
    key_length = len(key)
    ciph_length = len(cipher)
    
    cipher = list(cipher)
    
    dciph_chars_list = []
    
    if key_length is not ciph_length:
        
        for char in range(len(cipher) - key_length):
            key.append(key[char % key_length])     
    
    for pos in range(len(cipher)):
        
        dciph_col = cipher[pos]
        dciph_row = key[pos]
        
        dciph_row_pos = alpha_line.index(dciph_row)
        dciph_char_row = table[dciph_row_pos]
        
        dciph_char_pos = dciph_char_row.find(dciph_col)
        
        dciph_char = alpha_line[dciph_char_pos]
        dciph_chars_list.append(dciph_char)
        
    decipher = "".join(dciph_chars_list)
    
    print("\nDeciphered: ", decipher, sep = "")
    
    return decipher

table = build_table()

loop = True
while loop:

    print("\nEncipher Message or Decipher Message?")
    print("1.) Encipher")
    print("2.) Decipher")
    print("3.) Exit Program")

    user_in = int(input("\nPlease Make a Selection from the Menu: "))
    while user_in not in [1, 2, 3]:
        user_in = int(input("Invalid Selection. Please Choose from the Menu: "))

    key_in = None
    cipher = None
    if user_in == 1:

        msg_in = input("Enter Your Message: ")
        key_in = input("Enter Your Key: ")

        key, cipher = encipher(table, msg_in, key_in)

    elif user_in == 2:

        if key_in or cipher is None:
            print("Error! You Do Not Have a Key or Cipher!")
        
        else:
            msg_out = decipher(table, key_in, cipher)

    else: 
        break



