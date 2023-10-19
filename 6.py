def isphone(txt):
    if len(txt)!=12:
        return False
    for i in range(0,3):
        if not txt[i].isdigit():
            return False
    if txt[3]!='-':
        return False
    for i in range(4,7):
        if not txt[i].isdigit():
            return False
    if txt[7]!='-':
        return False
    for i in range(8,12):
        if not txt[i].isdigit():
            return False
    return True
x=input("Enter the input:")
print(isphone(x))