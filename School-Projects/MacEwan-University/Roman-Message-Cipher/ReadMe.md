The Roman Cipher (Encryption/Decryption) Program. This program will take in a message given by the user, encipher that message with a code and a key. That message can then be deciphered with the same key to be read on the other end of communication/transmission.

Program Information:

The Program Contains 3 main functions used to efficiently operate the logic.

1.) build_table() - This constructs the "Tabula Recta" used for Enciphering/Deciphering Communicated Messages
2.) encipher(table, message, key) - Uses the Tabula Recta to Encrypt a Message given by the User as well as a Key given by the user
3.) decipher(cipher, key) - Uses the Table and the Generated Cipher with User-Key to Decrypt/Decode the Ciphered Message into the Original

**How to Use**

The procedure to use this program starts with initializing Python and Importing all components from ciph_main.py:
>>> python
>>> from ciph_main import *

The program will load into the Menu and you may choose to Encipher a Message or Decipher a message. 
NOTE: You may only Decipher a message if you possess a Cipher and a Key...

*How to Encipher*
Select Option 1.) Encipher
Enter Your Message for Encoding/Encryption (e.g. - ATTACK)
Enter Your Desired Key - Used for Decipher (e.g. - HELLO)
Resulting Output is Your New Cipher (e.g. - HXELQR)

*How to Decipher* - With Cipher & Key
Select Option 2.) Decipher
Enter Your Generated Cipher
Enter Your Chosen Key
Output is the Original Message