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

from annoyances import *
"""
This segment below serves as a first run wizard.
It installs dependencies and sets up the database.
"""
curFiles = os.listdir('./')

if 'ok.txt' not in curFiles:
    rootLogger.info('Running luna setup...')
    # os.system('bash install_dependencies.sh')
    for file in curFiles:
        if file.startswith('dump'):
            try:
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/intelligence.bson' % file)
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/files.bson' % file)
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/arcs.bson' % file)
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/science.bson' % file)
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/exploits.bson' % file)
                os.system('mongorestore --db in_vivo_veritas ./%s/in_vivo_veritas/research.bson' % file)
            except Exception as e:
                print(e)
                pass
    os.system('touch ok.txt')
    rootLogger.info('setup complete.')

"""
import bay
"""
import subprocess
import os
import gc
import http.client
import threading
import poplib
import geopy
import PIL
import sys
import imaplib
import getpass
import email as amoebe
import datetime
import glob
import pprint
import uuid
import webbrowser
import datetime
import wikipedia
import socket
import json
import aiml
import time
import inflect
import urllib.request
import random,re,smtplib,requests,pymongo,uuid
from stages.introduction import Introduction
from personality import *
from translator import trans_to_eng
from rasa_nlu.model import Interpreter
from bs4 import BeautifulSoup
from colorama import Fore
from functions.LunaResponses import *
from bs4 import BeautifulSoup
from goo import search
from lxml import html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing.pool import ThreadPool
from resources.algorithms import Stack
from pymongo import MongoClient
from subprocess import Popen
from pymongo import MongoClient
from difflib import SequenceMatcher
from datetime import date
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from PIL import Image
from email.header import Header, decode_header, make_header
from glob import glob

"""
Initialisation:
"""
rootLogger.debug('Initialising...')
layout = Nominatim()
num_word_transform = inflect.engine()

previous_model = config.find_one({'name': 'nlu_model'})
current_model = open('data/nlu/nlu.json', 'r')
current_model_data = current_model.read()
if current_model_data != previous_model['payload']:
    rootLogger.warn('New training data detected. Updating models with latest data...')
    os.system('make train-nlu')
    interpreter = Interpreter.load('models/luna/main_nlu')
    save_model()
try:
    interpreter = Interpreter.load('models/luna/main_nlu')
    rootLogger.info('Found pre-existing models. No training necessary.')
    save_model()
except:
    rootLogger.warn('No previous models found. Training new model.')
    os.system('make train-nlu')
    interpreter = Interpreter.load('models/luna/main_nlu')
    save_model()

pool = ThreadPool(processes=1)
war_mode = False  # TODO: set to True to speed up output rate. Best for time critical operations.

k = aiml.Kernel()
spine = './brain/'

try:
    brn = os.listdir(spine)
    k.loadBrain(spine+brn[0])
except Exception as e:
    rootLogger.error(e)
    rootLogger.error("I'm brainless.")

threading.Thread(target=character_loader, args=(k,)).start()
threading.Thread(target=get_coords).start()

client = MongoClient()
db = client.in_vivo_veritas
users = db.users
files = db.files
intel = db.intelligence
sci = db.science
research = db.research
arch = db.arcs
logs = db.logs
unread = db.unread
read = db.read
mv = db.mindvalley
sessions = db.sessions
hades = db.exploits
hades.create_index([('title',pymongo.ASCENDING)], unique=True)
intel.create_index([('title',pymongo.ASCENDING)], unique=True)
files.create_index([('payload',pymongo.ASCENDING)], unique=True)
files.create_index([('date',pymongo.ASCENDING)], unique=True)
arch.create_index([('date',pymongo.ASCENDING)], unique=True)

listed_db = sci  # supports hot-switching. see controlCentre
user = []
eLog = []
hh = []
virgil = []
mc, h, header, agent, dr, uzer, cell, bullet, gbullet = promptLoader()
LOCAL_TIMEZONE = str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
catcher = []
 
 
def O():
    print(header,end='');time.sleep(0.2)


def id_gen(datetime_string):

    x = datetime_string.replace(' ', '_')
    y = x.replace('-', '')
    z = y.replace(':', '')

    return "dump_"+z[:15]

"""
database back-up manager and state preserver
"""
def backup_manager(*cmd):
    rootLogger.info('saving state...')
    current_files = os.listdir('./')

    if date.today().weekday() == 2 or cmd:

        if cmd:
            if "notification.json" in current_files:
                os.remove('notification.json')

        for db_folder in cules:
            if db_folder.startswith('dump_'):
                os.system('rm -r %s' % db_folder)
            if db_folder == 'microsoft-office-windows-7.zip':
                os.system('rm -r %s' % db_folder)

        if "notification.json" not in current_files:
            os.system('mongodump --db in_vivo_veritas --collection files')
            os.system('mongodump --db in_vivo_veritas --collection intelligence')
            os.system('mongodump --db in_vivo_veritas --collection science')
            os.system('mongodump --db in_vivo_veritas --collection exploits')
            os.system('mongodump --db in_vivo_veritas --collection arcs')
            os.system('mongodump --db in_vivo_veritas --collection research')
            # os.system('mongodump --db in_vivo_veritas --collection recent_location') # Ahem..
            os.system('mv dump %s' % id_gen(str(datetime.datetime.now())))
            os.system('zip -r --exclude=ok.txt* microsoft-office-windows-7.zip *')
            notify = open('notification.json', 'w')
            notify.close()
            rootLogger.info('state saved.')

        else:
            print('\n%sA previous state exists that seems to have been left untouched. Repeat command to overwrite it.' % mc)
            rootLogger.warn('unattended state detected and sustained.')

    else:
        if "notification.json" in current_files:
            dismiss_notification = input('\n%sUrgent. Transfer database duplicate. Or have you done that already?\n%s' % (mc, dr)).lower()

            if dismiss_notification == 'yes':
                os.remove('notification.json')

            print('%sCopy. Over and out.' % mc)

    if cmd:
        controlCentre()

"""
And so it begins
"""

def H(*n):
    if not n:
        print(h, end='');
    else:
        print(n[0], end='')
    time.sleep(0.2)

def Hplus():
    print('\n'+h, end='');
    time.sleep(0.2)

def suggested_reading():
    titles = []
    for i in sci.find():
        titles.append(i['title'])
    selected = []
    for n in range(5):
        selected.append(random.choice(titles))
    print(beam)
    print('Suggested Reading:')
    print(beam)
    for t in selected:
        print(t)
        time.sleep(0.01)
    print(beam)
    time.sleep(1)


def Hello():
    now = datetime.datetime.now()
    online_bullet = Fore.GREEN + u"\u25CF " + Fore.WHITE
    print(online_bullet + str(now))
    banners = ['banner1.py'] # banner1 bias
    banner = random.choice(banners)
    os.system('python3 ./resources/banners/%s' % banner)
    time.sleep(1)
    categories = ["ethos", "AI", "Maths"]
    all_files = []
    quotes = []

    try:
        threading.Thread(target=get_quotes).start()

        for entry in files.find():
            if entry['code_name'] in categories:
                all_files.append(entry)

        for file in all_files:
            quotes.append(file['payload'][0])

        H();sprint(random.choice(quotes))
        rootLogger.info('Initialisation complete.')
        identify()

    except Exception as e:
        rootLogger.warn(str(e))
        rootLogger.info('Initialisation complete.')
        H();sprint(random.choice(quotes))
        identify()


