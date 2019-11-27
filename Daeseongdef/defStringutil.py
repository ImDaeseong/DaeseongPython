def GetExt(filename):
    if filename.rfind('.') != -1:
        return filename[filename.rfind('.') + 1:]
    else:
        return filename


def GetFileName(filename):
    if filename.rfind('\\') != -1:
        return filename[filename.rfind('\\') + 1:]
    else:
        return filename


def GetOnlyFileName(filename):
    index1 = filename.rfind('\\')
    if index1 == -1:
        return ""

    index2 = filename.rfind('.')
    if index2 == -1:
        return ""

    return filename[index1+1:index2]


if __name__ == '__main__':
    print("GetExt: " + GetExt('E:\\Util\\python\\python.png'))
    print("GetFileName: " + GetFileName('E:\\Util\\python\\python-3.8.0.png'))
    print("GetOnlyFileName: " + GetOnlyFileName('E:\\Util\\python\\python-3.8.0.png'))
    pass
