
a = 100
b = 45
c = 90

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c    


print(greatest(a,b,c))