def get_quotes():
    try:
        page = requests.get('https://www.brainyquote.com')
        tree = html.fromstring(page.content)
        q = tree.xpath('//a[@title="view quote"]/text()')

        for quote in q:
            try:
                entry = {
                          '_id': str(uuid.uuid4()),
                          'code_name': 'ethos',
                          'date': str(datetime.datetime.now()),
                          'payload': [quote]
                        }
                files.insert_one(entry)

            except Exception as e:
                rootLogger.debug(str(e)[str(e).find('"'):].replace('}', '').replace('"', ''))
                pass
    except Exception as e:
        rootLogger.error(str(e))
        return


def clean_db(void=False):
    rootLogger.info('Cleaning database.')
    dirty_files = False
    f = open('stop_words.txt', 'r')
    raw_text = f.read()
    stop_words = raw_text.split('\n')
    for file in files.find():
        for sw in stop_words:
            if sw in file['payload'][0].lower() and sw != '':
                if file['code_name'] == 'ethos':
                    rootLogger.warn('Deleting %s' % file['_id'])
                    files.delete_one({
                                      '_id': file['_id']
                                     })
                    dirty_files = True
    if not dirty_files:
        rootLogger.info('No dirty files found.')
    rootLogger.info('Database cleansing complete.')
    if not void:
        H(); sprint('Database cleansed.')
        controlCentre()
    else:
        return


def identify():
    rootLogger.info('Identifying user...')
    global uzer

    try:
        time.sleep(1.5)
        user_name = input("\n                                              Code Name:")
        known_users = get_known_users()

        if user_name == os.getenv("PRIUSER"):
            user.append(user_name)
            uheader = create_prompt(user[0])
            uzer = uheader
            hh.append(uheader)
            time.sleep(1)
            H();sprint("%scommander." % timemaster())

        elif user_name.lower() in known_users:
            user.append(user_name)
            uheader = create_prompt(user[0])
            uzer = uheader
            hh.append(uheader)
            H(); sprint('%s%s. %s' % (timemaster(), user_name, random.choice(kUsers)))

        else:
            user.append(user_name)
            users.insert_one({
                '_id': str(uuid.uuid4()),
                'name': user_name,
                'created': str(datetime.datetime),
                'data': []
            })
            uheader = create_prompt(user[0])
            uzer = uheader
            time.sleep(1)
            H(); sprint("%s%s. My name is Luna. Luna Moonchild." % (timemaster(),user_name.title()))
            introduction = Introduction()
            sprint(introduction.run())

        k.setPredicate("name", user_name)
        rootLogger.info('User identified as %s' % user_name)
        controlCentre()

    except KeyboardInterrupt as e:
        rootLogger.debug('shutting down...')
        return


def get_known_users():
    known_users = []
    for user in users.find():
        known_users.append(user['name'].lower())
    return known_users


def create_prompt(name):
    return '\n[' + Fore.LIGHTBLACK_EX + name.upper() + Fore.WHITE + '] '


def timemaster():
    t = datetime.datetime.now()
    tstr = str(t)
    pattern = r'([0-9]+):([0-9]+):[0-9][0-9]'
    trgt = re.search(pattern, tstr)
    v = trgt.group()
    n = int(v[:2])
    if n < 12:
        return random.choice(am)
    elif n >= 18:
        return random.choice(eve)
    else:
        return random.choice(pm)


def TimeOut():
    switch.clear()
    user.clear()
    stutter("\n\n***Trust is such a fickle thing.***")


def findExternalResource():
    H(); sprint("What do you need?")
    res = input(uzer)
    try:
        # for anonymity edit google library to run through proxychains
        urls = search(res, stop=20)
        H(); sprint("Take your pick.")
        for url in urls:
            print(url)
            time.sleep(0.03)
        controlCentre()
    except Exception as e:
        rootLogger.debug(str(e))
        H(); sprint(random.choice(nah))
        controlCentre()


def imageFinder(entity, num_instances):
    #print("this is beta value %s" % entity)
    try:
        os.system( 'googleimagesdownload --keywords "%s" --limit %s' % (entity, num_instances) )
        H(); sprint("You know where to find them.")
    except KeyboardInterrupt:
        H(); sprint("You know where to find them.")

    controlCentre()


def imageShow(entity, num_instances):
    rootLogger.info('Searching for %s images on background thread' % num_instances)
    entity = entity.replace(' ', '_').replace('(', '').replace(')', '').replace("'","").lower()
    basewidth = 400  # This value controls the width of images displayed. Edit as needed.

    try:
        os.system('googleimagesdownload --keywords "%s" --limit %s >/dev/null 2>&1' % (entity, num_instances))
        displayList = os.listdir('./downloads/%s/' % entity)
        for image in displayList:
            img = Image.open('./downloads/%s/%s' % (entity, image))
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            img.show()
        time.sleep(20)
        os.system('rm -r ./downloads/%s --force' % entity)
        return
    except Exception as e:
        rootLogger.error(e)
        return


def reception():
    time.sleep(1)
    H();sprint(random.choice(rec1)+random.choice(rec2))
    controlCentre()


def alert(name):
    Name = name.title()

    try:
        fa = os.getenv('LUNADDR')
        ta = os.getenv('MYEMAIL')
        msg = MIMEMultipart()
        msg['From'] = fa
        msg['To'] = ta
        msg['Subject'] = "Attempted Security Breach"
        body = "Hello commander. Someone by the name of %s tried accessing the Shadow program. Just thought you should know.\n\n\nLUNA." % Name
        msg.attach(MIMEText(body,'plain'))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fa, os.getenv('EMAILPWD'))
        text = msg.as_string()
        server.sendmail(fa,ta,text)
        server.quit()
    except Exception as e:
        rootLogger.debug('mail alert for shadow function failes due to %s' % str(e))
        pass


def log(detail):
    try:
        fa = os.getenv('LUNADDR')
        ta = os.getenv('MYEMAIL')
        msg = MIMEMultipart()
        msg['From'] = fa
        msg['To'] = ta
        msg['Subject'] = "Active"
        page = requests.get('https://www.brainyquote.com/topics/mathematics')
        tree = html.fromstring(page.content)
        q = tree.xpath('//a[@title="view quote"]/text()')

        for quote in q:
            try:
                entry = {
                          '_id': str(uuid.uuid4()),
                          'code_name': 'Math',
                          'date': str(datetime.datetime.now()),
                          'payload': [quote]
                        }
                files.insert_one(entry)
            except Exception as e:
                pass

        quotes = []
        for i in files.find():
            if i['code_name'] == 'Math':
                quotes.append(i['payload'][0])
        for quote in q:

            try:

                entry = {
                          '_id': str(uuid.uuid4()),
                          'code_name': 'ethos',
                          'date': str(datetime.datetime.now()),
                          'payload': [quote]
                        }
                files.insert_one(entry)

            except Exception as e:
                pass

        lucky_candidate = random.choice(quotes)
        body = "[%s]  %s \n\n%s" % (str(datetime.datetime.now())[:19], detail, lucky_candidate)
        msg.attach(MIMEText(body,'plain'))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fa, os.getenv('EMAILPWD'))
        text = msg.as_string()
        server.sendmail(fa, ta, text)
        server.quit()

    except Exception as e:
        pass


def delete_latest():
    numMessages = 2
    try:
        mailserver = poplib.POP3_SSL('pop.gmail.com')
        mailserver.user('recent:%s' % os.getenv('LUNADDR'))
        mailserver.pass_(os.getenv('EMAILPWD'))
        numMessages = len(mailserver.list()[1])
        mailserver.dele(numMessages)
        mailserver.quit()
        rootLogger.info("Mail clean up successful.")
    except:
        rootLogger.warn("Could not clean up mail. Manual removal required. Sorry Bud.")
        return


def store_session_data(text):
    new_entry = {
                  'text': text,
                  'date': str(datetime.datetime.now()),
                  '_id': str(uuid.uuid4())
                }
    sessions.insert_one(new_entry)


