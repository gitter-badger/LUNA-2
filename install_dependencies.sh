#!/bin/sh

sudo apt-get update
sudo apt-get -y install build-essential
sudo apt-get -y install python3-setuptools
sudo apt-get -y install python3-pip
pip3 install conda
conda create -y --name luna python=3.6
source activate luna
sudo apt-get update
# sudo apt-get upgrade
sudo apt install whois
sudo apt-get -y install wget
sudo apt-get -y install traceroute
sudo apt-get -y install macchanger macchanger-gtk
sudo apt-get -y install xbacklight
sudo apt -y install speedtest-cli speedtest-cli
sudo apt-get -y install htop
wget --max-redirect=20 -O db.zip https://www.dropbox.com/s/aqqcevbmz7kxy4x/std_db.zip?dl=0
unzip db.zip
rm db.zip

if hash dict; then
    echo "Secondary database is already installed"
else
    sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
    sudo apt-get update
    sudo apt-get -y install dict
    sudo apt-get -y install dictd
    sudo apt-get -y install dict-gcide
    sudo apt-get -y install dict-wn
    sudo apt-get -y install dict-devil
    sudo apt-get -y install dict-moby-thesaurus
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

pip3 install pillow --user
pip3 install lxml --user
pip3 install google --user
pip3 install googletrans --user
pip3 install aiml --user
pip3 install pymongo --user
pip3 install geocoder --user
pip3 install twython --user
pip3 install bs4 --user
pip3 install ipgetter --user
pip3 install colorama --user
pip3 install wikipedia --user
pip3 install ipgetter --user
pip3 install colorama --user
pip3 install nltk --user
pip3 install geopy==1.11.0 --user
pip3 install google_images_download --user
pip3 install inflect --user --user
pip3 install rasa-nlu==0.13.7
pip3 install tensorflow --user
pip3 install sklearn --user
pip3 install sklearn-crfsuite --user
pip3 install scipy --user


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
