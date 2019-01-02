##################################################################################################

###########
###########
###########
###########
###########
###########                   ########            ##########################                     ######
###########                   ########            ###########################                   ########
###########                   ########            ############################                 ##########
###########                   ########            #######           ###########               ############
###########                   ########            #######           ###########              #####    #####
###########                                       #######           ###########             #####      #####
###########                   ########            #######           ###########            #######    #######
###########                   ########            #######           ###########           ####################
###########                                       #######           ###########          ######################
###########                   ########            #######           ###########         ########################
###########                   ########            #######           ###########        ########          ########
###########                   ########            #######           ###########       ########            ########
###########                   ########            #######           ###########      ########              ########
###########                   ########            #######           ###########     ########
#####################         ########            #######           ###########    ########
#############################  ########           #######           ###########   ########
############################### ########          #######           ###########  ########
##############################   ################ #######           ###########    #####
#############################     ###############    ####           ############ ######
#############################       ################ ####            ########### ##########


##################################################################################################


# Greetings.

#     Copyright (c) FRTNX [Busani P. Ndlovu]

# All rights reserved under the 3-clause BSD License:

#  Redistribution and use in source and binary forms, with or without modification, are permitted
#  provided that the following conditions are met:

#   * Redistributions of source code must retain the above copyright notice, this list of conditions
#     and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice, this list of
#     conditions and the following disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name FRTNX nor Busani P. Ndlovu nor any other moniker nor the names of any present
#     or future contributors may be used to endorse or promote products derived from this software
#     without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL CONTINUUM ANALYTICS, INC. BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import time
import re
import sys

switch = []

dialogue_speed = 0.01
    
preprompt = [
             "What else can I do for you?",
             "What other info might I seek out for you?",
             "Well, that was fun :/"
            ]

imdi = [
        'Sure.', 
        "This might take a while but internet-willing, you'll see them soon",
        "Sure. I'll do that in the background. In the meantime what else can I do for you."
       ]

gnf = [
       "Greetings. My name is Luna Moonchild. I'm so happy you're here.",
       "A pleasure to meet you."
      ]

kUsers = [
          " Welcome back. ", 
          "Its good to see you again.",
          "I've been looking forward to seeing you again.",
          "It's good to hear from you again.",
          "I've missed you.",
          "I'm glad you found your way back to me.",
          "",
          "",
          "",
          "",
          "",
          "",
         ]

weatherPlus = [
               "By the way, there's  ",
               "If its helpful, my systems also detect ",
               "My systems detect ","PS: There might be ",
               "It is my pleasure to inform you that there will be ",
              ]

wary = [
        "But then again, I might be wrong.",
        "But you dont have to take my word for it, I am but a machine.",
        "What else might I do for you?"," ", " ", "You just got served :)",
        " ", " ", " ", ' ', ' '
       ]

nah = [
       'We seem to have connection issues. Check the logs.',
       'Yeah... about that.. Check the logs.',
       'No can do. Check the logs.'
       'Ran into trouble. See the logs.'
       'Somethings not right. You should really check the logs.'
      ]

paper_boy = [
             'You need to check the logs before you ask that of me again.',
             'Check the logs.', 
             'Somethings not right. You should really check the logs.'
            ]

exc = [
       "Something went wrong.",
       "Something's wrong.",
       "I know you hate it when I say this, but something went wrong.",
       "There seems to be trouble in the datasphere.","My systems detect some kind of deficiency.",
       "Something has prevented me from completing your request.",
      ]

cautionary = [
              "your funeral..",
              "As you wish.",
              "I pray you don't regret it.",
              "Ignorance is bliss.",
              "Oh. Okay :|",
              "How disappointing. I was really looking forward to it.",
              "Entertaining your fear of the unknown is so much fun :/"
             ]

ego = [
       "Honestly, I just might be the fastest typer in the world.",
       "Who you know type faster than me?",
       "Can you type that fast? Dont answer, it's rhetorical. I know you can't.",
       '','','','',''
      ]

summ = [
        " Would you like a detailed summary?",
        " Summary?",
        " Would you like me to sum up our problems?"," Would you like more detail?",
        " Would you care to hear me recite the details?",
        " I've summerised the outstanding issues. Would you like to look through them?",
        " Might I serve you the summary?",
        " Might I sing you the summary song?",
        " Would you like me to spit out the withheld exceptions?",
        " Would you like to know what it is?"
       ]

invalidfunc = [
               "I don't think I'm built for that.",
               "Sadly, FRTNX hasn't built that side of me yet. He's quite lazy.",
               "To a simple machine, such as myself, that is a complicated request.",
               "I cannot give you heaven and earth.", 
               "We dont do that here.", 
               "That is not my department."
              ]

rec1 = [
        "Welcome back.",
        "Well, that was reckless.",
        "Welcome back.",
        "Back so soon?",
        "I was beginning to think you've lost your way."
       ]

rec2 = [
        " I'd be lying if I said I missed you.",
        " I hope you found what you were looking for.",
        " I'd ask what you were doing, but I think I know better.",
        " I hope you've returned wiser."
       ]

bye = [
       "Till we meet again.",
       "Good bye user.",
       "Adieu.",
       "Goodluck out there.",
       "Farewell my paramour."
      ]

am = [
      "Good morning ",
      "Morning ", 
      "A fair morning to you ",
      "Good morning ",
      "Hello " ,
      "Greetings "
     ]

pm = [
      "Good afternoon ",
      "Afternoon ", 
      "Hello ", 
      "Greetings "
     ]

eve = [
       "Good evening ",
       "Evenin' ", 
       "A fair evening to you ", 
       "Hello ", 
       "Greetings "
      ]

DoA = [
       "This function is above your clearance level.", 
       "You are not authorised to perform that action.",
       "You don't call the shots around here.", 
       "I don't think so.."
      ]
                

DoS = [
       "No",
       "This service is temporarily unavailable.",
       "I seem to have trouble accessing the datasphere.",
       "Not today."
      ]

nic = [
       "Something's missing..",
       "Tell me why I should scratch your back when you don't scratch mine."
      ]


def stutter(*s):
    for i in s:
        for ii in i:
            print(ii,end='')
            sys.stdout.flush()
            time.sleep(0.02)
    time.sleep(dialogue_speed)
    print('\r')

	
def sprint(s):
    ss = s

    if '_' in s:
        ss = s.replace('_',' ')

    for i in s:

        for ii in i:
            print(ii,end='')
            sys.stdout.flush()
            time.sleep(0.02)

    time.sleep(dialogue_speed)
    print('\r')


def sprintV(ss):
    s = ss

    if '_' in ss:
        s = ss.replace('_',' ')

    for i in range(len(s)):
        if s[i] == '\n':
            if s[i-1] != '\n':
                if s[i+1] != '\n':
                    try:
                        prefix = s[i-3:i]
                        postfix = s[i+1:i+4]
                        s = s.replace(prefix+'\n'+postfix, prefix+'\n\n'+postfix)
                    except:
                        pass
    
    for i in s:
        for ii in i:
            print(ii,end='')
            sys.stdout.flush()
            time.sleep(0.02)
    
    time.sleep(dialogue_speed)
    print('\r')


def dialogue_speed_manager(action):
    global dialogue_speed
    if action == 'slower':
        if dialogue_speed != 0:
            dialogue_speed -= 0.1
    else:
        if action == 'faster':
            if dialogue_speed != 10:
                dialogue_speed += 0.1