def pop_dense():
    H(); sprint("Please enter the number of people who live in this area.")
    population = input(uzer).replace(',','')
    H(); sprint("Enter the size of the area in square kilometers.")
    area = input(uzer).replace(',','')
    H(); sprint("The population density of this area is %s people per square kilometer." % str(int(population)/int(area)))
    controlCentre()


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string


def terminal_session():
    cmd = input(Fore.BLUE+'\n%s@blueterm$ ' % user[0].lower() + Fore.WHITE)
    if cmd != 'exit':
        os.system(cmd)
        terminal_session()
    else:
        H(); sprint('Terminal terminated.')
        controlCentre()


def init_translator(*session):
    if not session:
        H(); sprint('translator activated.')
    raw_text = input(uzer)
    if raw_text.lower() != 'exit':
        human_lang_translator(raw_text)
    else:
        H(); sprint('translator terminated.')
        controlCentre()


def human_lang_translator(text):
    try:
        H(); sprint(trans_to_eng(text))
    except Exception as e:
        rootLogger.error(str(e))
        H(); sprint('Some of my agents seem to be inhibited. Check the logs.')
    init_translator(*['session'])


def code_search():
    H(); sprint('Enter phrase or code snippet')
    term = input(uzer)
    H(); sprint("Please enter the path to the folder you'd like to begin the search from.")
    root_dir = input(uzer)
    ftypes = ['*']
    try:
        H(); sprint("Looking it up..")
        os.system("gnome-terminal -e \"grep -rnw '%s' -e '%s'\"" % (root_dir, term))
    except KeyboardInterrupt as e:
        controlCentre()
    except Exception as e:
        print(e)
        pass
    controlCentre()


def quote_search():
    H(); sprint('Enter search term')
    term = input(uzer)
    found = False
    for file in files.find():
        if term.lower() in file['payload'][0].lower():
            print(file['payload'][0])
            found = True
    if not found:
        sprint("Could'nt find anything related to that")
    controlCentre()


# TODO: to be implemented
def lightSpeed():
    lightspeed = 186000
    H(); sprint("Enter number of days.")
    days = input(uzer)
    seconds = days *24 *60 *60 # convert to seconds
    distance = lightspeed * seconds
    H(); sprint( "In %s days light will have travelled about %s miles" % (days, distance) )
    controlCentre()


def groundDistance(point_x, point_y):
    try:
        x_raw = layout.geocode(point_x)
        y_raw = layout.geocode(point_y)
        x = (x_raw.latitude, x_raw.longitude)
        y = (y_raw.latitude, y_raw.longitude)
        xydistance = vincenty(x,y).kilometers # other options: .nautical, .miles, .ft, ...etc. see docs
        H(); sprint("The distance between %s and %s is %s kilometers" % (point_x.title(), point_y.title(), xydistance))
        controlCentre()
    except Exception as e:
        rootLogger.error(e)
        groundDistance(point_x, point_y)


def gridWeight(entity):
    try:
        loc = layout.geocode(entity)
        H(); sprint("%s has an importance weight of %s" % (entity.title(), loc.raw['importance']))
        controlCentre()
    except Exception as e:
        rootLogger.error(e)
        gridWeight(entity)


def find_root(t):
    index = float(t[t.find('the')+4:t.find('root')-1])
    radicand = float(t[t.find('of')+3:])
    root = radicand**(1/index)
    H(); sprint('The %s root of %s is %s' % (index, radicand, root))
    controlCentre()


def converter(string):
    request = string

    mapper = [
               { 'binary': 2 },
               { 'ternary': 3 },
               { 'quarternary': 4 },
               { 'quinary': 5 },
               { 'senary': 6 },
               { 'septenary': 7 },
               { 'octal': 8 },
               { 'nonary': 9 },
               { 'decimal': 10 },
               { 'undenary': 11 },
               { 'duodecimal': 12 },
               { 'hexadecimal': 16 },
               { 'vigesimal': 20 },
               { 'sexagesimal': 60 }
            ]

    formats = []

    for mapp in mapper:
        formats.append(list(mapp)[0])

    if request.endswith('to decimal'):
        seg = request[:len(request)-8]
        base = ''
        for form in formats:
            if form in seg:
                base = form
        if base != '':
            extracted = 0
            for f in mapper:
                if list(f)[0] == base:
                    extracted = f[base]
            operand = seg[seg.find(base) + len(base) + 1: seg.find('to')]
            H(); sprint(int(operand, extracted))
            controlCentre()
    else:
        base = ''
        for formatt in formats:
            if formatt in request:
                base = formatt
        if base != '':
            extracted = 0
            for f in mapper:
                if list(f)[0] == base:
                    extracted = f[base]
        else:
            H(); sprint("Sorry. I couldn't convert that.")
            rootLogger.error('No converter found')
        stop1 = string.find(' to ')
        operand = string[8:stop1]
        try:
            H(); sprint(base_converter(int(operand), extracted))
            controlCentre()
        except Exception as e:
            print(str(e))
            controlCentre()


def help_center():
    f = open('commands.txt', 'r')
    ff = f.read()
    print(ff)
    controlCentre()


def directions(req):
    try:
        s = req.find('from')
        destination = req[:s-1]
        if 'from' in req:
            source = req[s+5:]
        else:
            source = location_finder()
        H();sprint('Charting a course to %s from %s.' % (destination.title(), source.title()))
        webbrowser.open('https://www.google.com/maps/dir/%s/%s' % (source, destination))
        controlCentre()
    except Exception as e:
        print(e)
        controlCentre()


def prepare_listing():
    temp = []
    temp2 = []
    for file in listed_db.find():
        if '\n' not in file['title']:
            if len(file['title']) < 40:
                temp.append(file['title'].strip())
            else:
                temp2.append(file['title'].strip())
    return temp, temp2


def confessional(*e):
    temp = []
    if e:
        for file in hades.find():
            temp.append(file['title'])

        H(); sprint("Voila...")
        for entry in temp:
            sprint(entry)
        ethan()

    else:
        try:
            start = time.time()
            async_res = pool.apply_async(prepare_listing)
            H(); sprint("I've done my homework on the following:")
            db_banners = ['db_banner2.py'] # for posterity: add other database banners here
            os.system('python3 ./resources/banners/%s' % random.choice(db_banners))
            rootLogger.info('Compiling database. This might take a while...')
            compiled = False
            while not compiled:
                temp, temp2 = async_res.get()
                if len(temp)+len(temp2) < listed_db.count():
                    rootLogger.debug('ratio temps: listed_db.count() %s: %s' % (len(temp)+len(temp2), listed_db.count()))
                else:
                    if len(temp)+len(temp2) >= listed_db.count():
                        compiled = True
            end = time.time()
            process_time = end-start
            temp.sort(); temp2.sort()
            raw = str(listed_db)[len(str(listed_db))-20:]  # this is a really
            db_name = raw[raw.find(',')+1:].replace(')', '').replace("'", '').strip() # bad
            rootLogger.info('Finished loading %s database. latency is at %s seconds.' % (db_name, str(end-start))) # algorithm
            rootLogger.debug('len(temp) = %s' % len(temp))
            rootLogger.debug('len(temp2) = %s' % len(temp2))

            file_count = len(temp)+len(temp2)

            if process_time < 2: # tip: banner prints at a mean 2 seconds.
                time.sleep(2-process_time)

            column_len = len(temp) // 3
            a_space = 40
            b_space = 40
            max_len = 0

            # Extra bit of code ensures neat presentation
            a_sequence = []
            b_sequence = []
            a = 0
            b = 1
            while (a < len(temp) and b < len(temp)):
                a_sequence.append(temp[a])
                b_sequence.append(temp[b])
                a += 3
                b += 3

            tri_release = []

            if len(temp) > 3:
                for i in temp:
                    tri_release.append(i)
                    if len(tri_release) == 3:
                        aSpace = a_space-len(tri_release[0])+2
                        bSpace = b_space-len(tri_release[1])+2
                        print("%s%s%s%s%s" % (tri_release[0], ' '* aSpace,
                                              tri_release[1], ' '* bSpace,
                                              tri_release[2]))
                        tri_release.clear()
                        time.sleep(0.01)
            else:
                if len(temp) == 2:
                    aSpace = a_space-len(tri_release[0])+2
                    print("%s%s%s" % (tri_release[0], ' '* aSpace,
                                      tri_release[1]))
                else:
                    print(tri_release[0])

            if temp2 != []:
                print(beam)
                for title in temp2:
                    print(title)
                    time.sleep(0.01)
            print(beam+'%s distinct files' % str(file_count))
        except KeyboardInterrupt as e:
            H(); sprint('Aborted.')
            controlCentre()
        except Exception as e:
            rootLogger.error(str(e))
            H(); sprint('Mine is a troubled mind. Check the logs and console me.')
            controlCentre()
    gc.collect()
    controlCentre()


