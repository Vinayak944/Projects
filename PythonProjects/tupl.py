name = input("Enter the file name:")
han = open(name)
counts = dict()
for line in han:
    words = line.split()
    for word in words:
        #word = words.split()
        counts[word] = counts.get(word,0) + 1
temp = list()
for k,v in counts.items():
    newdic = (v, k)
    temp.append(newdic)
temp = sorted(temp, reverse=True)
for v,k in temp[:10]:
    print(v, k)
#print(counts.items())