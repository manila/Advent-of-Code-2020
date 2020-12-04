x=0
f=open('file2.txt','r')
for s in f:
    s=s.split(': ')
    a=str(s[0][-1])
    s[0]=s[0][:-2]
    b=s[0].split('-')
    s.pop(0)
    if s[0][int(b[0])-1]==a and s[0][int(b[1])-1]!=a:
        x+=1
    elif s[0][int(b[0])-1]!=a and s[0][int(b[1])-1]==a:
        x+=1
print('count-->',x)
f.close()