def ethan():
    inp = input(uzer)
    if inp.startswith('open'):
        target = inp[5:]
        try:
            x = hades.find_one({'title': target})
            sprint(x['payload'])
            controlCentre()
        except Exception as e:
            H(); sprint("No record found.")
            controlCentre()
    else:
        controlCentre(*[inp])


def find_related(key_word):
    H(); sprint('This might take a while so please be patient.')
    try:
        keyword = key_word
        found = []
        count = 0
        cycle = 0
        for file in intel.find():
            if ' '+keyword.lower()+' ' in file['payload'][0].lower():
                found.append([file['payload'][0].lower().count(keyword.lower()), file['title']])
                count += file['payload'][0].lower().count(keyword.lower())
                cycle += 1
                if cycle == 1 or cycle == 100000:
                    rootLogger.debug('<<<%s>>>...>' % file['payload'][0].lower().count(keyword.lower()))
                    cycle = 0
    except KeyboardInterrupt as e:
        rootLogger.warning('User aborted search for keyword "%s".' % key_word)
        H(); sprint("I guess patience isn't your strong suit.")
        controlCentre()
        return

    if found:
        rootLogger.debug('keyword "%s" appears %s times in current universe.' % (key_word, str(count)))
        try:
            found.sort()
            found.reverse()
            for title in found:
                print('%s     (%s)' % (title[1].strip(), str(title[0])))
                time.sleep(0.02)
            controlCentre()
            return
        except KeyboardInterrupt as e:
            controlCentre()

    else:
        H(); sprint("No mentions of %s exist locally, shall I do an internet sweep for requested data?" % key_word)
        response = input(uzer)
        if 'yes' in response:
            rootLogger.debug('relation seeker sent "%s" to informant.' % key_word)
            H(); sprint('Doing that.')
            informant(key_word, True, 0, False, *['relation seeker'])
        else:
            controlCentre(*[response])
            return


def informant(mark, img=True, latency=0, flesh=False, *flag):
    # rootLogger.debug('informant recieved: %s' % mark)
    # currently this only fetches data from wikipedia
    if img:
        threading.Thread(target=imageShow, args=(mark, 5,)).start()
    try:
        if flag:
            rootLogger.info('User requested document "%s".' % mark)
            rootLogger.warn('Nature of request requires internet. Attempting to connect...')
            try:
                s = time.time()
                res = wikipedia.page(mark)
                x = res.content
                y = res.title
                stop = x.find('\n\n\n')
                e = time.time()
                rootLogger.info('"%s" found. latency is at %s seconds.' % (y, str(e-s+latency)))
                H(); print(gbullet+'\n')
                if flesh:
                    rootLogger.info('Fleshing out requested document.')
                    directive(x, y, stop+3, *['flesh'])
                    controlCentre()
                    return
                if 'displaystyle' not in x[:stop] and 'textstyle' not in x[:stop]:
                    sprintV(x[:stop])
                else:
                    output_controller(x[:stop])
                directive(x, y, stop, *['enable-saving'])
            except KeyboardInterrupt as e:
                print('\n')
                directive(x, y, stop, *['enable-saving'])
            except Exception as e:
                rootLogger.debug(str(e))
                H(); sprint(random.choice(nah))
                controlCentre()

        else:
            rootLogger.info('User requested document "%s".' % mark)
            start = time.time()
            titles = []

            for file in intel.find():
                titles.append(file['title'])

            threshold = 0.86
            for title in titles:
                similarity = SequenceMatcher(None, mark.lower(), title.lower()).ratio()
                if similarity > threshold:
                    threshold = similarity
                    mark = title
                    rootLogger.debug('mark is now %s' % title)

            try:
                i = intel.find_one({'title': mark})
                content = i['payload'][0]
                stop = content.find('\n\n\n')
                end = time.time()
                rootLogger.info('"%s" found. latency is at %s seconds.' % (mark, str(end-start+latency)))
                H(); sprint(bullet+"\n")
                if flesh:
                    rootLogger.info('Fleshing out requested document.')
                    directive(content, mark, stop+3, *['flesh'])
                    controlCentre()
                    return
                if 'displaystyle' not in content[:stop] and 'textstyle' not in content[:stop]:
                    sprintV(content[:stop])
                else:
                    output_controller(content[:stop])
                directive(content, mark, stop, *['savenot'])
            except KeyboardInterrupt as e:
                print('\n')
                directive(content, mark, stop, *['savenot'])
            except Exception as e:
                end = time.time()
                rootLogger.error(str(e))
                rootLogger.error('Could not find requested document locally.')
                rootLogger.warning('Attempting to find requested document online.')
                informant(mark, False, end-start, flesh, *['engagethehive'])
    except KeyboardInterrupt as e:
        controlCentre()
    except Exception as e:
        rootLogger.debug(str(e))
        controlCentre()


# Bug watch. Wrote this in a hurry.
def directive(content, title, interm, *mode):
    if mode and mode[0] == 'flesh':
        flesh_fryer(content[interm:])
    action = input(uzer).lower()
    if not mode or mode[0] != 'flesh' and 'tell me more' in action:
        rootLogger.info('User has shown interest in document "%s".' % title)
        if 'displaystyle' not in content[interm:] and 'textstyle' not in content[interm:]:
            H(); print(content[interm:])
        else:
            H(); output_controller(content[interm:], *['plain'])
        if not mode:
            directive(content, title, interm, *['breakrecursion'])
        else:
            controlCentre()

    elif action == 'save':
        try:
            entry = {
                     '_id': str(uuid.uuid4()),
                     'title': title,
                     'date': str(datetime.datetime.now()),
                     'payload': [content]
                    }
            intel.insert_one(entry)
            H(); sprint("Saved.")
            controlCentre()
            return

        except Exception as e:

            H(); sprint("Previous intell already exists. Update?[yes/no]")
            overide = input(uzer).lower()
            if overide == 'yes':
                try:
                    arch.insert_one(intel.find_one({'title': title}))
                    intel.delete_one({'title': title})

                    entry = {
                             '_id': str(uuid.uuid4()),
                             'title': title,
                             'date': str(datetime.datetime.now()),
                             'payload': [content]
                            }
                    intel.insert_one(entry)
                    H(); sprint("Done.")
                    controlCentre()
                    return

                except Exception as e:
                    print(str(e))
                    controlCentre()
                    return
            else:
                if overide == 'no':
                    H(); sprint("Old entry sustained.")
                    controlCentre()
                    return

    else:
        controlCentre(*[action])


