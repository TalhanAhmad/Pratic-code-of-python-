class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary = salary
        self.pin = pin


p = Programmer("talha","1200 USD",245001)
        
print(p.name,p.salary,p.pin,)
r = Programmer("rohan","1200 USD",245001)
print(r.name,r.salary,r.pin,)