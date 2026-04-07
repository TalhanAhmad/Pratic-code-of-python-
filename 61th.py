with open("file2.txt")as f:
    content1 = f.read()

with open("file3.txt")as f:
    content2 = f.read()

if(content1 in content2):
    print("the files have teh similar data")
else:
    print("no similar data found")        