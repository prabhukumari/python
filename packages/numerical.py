def isprime(n):
    flag=0
    c=0
    for i in range(1,n+1):
        if n%i==0:
            flag+=1
            c+=1
    if flag==2:
        return True
def factors(n):
    a=[]  
    for i in range(1,n+1):    
        if n%i==0:
            if isprime(i)==1:
                a.append(i)
    print(a)
    