def flesh_fryer(flesh):
    if 'displaystyle' not in flesh and 'textstyle' not in flesh:
        print(flesh)
    else:
        output_controller(flesh, *['plain'])
    return


def output_controller(content, *plain):
    rootLogger.info('Output controller invoked.')
    x = content.split('\n')
    safe_words = ['is', 'or', 'to']
    for i in x:
        if len(i.replace(' ','')) <= 2 and i.replace(' ','') not in safe_words:
            print(i.replace(' ',''), end='')
        elif 'displaystyle' in i or 'textstyle' in i:
            print('\n')
        else:
            if '==' in i:
                print('\n')
            if not plain:
                sprint(i)
            else:
                print(i)


shit_times = 1


def find_lc(city):
    # rootLogger.debug('find_lc recived %s' % city)
    global shit_times
    try:
        lc = layout.geocode(city)
        shit_times = 0
        return [lc.latitude, lc.longitude]
    except:
        if shit_times <= 10:
            shit_times += 1
            find_lc(city)
        else:
            shit_times = 0
            return 'booper'


cycles = 1


def weather(void=False, api_request=False, *city):
    # if city:
        # rootLogger.debug('weather recieved %s' % city)
    global cycles

    try:
        if not city:
            subject = rec_loc.find_one({'delta': 1})
            coords = subject['loc']

        else:
            coords_raw = find_lc(city[0])
            if coords_raw != 'blooper':
                coords = []
                for coord in coords_raw:
                    c = str(coord)
                    coords.append(c[:8])

        page = requests.get('https://darksky.net/forecast/%s,%s/si24/en' % (coords[0], coords[1]))
        tree = html.fromstring(page.content)
        minTemp = tree.xpath('//span[@class="minTemp"]/text()')
        maxTemp = tree.xpath('//span[@class="maxTemp"]/text()')
        windhumidity = tree.xpath('//span[@class="num swip"]/text()')
        skystatus = tree.xpath('//span[@class="summary swap"]/text()')[0].lower()
        humidity = windhumidity[1]+'%'
        windspeed = windhumidity[0]+'m/s'
        currenttemp = skystatus[:3]+'c'
        maxtemp = maxTemp[0]+'c'
        mintemp = minTemp[0]+'c'
        visibility = windhumidity[2]+'km'
        pressure = windhumidity[3]+'hPa'
        rootLogger.debug('alpha')

        # print('maxtemp: %s\nmintemp: %s\nwindhumid: %s\nskystatus: %s\n' % (minTemp,
        #                                                                     maxTemp,
        #                                                                     windhumidity,
        #                                                                     skystatus))

        cloud_cover = ['clear.', 'partly cloudy.', 'overcast.', 'cloudy.',
                       'mostly cloudy.', 'ostly cloudy']

        temp_descOpts = ['freezing ', 'chilly ', 'warm ', 'hot ', 'blazing ']

        integers = ['0', '1','2','3','4','5','6','7','8','9']
        temp_num = []
        for i in skystatus:
            if i in integers:
                temp_num.append(i)
        tempState = int(''.join(temp_num))

        # TODO: add 15 - 20 = cool. Rearrange other values as necessary.
        if tempState < 10:
            descr = temp_descOpts[0]
        elif tempState >= 10 and tempState <= 15:
            descr = temp_descOpts[1]
        elif tempState >= 15 and tempState <= 23:
            descr = temp_descOpts[2]
        elif tempState >= 23 and  tempState <= 30:
            descr = temp_descOpts[3]
        elif tempState > 30:
            descr = temp_descOpts[4]

        if skystatus[4:] in cloud_cover:
            prefix = 'Skies are '

        else:

            if city:
                prefix = 'This location is currently experiencing '

            else:
                prefix = 'Our current position is experiencing '


        t = tree.xpath('//div[@class="summary"]/text()')
        l = t[0]

        if city:
            a1 = "Temprature readings in %s range between " % city[0].title()
            a2 = "c. Currently this position is at a "

        else:
            a1 = "Todays temperatures range between "
            a2 = ". Currently we are at a "

        ll = l.strip().lower()

        weather_json = {
                        '_id': str(uuid.uuid4()),
                        'date': str(datetime.datetime.now()),
                        'collectedFromTimezone': LOCAL_TIMEZONE,
                        'location': {
                                     'latitude': coords[0],
                                     'longitude': coords[1]
                                    },
                        'data': {
                                 'mintemp': mintemp,
                                 'maxtemp': maxtemp,
                                 'currentTemp': currenttemp,
                                 'humidity': humidity,
                                 'windspeed': windspeed,
                                 'skystatus': skystatus[4:],
                                 'visibility': visibility,
                                 'pressure': pressure
                                }
                        }

        rootLogger.debug('bravo')
        rootLogger.info('Constructed weather JSON: %s' % weather_json)
        research.insert_one(weather_json)
        # for file in research.find():
        #     pprint.pprint(file)
        if void:
            return
        if api_request:
            return json.dumps(weather_json)
        else:
            if not void:
                sprint(
                        "\n"+a1+ mintemp+ " and "+ maxtemp+ a2 + descr + currenttemp
                        +"." +"\n"+ "Humidity is at "+ humidity+ "."
                        +" Wind speed is at "+windspeed+"."+"\n"+ prefix
                        +skystatus[4:] + " " + t[1] + "\n" +random.choice(weatherPlus)
                        +ll+ " "+random.choice(wary)
                      )
        rootLogger.debug('charlie')
        cycles = 0
        controlCentre()
        return

    except KeyboardInterrupt as e:
        rootLogger.debug('User interupted weather request.')
        print('\n'); controlCentre()

    except Exception as e:
        rootLogger.error(str(e))
        if void:
            return
        if city:
            if cycles < 10:     # times out after 10 attempts
                cycles += 1     # TODO: it would be best to differentiate between no-internet
                weather(void, api_request, *city)  # and bad connection errors.
            else:
                rootLogger.debug(str(e))
                H(); sprint("Couldn't. Check the logs.")
                controlCentre()
        else:
            if void:
                return
            else:
                rootLogger.debug(str(e))
                H(); sprint("Couldn't. Check the logs.")
                controlCentre()


def zen():
    koans = []
    for file in files.find({'code_name': 'koan'}):
        koans.append(file['payload'][0])
    H(); print('\n'+random.choice(koans))
    controlCentre()


def nearby(req):
    try:
        mid = req.find('near')
        obj = req[:9-1]
        pos = req[9+5:]
        coords = find_lc(pos)
        H();sprint('Searching for %s near %s' % (obj, pos))
        webbrowser.open('https://google.com/maps/search/%s/@%s,%s' % (obj, coords[0], coords[1]))
        controlCentre()
    except Exception as e:
        rootLogger.debug(str(e))
        print("Couldn't comnply. Check the logs.")
        controlCentre()


def porter():
    uheader = '['+user[0].upper()+']'
    H(); sprint("Enter payload\n")
    lines = []
    try:
        while True:
            lines.append(input(cell))
    except EOFError:
        pass
    payload = "\n".join(lines)
    print('\n'); H(); sprint("Label the package")
    subject = input(uzer)
    H(); sprint("Who's the mark?")
    target = input(uzer)
    try:
        fa = os.getenv('LUNADDR')
        if not target:  # Env vars
            ta = os.getenv('MYEMAIL')
        else:
            ta = target
        msg = MIMEMultipart()
        msg['From'] = fa
        msg['To'] = ta
        msg['Subject'] = subject
        body = payload
        msg.attach(MIMEText(body,'plain'))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fa, os.getenv('EMAILPWD'))
        text = msg.as_string()
        server.sendmail(fa,ta,text)
        server.quit()
        H(); sprint("Package sent.")
        delete_latest()
        controlCentre()
    except:
        H(); sprint('Package sending failed.')
        controlCentre()


