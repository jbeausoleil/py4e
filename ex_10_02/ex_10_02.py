#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input('Enter file: ')
#fname = 'mbox-short.txt'
if len(fname) < 1 : name = 'mbox-short.txt'
fh = open(fname)

hours = dict()
for lines in fh :
    lines = lines.strip()
    words = lines.split()
    if len(words) < 1 or words[0]!='From' : continue
    time = words[5][:2]
    hours[time] = hours.get(time,0) + 1
    sorted([(k,v) for k,v in hours.items()])
for k, v in sorted(hours.items()) :
    print(k, v)
