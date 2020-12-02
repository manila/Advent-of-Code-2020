f = open("file1.txt", "r")
l=[]
for x in f:
    l.append(int(x))
for i in range(0,len(l)-1):
    a=l[i]
    for k in range(i+1,len(l)-1):
        b=l[k]
        if a+b==2020:
            print('Product-->',a*b)