# beta code start.


def gen_gate():
    try:
        plyr1 = input(h+'Identify inquisitor\n\n:')
        if plyr1 == 'exit':
            H(); sprint('Manual training suspended.')
            controlCentre()
        plyr2 = input(h+'Identify donor\n\n:')
        if plyr2 == 'exit':
            H(); sprint('Session terminated.')
            controlCentre()
        if not plyr1:
            plyr1 = 'inquisitor'
        if not plyr2:
            plyr2 = 'donor'
        dialog_gen(plyr1, plyr2)
    except Exception as e:
        H(); sprint(e)
        controlCentre()


# use session database...
def dialog_gen(inq, don ):
    # TODO: Add the option of training on aiml-handled input
    try:
        pattern = input('\n[%s]' % inq.upper())
        if pattern == 'exit':
            H(); sprint('Session terminated.')
            controlCentre()
        template = input('\n[%s]' % don.upper())
        if template == 'exit':
            H(); sprint('Manual training suspended.')
            controlCentre()
        x = "<category><pattern>%s</pattern>\n<template>%s</template>\n</category>\n" % (pattern.upper(),template)
        f = open('.test.aiml', 'a')
        f.write(x)
        f.close()
        dialog_gen( inq, don)
    except Exception as e:
        H(); sprint(e)
        controlCentre()

# beta code end.


def media_player(artist):
    result = [y for x in os.walk('%s/Downloads' % os.path.expanduser('~')) for y in glob(os.path.join(x[0], '*.mp3'))]
    for file in result:
        if artist.lower() in file.lower():
            os.system('xdg-open "%s"' % file)
            controlCentre()
    H(); sprint('Could not find any %s' % artist)
    controlCentre()


def add_to_db(text):
    try:
        ukey = db.archives.create_index([('text',pymongo.ASCENDING)],
                                          unique=True)
        instance = {'text': text,
                    'date': str(datetime.datetime.utcnow()),
                    '_id': uuid.uuid4()
                   }
        arch.insert_one(instance)
    except Exception as e:
        pass


def lightIntel(): # a misnomer now
    try:
        page1 = requests.get('https://washingtonpost.com')
        tree1 = html.fromstring(page1.content)
        page2 = requests.get('https://techcrunch.com')
        tree2 = html.fromstring(page2.content)
        page3 = requests.get('https://www.medium.com')
        tree3 = html.fromstring(page3.content)
        excerpt = tree2.xpath('//a[@class="post-block__title__link"]/text()')
        H();print("\nTechCrunch:\n")

        articles = tree2.xpath('//a[@class="post-block__title__link"]/text()')
        for i in articles:
            print(i.strip())
            time.sleep(0.03)

        headlines1 = tree3.xpath('//h3[@class="ui-h3 ui-xs-clamp2 u-paddingTop4 ui-sm-clamp2"]/text()')
        headlines2 = tree3.xpath('//h3[@class="ui-h3 ui-clamp3"]/text()')
        headlines3 = tree3.xpath('//h3[@class="ui-h2 ui-xs-h4 ui-clamp3"]/text()')
        headlines4 = tree3.xpath('//h3[@class="ui-h4 ui-clamp3 u-marginBottom4"]/text()')
        headlines5 = tree3.xpath('//h3[@class="ui-h3 ui-clamp2"]/text()')
        headlines6 = tree3.xpath('//h3[@class="ui-h3 ui-xs-h4 ui-clamp3 u-marginBottom8"]/text()')
        headlines = headlines1 + headlines2 + headlines3 + headlines4 + headlines5 + headlines6
        time.sleep(25)
        stutter("\nMedium:\n")
        time.sleep(1)

        for i in headlines:
            print(i)
            time.sleep(0.03)

        headlinez = tree1.xpath('//a[@data-pb-placeholder="Write headline here"]/text()')
        time.sleep(25)
        stutter("\nWashington Post:\n")
        time.sleep(1)

        for i in headlinez:
            print(i)
            time.sleep(0.03)

        print(random.choice(ego))
        controlCentre()
    except KeyboardInterrupt as e:
        H(); sprint('Aborted.')
        controlCentre()

    except Exception as e:
        rootLogger.debug(str(e))
        H(); sprint(random.choice(paper_boy))
        controlCentre()


def laFibonacci():
    H(); sprint('The first two numbers are 1 and 1. Continue the sequence. The last one standing wins (I always win).')
    straws = [1,2]
    firstGo = random.choice(straws)
    if firstGo == 1:
        H(); sprint("I'll go first.")
        lunasTurn(1,1,0)
    else:
        usersTurn()


def usersTurn(n1=1, n2=1, depth=0):
    try:
        start = time.time()
        nextInt = n1+n2
        try:
            userNext = input(uzer)
            test = int(userNext)
        except Exception as e:
            controlCentre(*[userNext])
        end = time.time()
        gameOver = False
        if int(end - start) > 10:
            H(); sprint('You took too long. Your max depth is %s.' % depth)
            start_over()
        if int(userNext) != nextInt:
            H(); sprint('Cute. Max depth is %s.' % depth)
            gameOver = True
        if gameOver:
            start_over()
            # save high score to file. Sustain if depth is lower.
        else:
            n1 = n2
            n2 = nextInt
            depth += 1
            lunasTurn(n1, n2, depth)
    except KeyboardInterrupt as e:
        H(); sprint("Sequence terminated.")
        controlCentre()

def start_over():
    H(); sprint('Would you like to start over?')
    directive = input(uzer)
    if 'yes' in directive:
        laFibonacci()
    else:
        H(); sprint("Cool. It was nice reminding you who's the boss around here.")
        controlCentre()


def lunasTurn(n1,n2,depth):
    nextInt = n1+n2
    n1 = n2
    n2 = nextInt
    H(); time.sleep(2);print(nextInt)
    usersTurn(n1, n2, depth)


def save_new_user(user_list):
    new_file = {'users': user_list}
    new_file = json.dumps(new_file)
    file = open('known_users.json', 'w')
    file.write(new_file)
    file.close()


def Engage():
    print(Fore.LIGHTBLACK_EX+beam+Fore.WHITE)
    time.sleep(1.5)
    O();sprint('Welcome to Covert Operations')
    time.sleep(2)
    covertControl()


def covertControl():
    """Welcome to the other side.

Valid function triggers are:
        'butler' to obtain a targets ip address, or an ip addresses owner
        'tracker' to track an ip address's geographic location
        'recon' to get target server information
        'port' to run a port scan on a given target
        'strack' to geolocate a server given a url
        'study' if you wish to be educated on some program related issue
        'help' should you wish to see this dialogue again
        'exit' to exit covert ops
These are merely trigger words and may be used in a sentence.
    """
    try:

        prompt = input(agent)
        if 'butler' in prompt:
            ranger()

        elif 'recon' in prompt:
            recon()

        elif 'strack' in prompt:
            fasttrack()

        elif 'tracker' in prompt:
            locate()

        elif 'study' in prompt:
            print(header)
            lessons()

        elif 'help' in prompt:
            print(header)
            sprint(covertControl.__doc__)
            covertControl()

        elif 'exit' in prompt:
            O();sprint("Over and out.")
            print(Fore.LIGHTBLACK_EX+beam+Fore.WHITE)
            reception()
            return

        else:
            O();sprint("'"+prompt+"'"+'is an unrecognized command')
            covertControl()

    except KeyboardInterrupt as e:
        print("\n")
        O();sprint("Over and out.")
        print(Fore.LIGHTBLACK_EX+beam+Fore.WHITE)
        reception()
        return

    except Exception as e:
        O();sprint('\n'+e)
        covertControl()


