fname = input('Enter file name: ')
#fname = 'mbox-short.txt'
fh = open(fname)

count = 0
for lines in fh :
    if 'From:' not in lines :
        if lines.startswith('From') :
            lines = lines.strip().split()
            lines = lines[1]
            count = count + 1
            print(lines)
print('There were', count, 'lines in the file with From as the first word')
