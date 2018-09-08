import random

yy1 = ['######', '######', '######', '######', '##  ##', '##  ##', '##  ##', '##  ##']
yy2 = ['######', '######', '######', '######', '##  ##', '##  ##', '##  ##', '##  ##']
yy3 = ['######', '######', '######', '######', '##  ##', '##  ##', '##  ##', '##  ##']

random.shuffle(yy1)
random.shuffle(yy2)
random.shuffle(yy3)
trigram = [yy1, yy2, yy3]

file = open('resources/banners/logs_banner1.txt', 'w')
file.write('\n\n')
for monogram in trigram:
    file.write('        %s  %s  %s  %s  %s  %s  %s  %s\n' % (monogram[0],
    	                                                     monogram[1],
    	                                                     monogram[2],
    	                                                     monogram[3],
    	                                                     monogram[4],
    	                                                     monogram[5],
    	                                                     monogram[6],
    	                                                     monogram[7]))
file.close()

# broken lines are yin (dark, earth, female)
# solid lines are yang (light, heaven, male)
