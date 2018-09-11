import getpass
import os
import subprocess
from annoyances import rootLogger


def launcher():
    cwd = os.getcwd()
    conf = ['#!/bin/sh\n\n',
            '',
            'chmod +x luna.sh\n',
            'export EMAILPWD="OCO-2"\n',
            'export MYEMAIL="SHIZUKU"\n',
            'export LUNADDR="Aqua"\n',
            'export SHADOW="CALIPSO"\n',
            'export PRIUSER="Aura"\n',
            'git pull origin master &>> ./logs/luna.log\n',
            './luna.sh "$@"\n',]
    conf[1] = 'cd %s\n' % cwd
    if not os.path.isdir("/usr/local/bin/"):
        os.makedirs("/usr/local/bin/")
    filewrite = open("luna", "w")
    filewrite.write(''.join(conf))
    filewrite.close()
    os.system('sudo mv luna /usr/local/bin/luna')
    subprocess.Popen("sudo chmod +x /usr/local/bin/luna", shell=True).wait()
    rootLogger.info('successfully created launcher.')

launcher()
os.system('bash install_dependencies.sh')
os.system('luna')
"""
def pwd_manager():
    print('Enter the password for the email you created for the program ')
    emailpwd = getpass.getpass()
    print('Confirm password')
    emailpwd2 = getpass.getpass()
    if emailpwd == emailpwd2:
        return emailpwd
    else:
    	print('Passwords dont match. Try again.')
    	pwd_manager()

print('Welcome to the Luna setup wizard.\nBefore continuing please make to have created'+
	  ' a new gmail account and allowed access from less secure apps.'+
	  '\nNOTE:This is a crucial step so please make sure to get it right.\nNOTE:Mess this up and you may need to'+
	  ' do a complete reinstallation. No pressure.')
response = input("Enter 'yes' if you have completed this step. Enter 'no' to exit the setup wizard.\n[yes/no]: ")
if 'yes' in response.lower():
    try:
        primary_user = input('Choose a code name: ')
        email = input('Give the program the gmail account you created for it: ')
        pwd = pwd_manager()
        user_mail = input('Enter an email address you would like to recieve emails from the program from.\nyour email: ')
        print('code name: %s\nemail: %s\npassword: %s' % (primary_user, email, pwd))
        try:
            os.system('mkdir .access')
        except:
        	pass
        file = open('.access/keys', 'w')
        data = ['#!/bin/sh\n\nexport EMAILPWD="%s"\nexport MYEMAIL="%s"\nexport LUNADDR="%s"\nexport SHADOW="%s"\nexport PRIUSER="%s"\n' % (pwd, user_mail, email, pwd, primary_user)]
        print(data[0])
        file.write(data[0])
        file.close()
        print('Settings saved.')

    except Exception as e:
        print(str(e))
else:
	os.system('exit')
"""