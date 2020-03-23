def read(fileName, fileExtention, fileEncoding=None):
    if fileEncoding is None:
        fileEncoding = "UTF-8"
    with open("{}.{}".format(fileName, fileExtention), "r", encoding="{}".format(fileEncoding)) as a:
        a.read()


def write(fileName, fileExtention, fileContents, fileEncoding=None):
    if fileEncoding is None:
        fileEncoding = "UTF-8"
    with open("{}.{}".format(fileName, fileExtention), "w", encoding="{}".format(fileEncoding)) as a:
        a.write(fileContents)


def readWrite(fileName, fileExtention, fileContents, fileEncoding=None):
    if fileEncoding is None:
        fileEncoding = "UTF-8"
    with open("{}.{}".format(fileName, fileExtention), "+", encoding="{}".format(fileEncoding)) as a:
        a.write(fileContents)


def append(fileName, fileExtention, fileContents, fileEncoding=None):
    if fileEncoding is None:
        fileEncoding = "UTF-8"
    with open("{}.{}".format(fileName, fileExtention), "a", encoding="{}".format(fileEncoding)) as a:
        a.write(fileContents)
