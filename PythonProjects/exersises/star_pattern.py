n = int(input("Enter the number of patterns to print: "))
for i in range(n):
    #print("*" * (i+1))
    s = '' 
    for j in range(i+1):
        s= s+'*'
    print(s)
