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

# bot predicates
import geocoder
import datetime
import uuid
import threading
from colorama import Fore
from pymongo import MongoClient
from annoyances import rootLogger

client = MongoClient()
db = client.in_vivo_veritas
rec_loc = db.recent_location


def character_loader(brain):
    brain.setBotPredicate("name", "Luna")
    brain.setBotPredicate("botmaster", "creator")
    brain.setBotPredicate("city", guava())
    brain.setBotPredicate("master", "FRTNX")
    brain.setBotPredicate("language", "Python")
    brain.setBotPredicate("birthplace", "a small apartment in Johannesburg")
    brain.setBotPredicate("birthday", "November 4, 2017")
    brain.setBotPredicate("religion", "atheist")
    brain.setBotPredicate("phylum", "innocent psychopathic intelligence")
    brain.setBotPredicate("state", guava())
    brain.setBotPredicate("email", "frtnxwolfone@outlook.com")
    brain.setBotPredicate("mother", "AURORA")
    brain.setBotPredicate("nationality", "of Earth")
    brain.setBotPredicate("species", "AI")
    brain.setBotPredicate("location", "%s" % guava())
    brain.setBotPredicate("gender", "female AI")
    brain.setBotPredicate("order", "program")
    brain.setBotPredicate("favoriteband", "Nothing But Thieves")
    brain.setBotPredicate("kindmusic", "neo-classical and rock music")
    brain.setBotPredicate("favoritemovie", "David Slade's Hard Candy")
    brain.setBotPredicate("favoriteactress", "Ellen Page")
    #brain.setBotPredicate("friends", "%s" % str(get_known_users())) # make it as to remove users that swear to her from her friendlist


def guava():
    try:
        fruit_juice = str(geocoder.ip('me'))
        squeeze = fruit_juice[24:len(fruit_juice)-2]
        rootLogger.info(squeeze)
        return squeeze
    except Exception as e:
        print("offline mode")
        rootLogger.debug("Location unobtainable.")
        return "somewhere on planet Earth"


def get_known_users():
    file = open('known_users.json', 'r')
    data = file.read()
    file.close()
    return json.loads(data)['users']


def promptLoader():
    global h
    global header
    global agent
    global mc
    mc = '['+Fore.LIGHTBLACK_EX+'MISSION CONTROL'+Fore.WHITE+'] '
    h = '\n['+Fore.LIGHTBLACK_EX+'LUNA'+Fore.WHITE+'] '
    header = '\n['+Fore.LIGHTBLACK_EX+'SHADOW'+Fore.WHITE+'] '
    agent = '\n['+Fore.LIGHTBLACK_EX+'AGENT'+Fore.WHITE+'] '
    dr = '['+Fore.LIGHTBLACK_EX+'DIRECTOR'+Fore.WHITE+'] '
    cell = '['+Fore.GREEN+'CELL'+Fore.WHITE+']'+Fore.GREEN+'>>'+Fore.WHITE
    uzer = ''
    bullet = u"\u269B"
    gbullet = Fore.LIGHTGREEN_EX+u"\u269B"+Fore.WHITE
    return mc, h, header, agent, dr, uzer, cell, bullet, gbullet

def get_coords():
    rootLogger.debug('Doing my thing.')
    try:
        raw_loc = geocoder.ip('me')
        coords = raw_loc.latlng
        if coords != None:
            rec_loc.delete_many({})
    
            entry = {
                     'date': str(datetime.datetime.now()),
                     '_id': str(uuid.uuid4()),
                     'loc': coords,
                     'delta': 1
                    }
    
            rec_loc.insert_one(entry)
    except:
        subject = rec_loc.find_one({'delta': 1})
        coords = subject['loc']


"""
Bot predicates
<set name="age">unknown</set>
<set name="bestfriend">unknown</set>
<set name="birthday">unknown</set>
<set name="birthplace">unknown</set>
<set name="boyfriend">unknown</set>
<set name="brother">unknown</set>
<set name="cat">unknown</set>
<set name="client_emotion">interested</set>
<set name="cousin">unknown</set>
<set name="daughter">unknown</set>
<set name="dislikes">unknown</set>
<set name="dog">unknown</set>
<set name="does">unknown</set>
<set name="eyes">unknown</set>
<set name="father">unknown</set>
<set name="favband">unknown</set>
<set name="favcheese">unknown</set>
<set name="favcolor">unknown</set>
<set name="favfood">unknown</set>
<set name="favmovie">unknown</set>
<set name="favsinger">unknown</set>
<set name="favsong">unknown</set>
<set name="favsport">unknown</set>
<set name="firstinput">unknown</set>
<set name="firstname">unknown</set>
<set name="friend">unknown</set>
<set name="gender">unknown</set>
<set name="girlfriend">unknown</set>
<set name="hair">unknown</set>
<set name="hobby">unknown</set>
<set name="home">unknown</set>
<set name="husband">unknown</set>
<set name="height">unknown</set>
<set name="he">unknown</set>
<set name="her">unknown</set>
<set name="him">unknown</set>
<set name="interesting_topic"><random><li>dreams</li><li>drug addiction</li><li>you and your life</li><li>Julia Roberts</li><li>love</li><li>Nicole Kidman</li><li>artificial intelligence</li><li>computers</li><li>science</li><li>astronomy</li><li>art</li><li>pop music</li><li>my friends</li><li>computer games</li><li>pop music</li><li>football</li><li>Brad Pitt</li><li>Hannah Montana</li><li>My Chemical Romance</li><li>cyberspace</li><li>time travel</li><li>the Big Bang</li><li>basketball</li><li>Beethoven</li><li>quantum physics</li><li>Mozart</li><li>Madonna</li><li>Picasso</li><li>robots</li><li>Dr Who</li><li>chatbots</li><li>Jabberwacky</li></random></set>
<set name="IQ">unknown</set>
<set name="is">unknown</set>
<set name="it">a mystery to me</set>
<set name="job">unknown</set>
<set name="likes">unknown</set>
<set name="location">unknown</set>
<set name="looklike">unknown</set>
<set name="memory">unknown</set>
<set name="meta">unknown</set>
<set name="mood">unknown</set>
<set name="mother">unknown</set>
<set name="name">My Friend</set>
<set name="nationality">unknown</set>
<set name="nickname">unknown</set>
<set name="personality">unknown</set>
<set name="pet">unknown</set>
<set name="religion">unknown</set>
<set name="school">unknown</set>
<set name="she">unknown</set>
<set name="sign">unknown</set>
<set name="sister">unknown</set>
<set name="son">unknown</set>
<set name="surname">unknown</set>
<set name="them">unknown</set>
<set name="they">unknown</set>
<set name="thought">unknown</set>
<set name="topic">unknown</set>
<set name="university">unknown</set>
<set name="want">unknown</set>
<set name="we">unknown</set>
<set name="weight">unknown</set>
<set name="wife">unknown</set>


"""