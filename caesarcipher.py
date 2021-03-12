# Criptography project
# Author >>> Yago Goltara

import alphabet
import art
import os
import time

def caesar(text, shift, direction):
    end_msg = ''
    
    if shift > 26:
        shift = shift % 26 

    if(direction == 'encode') or (direction == 'decode'):
        for letter in text:
            if letter not in abc:
                end_msg += letter
            else:
                pos = abc.index(letter)

                if(direction == 'encode'):
                    position = pos + shift
                    if(position >= 26):
                        position -= 26  
                    end_msg += abc[position]

                elif(direction == 'decode'):
                    position = pos - shift
                    if(position < 0):
                        position += 26
                    end_msg += abc[position]
 
        if(direction == 'encode'):
            print(f"The encrypted message is: {end_msg}")
        else:
            print(f"The decrypted message is: {end_msg}")
    
    else:
        print("Insert a valid command.\n")

#------------------------------->
#                               |
#   BEGINNING OF THE PROGRAM    |
#                               |
#------------------------------->

logo = art.logo
abc = alphabet.alphabet
want_to_quit = False

while want_to_quit == False:
    os.system('cls')
    direction = input(f"{logo}\nType ENCODE to encrypt a message\nor DECODE to decrypt a message: ").lower()
    text = input("Type the message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)
    opt = input("\nDo you want to go again? Type YES or NO:\n").lower()
    if opt == "no":
        want_to_quit = True
        print("Goodbye :)\n")
        time.sleep(3)