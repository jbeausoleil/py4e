fname = input('Enter file name: ')
fh = open(fname)
count = 0
scfind = 0

for line in fh :
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    cfind = float(line[line.find(':')+1:].strip())
    scfind = cfind + scfind
    #print(scfind)
    count = count + 1
    #print(line)
print('Average spam confidence:', scfind/count)
