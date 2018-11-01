

class Introduction(Object):

    def __init__(self):
        return


    def run(self):
        try:
            time.sleep(1.5)
            user_name = input("\n                                              Code Name:")
            #users = get_known_users()
    
            if user_name == os.getenv("PRIUSER"):
                user.append(user_name)
                uheader = '\n['+Fore.LIGHTBLACK_EX+user[0].upper()+Fore.WHITE+'] '
                uzer = uheader
                hh.append(uheader)
                time.sleep(1)
                H();sprint("%scommander." % timemaster())
                """elif user_name.lower() in users:
                try:
                    H();sprint(random.choice(recall)+" "+user_name+".")
                except:
                    pass"""
            else:
                user.append(user_name)
                uheader = '\n['+Fore.LIGHTBLACK_EX+user[0].upper()+Fore.WHITE+'] '
                uzer = uheader
                #users.append(gate.lower())
                #save_new_user(users)
                time.sleep(1)
                H(); sprint("%s%s. My name is Luna. Luna Moonchild." % (timemaster(),user_name.title()))
    
            k.setPredicate("name", user_name)
            rootLogger.info('User identified as %s' % user_name)
            controlCentre()
    
        except KeyboardInterrupt as e:
            rootLogger.debug('shutting down...')
            return