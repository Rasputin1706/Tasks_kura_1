def f(n):
    s=str(bin(n)[2::])
    s='10'+s+'01'
    return int(s,2)
for i in range (1,100):
    if f(i)>800:
        print(i, f(i)) 
