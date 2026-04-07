# remane the old one text  by python to remaned one


with open("old.txt")as f:
    content = f.read()


with open("renamed_by_python.txt","w")as f:
    f.write(content)    