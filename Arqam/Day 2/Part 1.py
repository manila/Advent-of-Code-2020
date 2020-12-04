x=0
f=open('file2.txt','r')
for s in f:
    s=s.split(': ')
    a=str(s[0][-1])
    s[0]=s[0][:-2]
    b=s[0].split('-')
    s.pop(0)
    cnt= s[0].count(a)
    if cnt>=int(b[0]) and cnt<=int(b[1]):
        x+=1
print('count-->',x)
f.close()



