import re

def getTotal(file):
    if file.closed == True:
        raise ValueError('database must be open')
    lines = file.readlines()
    total = 0
    for i in lines:
        i = i.replace("\n","")
        if(i != ""):
            if i.lstrip('+-').isdigit():
                total += int(i)
            else:
                raise ValueError('all values must be digits')
    file.writelines('\n' + str(total))


# f = open("Integers.txt","r+")
# getTotal(f)
# f.close()
# f = open("Integers.txt","r+")
# print(f.readlines())
# f.close()
