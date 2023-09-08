fh = open('py4e.com_code3_mbox-short.txt')
w = list()
for line in fh:
    line = line.rstrip()
    w = line.split()
    #print('IGNORE', w)
    if len(w) < 3 or not line.startswith('From') : continue
    #if len(w) < 3:
     #   continue
    print(w[2])
#for i in fh:
#    j = i.rstrip()
 #   print()

#print(fh.read(10))