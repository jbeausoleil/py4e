import re

#fname = ('Enter File Name: ')
#fname = 'regex_sum_42.txt'
fname = 'regex_sum_183152.txt'
fh = open(fname)

inumbers = 0

for lines in fh :
    lines = lines.strip()
    snumbers = re.findall('[0-9]+', lines)
    if len(snumbers) > 0 :
        #print(snumbers)
        for inumber in snumbers :
            inumbers = int(inumber) + inumbers
            #print(inumbers)
