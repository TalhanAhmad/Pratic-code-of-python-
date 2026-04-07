word = "not accetable content#"

with open("file2.txt" , "r")as f:
    content = f.read()

contentNew = content.replace(word,"Exclusive")

with open("file2.txt","w")as f:
    f.write(contentNew)
