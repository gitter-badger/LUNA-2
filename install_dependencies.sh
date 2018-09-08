#!/bin/sh

sudo apt-get -y install python3-pip
pip install conda
conda create -y --name luna python=3.6
source activate luna
sudo apt-get update
# sudo apt-get upgrade
sudo apt install whois
sudo apt-get install wget
sudo apt-get install traceroute
sudo apt-get install macchanger macchanger-gtk
sudo apt-get install xbacklight
sudo apt install speedtest-cli speedtest-cli
sudo apt-get install htop
wget --max-redirect=20 -O db.zip https://www.dropbox.com/s/aqqcevbmz7kxy4x/std_db.zip?dl=0
unzip db.zip
rm db.zip

if hash dict; then 
    echo "Secondary database is already installed"
else
    sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
    sudo apt-get update
    sudo apt-get install dict
    sudo apt-get install dictd
    sudo apt-get install dict-gcide
    sudo apt-get install dict-wn 
    sudo apt-get install dict-devil
    sudo apt-get install dict-moby-thesaurus
fi

# install mongodb, if absent
if hash mongod; then
    echo "Primary database is already installed"
else
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    sudo apt-get update
    sudo apt-get install -y mongodb-org
    sudo systemctl start mongod
    # sudo systemctl status mongod
    sudo systemctl enable mongod
fi

pip install --upgrade pip
pip install pillow
pip install lxml
pip install google
pip install googletrans
pip install aiml
pip install pymongo
pip install geocoder
pip install twython
pip install bs4
pip install ipgetter
pip install colorama
pip install wikipedia
pip install ipgetter
pip install colorama
pip install nltk
pip install geopy==1.11.0
pip install google_images_download
pip install inflect


# finally copy the nltk folder into host machines home dir

# golang for go-based services

# javac for java-based services

# install metasploit framework
# curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
#  chmod 755 msfinstall && \
#  ./msfinstall

# install set
# sudo apt-get install git
#git clone https://github.com/trustedsec/social-engineer-toolkit/ set/

# run these commands manually:
# cd set
# python setup.py install

# theHarvester... install via ptf, which in turn ships with Luna zip file


# Katoolin
# git clone https://github.com/LionSec/katoolin.git && sudo cp katoolin/katoolin.py /usr/bin/katoolin
# sudo chmod +x /usr/bin/katoolin 
# thats all you need. Run it with: 'sudo katoolin'
