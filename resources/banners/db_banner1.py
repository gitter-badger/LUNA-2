import random
from colorama import Fore

ban = ["         #############################################################################",
       "         #############################################################################",
       "         ####### LLLL ####### UUU ### UUU ## NN NNNNNN ######### AAAA ###########################",
       "         ####### LLLL ####### UUU ### UUU ## NNNNNNNNNNN ###### AAAAAAA #########################",
       "         ####### LLLL ####### UUU ### UUU ## NNN ### NNNN #### AAA # AAA ##########################",
       "         ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #########################",
       "         ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAAAAAAAAAA #########################",
       "         ####### LLLL ####### UUU ### UUU ## NNN ##### NNN ## AAA ### AAA #########################",
       "         ####### LLLLLLLLL ### UUUUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######################",
       "         ####### LLLLLLLLL ##### UUUUUUUU ## NNN ##### NNN ## AAA ### AAA #######################",
       "         #############################################################################",
       "         #############################################################################"]

char_set = ['1','2','3','4','5','6','7','8','9','#','@','F','R','T','N','X']

print('\n\n')
for line in ban:
    for letter in line:
        if letter == '#':
            print(Fore.LIGHTBLACK_EX+random.choice(char_set), end='')
        elif letter == ' ':
            print(letter, end='')
        else:
            print(Fore.GREEN+random.choice(char_set), end='')
    print()
print(Fore.WHITE+'\n\n')