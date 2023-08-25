import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
#python urllinks.py
#Enter - http://www.dr-chuck.com/pagel.htm
#http://www.dr-chuck.com/page2.htm