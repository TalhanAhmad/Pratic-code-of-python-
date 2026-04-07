f = open("poem.txt")
content = f.read()

if("twinkle" in content):
    print("the word is in the txt file")
else:
    print("the word is not present in the txt")    