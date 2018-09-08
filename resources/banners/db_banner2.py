import sys
import random
import time
from colorama import Fore

ban = ["                     ########################################################################",
       "                     ########################################################################",
       "                     ####### LLLL ####### UUU ### UUU ## NN NNNNNN ######### AAAA ###########",
       "                     ####### LLLL ####### UUU ### UUU ## NNNNNNNNNNN ###### AAAAAAA ######### ",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ### NNNN #### AAA # AAA ########",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #######",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #######",
       "                     ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ####### LLLLLLLLL ### UUUUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ####### LLLLLLLLL ##### UUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######",
       "                     ########################################################################",
       "                     ###############################################################"]

x = ['#########']

char_set = ['1','2','3','4','5','6','7','8','9','#','@','F','R','T','N','X']

banner_line = 1

x_column = 1

print('\n\n')
for line in ban:
    for letter in line:
        if letter == '#':
            print(Fore.LIGHTBLACK_EX+random.choice(char_set), end='')
            time.sleep(0.0001)
            sys.stdout.flush()
        elif letter == ' ':
            print(letter, end='')
            sys.stdout.flush()
        else:
            print(Fore.GREEN+random.choice(char_set), end='')
            time.sleep(0.0001)
            sys.stdout.flush()
    banner_line += 1
    if banner_line == 13:
        for line in x:
            for char in line:
                if x_column == 9:
                    time.sleep(1)
                    print(Fore.GREEN+random.choice(char_set))
                else:
                    print(Fore.LIGHTBLACK_EX+random.choice(char_set), end='')
                    time.sleep(0.09)
                    sys.stdout.flush()
                    x_column += 1
            print()
    else:
        print()

print(Fore.WHITE+'\n\n')