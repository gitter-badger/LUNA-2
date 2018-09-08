f = open('logs/luna.log', 'r')
ff = f.read()
fff = ff.split('\n')
hist = []
consol = []

for e in fff:         
    if "user requested document " in e.lower():
        hist.append(e)

print('')

for i in hist:                
    start = i.find('"')                        
    chronicle = i[start:].replace('.','').replace('"','').strip()
    if chronicle not in consol:
    	del consol[:]
    	print(chronicle)
    	consol.append(chronicle)
