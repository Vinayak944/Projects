name = input("Enter the file name:")
han = open(name)
count = dict()
for line in han:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
bigcount = None
bigword = None
for word,counts in count.items():
    if bigcount is None or counts > bigcount:
        bigcount = counts
        bigword = word
print(bigword, bigcount)