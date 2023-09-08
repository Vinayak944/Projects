i = 5
while i > 0:
    s = ""
    j = i
    while j > 0:
        s = s + '*'
        j = j - 1
    i = i - 1
    print(s)