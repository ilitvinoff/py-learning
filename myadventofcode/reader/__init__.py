def listFromFile(filePath):
    file = open(filePath, 'r')
    res = []
    for line in file:
        res.append(line)
    return res