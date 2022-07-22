def f(n):
    s=str(bin(n)[2::])
    if n%2==0:
        s=s+'10'
    else:
        s=s+'11'
    return int(s,2)
cnt=0
for i in range (1,300):
    if f(i)>50 and f(i)<176:
         cnt+=1
print(cnt)    
