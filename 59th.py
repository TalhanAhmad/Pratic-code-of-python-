with open("log.html")as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yesh python is present...line no:{lineno}")
        break
    lineno += 1

else:
    print("no its not present in the file")    
    
