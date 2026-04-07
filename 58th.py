with open("log.html")as f:
    content = f.read()
if("python" in content):
    print("present")
else:
    print("not present")        