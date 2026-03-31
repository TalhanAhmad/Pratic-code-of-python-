

def f_into_c(f):
    return 5*(f-32)/9
f = int(input("enter the temperatur :"))    
c = f_into_c(f)
print(f"{round(c,2)} degree c")