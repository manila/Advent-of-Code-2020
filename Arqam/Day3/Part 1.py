f=open('file3.txt','r')
s=[]
for i in f:
    s.append(str(i))
a=b=i=X=0
while b==0:
    if a>27:
        a=a-30-1
    a+=3
    i+=1
    if s[i][a]=='#':
        X+=1
    if len(s)-1==i:
        b=1
print(X)

        
    
    
