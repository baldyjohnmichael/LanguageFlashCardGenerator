def getListFromFile(filePath):
    f = open(filePath, "r")
    list = []
    for line in f:
        list.append(line)
    f.close()
    return list

def appendToFile(filePath, str):
    f = open(filePath, "a")
    f.write(str)
    f.close()