def check_web_sever(host, port, path):
    try:
        h = http.client.HTTPConnection(host, port)
        h.request('GET',path)
        resp = h.getresponse()
        sprint('HTTP Response:')
        print('    status = ',resp.status)
        print('    reason = ',resp.reason)
        sprint('HTTP Headers:')
        for hdr in resp.getheaders():
            sprint('    %s: %s' % hdr)
        covertControl()
    except Exception as e:
        O();sprint('\n'+str(e))
        covertControl()

"""
# parallel thread that changes mac address every 30 minutes
def machanic():
    os.system('sudo macchanger -r eno1')
    os.system('sudo macchanger -r lo')
    os.system('sudo macchanger -r wlp3s0')
    time.sleep(1800)
    machanic()
"""

def recon():
    host_info = []

    O();sprint("Enter target host")
    prompt = input(agent)
    host_info.append(prompt)

    O();sprint("Enter target port")
    prompt2 = input(agent)
    host_info.append(str(prompt2))

    O();sprint("Enter target path")
    prompt3 = input(agent)
    host_info.append(prompt3)
    check_web_sever(prompt, prompt2, prompt3)


def ranger():
    try:
        O();sprint("Extract target name or target IP?")
        prompt = input(agent)
        if 'name' in prompt:
            O();sprint("Enter target ip")
            prmpt = input(agent)
            try:
                b = socket.gethostbyaddr(prmpt)
                sprint(str(b))
                covertControl()
            except Exception as e:
                sprint(str(e))
                covertControl()
        elif 'ip' in prompt:
            O();sprint("Enter target address")
            prom = input(agent)
            try:
                d = socket.gethostbyname(prom)
                sprint(str(d))
                covertControl()
            except Exception as e:
                O();sprint(e)
                covertControl()
        else:
            O();sprint("Invalid input.")
            time.sleep(2)
            ranger()
    except Exception as e:
        O();sprint('Negative contact')
        covertControl()


def locate():
    O();sprint("Enter target IP")
    prompt = input(agent)
    ip = prompt
    try:
        url = 'http://freegeoip.net/json/' + ip
        r = requests.get(url)
        js = r.json()
        print(header)
        for key,value in js.items():
            sprint('{} : {}'.format(key, value))
        covertControl()
    except Exception as e:
        O();sprint("Negative contact.")
        covertControl()

# TODO:create curl file downloader.
# assisted by google library. find and download files with a specific format

def exploit_port():
    """A portal to adding and viewing exploits.
    I'll seek to make it more secure"""
    try:
        H(); sprint("Label your exploit:")
        title = input(uzer)

    except KeyboardInterrupt as e:
        Hplus(); sprint("Aborted.")
        controlCentre()

    inputFile = open("temp.txt", "w")
    inputFile.write("Exploiteria:\n")
    inputFile.close()
    os.system("nano temp.txt")
    file = open("temp.txt", "r")
    Rfile = file.read()
    H(); sprint("Extracted this from file: %s" % Rfile[:20]+"...")
    entry = {
              '_id': str(uuid.uuid4()),
              'title': title,
              'payload': Rfile,
              'datetime': str(datetime.datetime.now())
            }
    hades.insert_one(entry)
    H(); sprint("Exploit saved")
    os.remove("temp.txt")
    controlCentre()

# Advanced traceroute implementation.
collector = []

def traceroutePlus(cmd):
    start1 = cmd.find(' ')+1
    H(); sprint('running trace...')
    os.system('traceroute %s | tee result.txt' % cmd[start1:])
    H(); sprint("processing... I'll get you what I can.")
    f = open('result.txt', 'r')
    ff = f.read()
    ipextractor(ff)
    locate2()
    collector.clear()
    os.remove('result.txt')
    controlCentre()


def ipextractor(trstring):
    try:
        start = trstring.find('\n')+7
        seg = trstring[start:]
        if seg[1] != '*':
            end = seg.find(' ')
            collector.append(seg[:end])
            ipextractor(seg[end:])
        else:
            print('bummer')
    except:
        pass


def locate2():
    for ip in collector:
        try:
            url = 'http://freegeoip.net/json/' + ip
            r = requests.get(url)
            js = r.json()
            print('%s %s, %s, %s, lat: %s, lon: %s' % (ip, js['city'], js['region_name'],
                                                       js['country_name'], js['latitude'],
                                                       js['longitude']))
        except Exception as e:
            pass


def fasttrack():
    O();sprint("Enter target url")
    prmpt = input(agent)
    try:
        ip = socket.gethostbyname(prmpt)
        url = 'http://freegeoip.net/json/' + ip
        r = requests.get(url)
        js = r.json()
        for key,value in js.items():
            sprint('{} : {}'.format(key,value))
        covertControl()
    except Exception as e:
        O();sprint('\n'+e)
        covertControl()


def lessons():
    """Greetings grasshopper.

    Well done on embarking on this journey of discovery.
    Hopefully you master the patience and wisdom necessary.

    In case you've been struggling with recon target ports,
        common ports are 21,22,25,80,110, and 443
           with a special emphasis on port 80...

    Besides that, all roads lead back to the control centre.

    This is a reconanaisance program. Do not abuse it. nor expect heaven
    and earth from it.

    Happy scouting.
    """
    sprint(lessons.__doc__)
    covertControl()


def port_1():
    try:
        hh.append(uzer)
        H(); sprint('Enter code name')
        cn = input(uzer)
        H(); sprint('Enter text')
        txt = input(uzer)
        save_in_db(cn, txt)
    except KeyboardInterrupt as e:
        print('Aborted.')
        controlCentre()


def save_in_db(code_name, obj):
    entry = {
             '_id': str(uuid.uuid4()),
             'code_name': code_name,
             'date': str(datetime.datetime.now()),
             'payload': [obj]
    }
    files.insert_one(entry)
    H();sprint("New file stored successfully.")
    controlCentre()

def find_all():
    membrane = []
    for file in files.find():
        membrane.append(file)
    return membrane


# nmap extension
translator = {'-A': ['-A', 'enable os detection'],
              '-v':['-v', 'verbosity level 1', 'verbosity 1']}


"""
host_handler():
    q1 = input('Would like to add or remove a host to the black list?')
    if 'add' in q1:
        #under construction
"""


def dictionary():
    try:
        H(); print("Choose a dictionary database (enter the associated number)\n\n",
             "1. The Collaborative International Dictionary of English\n",
             "2. Wordnet (2006)\n",
             "3. The Devil's Dictionary (1881-1906)\n",
             "4. The Moby Thesaurus II by Grady Ward")
        dic = input(uzer)
        mapper = {'1': 'gcide', '2': 'wn', '3': 'devil', '4': 'moby-thesaurus'}
        mapper2 = {'1': 'The Collaborative International Dictionary of English',
                   '2': 'Wordnet (2006)',
                   '3': "The Devil's Dictionary (1881-1906)",
                   '4': 'The Moby Thesaurus II by Grady Ward'}
        H(); sprint("You are now in %s" % mapper2[dic])
        dictionaryHelper(mapper[dic])
    except KeyboardInterrupt:
        H(); sprint('Aborted')
        controlCentre()


def dictionaryHelper(dictionary):
    word = input(uzer)
    if word != 'exit':
        try:
            H(); os.system('dict -d %s %s' % (dictionary, word))
            dictionaryHelper(dictionary)
        except Exception as e:
            H(); sprint(e)
            controlCentre()
    else:
        H(); sprint('You have left dictionary cyberspace.')
        controlCentre()


