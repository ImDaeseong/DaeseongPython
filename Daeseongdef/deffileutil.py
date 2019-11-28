import os
import shutil


def isDir(path):
    if not os.path.isdir(path):
        return False
    else:
        return True


def isFile(path):
    if not os.path.exists(path):
        return False
    else:
        return True


def IsDirExist(path):
    if not os.path.exists(path):
        return False
    else:
        return True


def GetFilePath(path):
    return os.path.dirname(path)


def GetFileName(path):
    return os.path.basename(path)


def DeleteFile(path):
    if not IsDirExist(path):
        return

    if isDir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def ReadLineFile(path):
    f = open(path, 'r')
    lines = f.readlines()

    count = 0
    for line in lines:
        count = count + 1
        print("번호:{0}, 내용:{1}".format(count, line))
    f.close()


def FindFileList(path):
    fileList = []
    for root, subFolders, files in os.walk(path):
        for f in files:
            if isFile(root + os.sep + f):
                fileList.append(root + os.sep + f)
                # fileList.append(print("{0}\\{1}".format(root, f)))
    return fileList


def FindDirList(path):
    dirList = []
    for root, subFolders, files in os.walk(path):
        dirList.append(root)
    return dirList


if __name__ == '__main__':
    # print(isDir('E:\\test'))
    # print(isFile('E:\\DaeseongPython\\main.py'))
    # print(IsDirExist('E:\\test'))
    # print(IsDirExist('E:\\DaeseongPython\\main.py'))
    # print(GetFilePath('E:\\DaeseongPython\\afdasdf\\main.py'))
    # print(GetFileName('E:\\DaeseongPython\\afdasdf\\main.py'))
    # DeleteFile('E:\\liteidex30.3.windows-qt5.zip')
    # DeleteFile('E:\\a')
    # ReadLineFile('E:\\a.txt')

    FileList = FindFileList('E:\\a')
    # print(len(FileList))
    for i in range(len(FileList)):
        print(FileList[i])

    """
    dirList = FindDirList('E:\\a')
    for dir in dirList:
        print(dir)
    """
    pass
