f=open('file3.txt','r')
s=[]
for i in f:
    s.append(str(i))
a=b=i=X1=X2=X3=X4=X5=0
while b==0:
    if a==30:
        a=-1
    a+=1
    i+=1
    if s[i][a]=='#':
        X1+=1
    if len(s)-1==i:
        b=1
print(X1)
a=i=0
while b==1:
    if a>27:
        a=a-30-1
    a+=3
    i+=1
    if s[i][a]=='#':
        X2+=1
    if len(s)-1==i:
        b=2
print(X2)
a=i=0
while b==2:
    if a>25:
        a=a-30-1
    a+=5
    i+=1
    if s[i][a]=='#':
        X3+=1
    if len(s)-1==i:
        b=3
print(X3)
a=i=0
while b==3:
    if a>23:
        a=a-30-1
    a+=7
    i+=1
    if s[i][a]=='#':
        X4+=1
    if len(s)-1==i:
        b=4
print(X4)
a=i=0
while b==4:
    if a==30:
        a=-1
    a+=1
    i+=2
    if s[i][a]=='#':
        X5+=1
    if len(s)-1==i:
        b=5
print(X5)
print('Product-->',X1*X2*X3*X4*X5)
        