def intent_and_entity_rerouter(text):
    THRESHOLD = 0.75
    nlu_response = interpreter.parse(text)
    logging.debug('nlu recieved text: %s' % text)
    logging.debug('nlu response: %s' % nlu_response)
    if nlu_response['intent']['confidence'] >= THRESHOLD:
        logging.info('text has gotten through threshold')
        intent = nlu_response['intent']['name']
        entities = nlu_response['entities']
        if intent == 'get_weather':
            logging.info('text has found to be weather. running weather()')
            if entities:
                weather(False, False, *[entities[0]['value']])
            else:
                weather()
        elif intent == 'find_info':
            evaluate_subject(entities, text) # if subject does not exist, right of execution is passed to controlCentre()
            # TODO: consider how to make images and local lookup optional
            informant(entities[0]['value'].title(), True, 0, False) 
        elif intent == 'find_images':
            threading.Thread(target=imageShow, args=(entities[0]['value'], 5,)).start()
            H(); sprint(random.choice(imdi))
            controlCentre()
        elif intent == 'find_related_info':
            evaluate_subject(entities, text)
            find_related(entities[0]['value'])
        else:
            if intent == 'find_more_info':
                evaluate_subject(entities, text)
                informant(entities[0]['value'].title(), False, 0, True)
    else:
        controlCentre(*[text])


def evaluate_subject(entities, text):
    """if entities is empty the user is notified and right of execution is passed
       to controlCentre. Else right of execution is returned to the caller.
    """
    if entities == []:
        logging.debug('No subject specified.')
        controlCentre(*[text])
    else:
        return


def controlCentre(*s):
    if s:
        prompt = s[0]
        # rootLogger.debug('prompt is %s' % prompt)

    else:
        prompt = input(uzer).lower()
        intent_and_entity_rerouter(prompt)

    try:
        global listed_db

        if prompt == 'help':
            help_center()

        elif (prompt.startswith('what is the distance between ') or prompt.startswith('distance between')):
            end = prompt.find(' and ')
            start = prompt.find(' between ')
            x = prompt[start+9:end]
            y = prompt[end+5:]
            groundDistance(x,y)

        elif 'resource' in prompt:
            findExternalResource()

        elif prompt == 'archives':
            # TODO: replace implementation to: set listed_db to 'arch' then call confessional()
            if arch.count() > 0:
                print('')
                for file in arch.find():
                    print(file['title'])
                    time.sleep(0.1)
            else:
                H(); sprint('No files have been archived.')
            controlCentre()

        elif prompt == 'translator':
            init_translator()

        elif prompt == 'search quotes':
            quote_search()

        elif prompt == 'clear':
            os.system('clear')
            controlCentre()

        elif prompt.startswith('play me some '):
            media_player(prompt[13:])

        elif prompt == 'load full database':
            listed_db = intel
            H(); sprint('Full database loaded for preview.')
            controlCentre()

        elif prompt == 'load partial database':
            listed_db = sci
            H(); sprint('Database preview has been refined with scientific bias.')
            controlCentre()

        elif prompt == 'data stats':
            H(); sprint('Listing database item counts\n')
            sprint('intel : %s' % intel.count())
            sprint('files : %s' % files.count())
            sprint('sci-db: %s' % sci.count())
            controlCentre()

        elif prompt.startswith('how do i pronounce'):
            try:
                transformed = num_word_transform.number_to_words(prompt[19:])
                H(); sprint(transformed)
                controlCentre()
            except Exception as e:
                H(); sprint(str(e))
                controlCentre()
        elif 'reading list' in prompt:
            suggested_reading()
            controlCentre()

        elif prompt == 'banner':
            banners = ['db_banner2.py'] # for future: add other banners here
            os.system('python3 ./resources/banners/%s' % random.choice(banners))
            controlCentre()

        elif prompt.startswith('find the') and 'root' in prompt:
            find_root(prompt)

        elif prompt == 'tell me everything you know':
            confessional()

        elif prompt.startswith('how important is '):
            start = prompt.find(' is ')
            entity = prompt[start+4:]
            gridWeight(entity)

        elif 'note' in prompt:
            port_1()

        elif prompt == 'open pandora':
            confessional(*['thefuturebelongstothosewhotakeit'])

        # save exploit
        elif prompt == 'auriga':
            exploit_port()

        elif prompt == 'growth point':
            gen_gate()

        elif 'population density' in prompt:
            pop_dense()

        elif 'terminal' in prompt:
            H(); sprint('Terminal open.')
            terminal_session()

        elif prompt == 'clean swap':
            print(''); os.system('sudo swapoff -a && sudo swapon -a')
            H(); sprint('swap cleansed.')
            controlCentre()

        elif prompt == 'clean db':
            clean_db(False)

        elif 'network diagnostic' in prompt or prompt == 'netdog':
            print('')
            os.system('sudo nmcli radio wifi off')
            rootLogger.debug('Turning wifi off.')
            os.system('nmcli radio wifi on')
            rootLogger.debug('Turning wifi on.')
            os.system('sudo service network-manager restart')
            rootLogger.debug('Restarting network manager.')
            H(); sprint('Diagnosis complete. Counter-measures deployed.')
            controlCentre()

        elif 'all systems shutdown' in prompt:

            if 'FRTNX' in user:

                try:

                    os.system('sudo shutdown now')

                except KeyboardInterrupt:
                    controlCentre()

                except Exception as e:
                    H();print(e)
                    controlCentre()

            else:
                H();sprint(random.choice(DoA))
                controlCentre()

        elif prompt.startswith('convert'):
            converter(prompt)

        elif 'reboot all systems' in prompt:

            if 'FRTNX' in user:

                try:

                    os.system('sudo reboot now')

                except KeyboardInterrupt:
                    controlCentre()

                except Exception as e:
                    H();print(e)
                    controlCentre()

            else:
                H();sprint(random.choice(DoA))
                controlCentre()

        elif prompt == 'port':
            porter()

        elif prompt.startswith('how do i get to '):
            directions(prompt[16:])

        elif prompt.startswith('show me all '):
            nearby(prompt[12:])

        elif prompt == 'save state':
            backup_manager(*[999])

        elif prompt.startswith('dict'):
            dictionary()

        elif prompt == 'faster' or prompt == 'slower':
            dialogue_speed_manager(prompt)
            controlCentre()
            return

        elif prompt == "whats in the papers":
            lightIntel()
            return

        elif "reading list" in prompt:
            suggested_reading()

        elif 'todo list' in prompt:
            file = open('TODO.txt', 'r')
            ff = file.read()
            print(ff)
            controlCentre()

        elif prompt.startswith('traceroute'):
            traceroutePlus(prompt)

        elif prompt == 'code finder':
            code_search()

        elif 'fibonacci' in prompt:
            laFibonacci()

        elif 'in vivo veritas' in prompt:

            if 'FRTNX' not in user:
                H();sprint(random.choice(DoA))
                alert(user[0])
                TimeOut()

            else:
                auth = getpass.getpass()

                if auth == os.getenv('SHADOW'):
                    Engage()

                else:
                    print('Access Denied')
                    controlCentre()

        elif 'koan' in prompt:
            zen()

        elif prompt == 'history':
            print('')
            os.system('sudo python3 herodotus.py')
            controlCentre()

        elif 'exit' in prompt:
            user.clear()
            H();sprint(random.choice(bye))
            switch.clear()
            rootLogger.warn('shutting down...')
            return ''

        else:
            H();sprint(k.respond(prompt))
            store_session_data(prompt)
            controlCentre()

    except KeyboardInterrupt as e:
        user.clear()
        print('\n')
        H();sprint(random.choice(bye))
        switch.clear()
        rootLogger.warn('shutting down...')
        return ''

    except Exception as e:
        H();print(e)
        controlCentre()

for city in climate_monitor:
    threading.Thread(target=weather, args=(True, False, city,)).start()
threading.Thread(target=clean_db, args=(True,)).start()
suggested_reading()
Hello()
