import os
import shutil

class clsfiledutil:
    def __init__(self):
        pass

    def isDir(self, path):
        if not os.path.isdir(path):
            return False
        else:
            return True

    def isFile(self, path):
        if not os.path.exists(path):
            return False
        else:
            return True

    def IsDirExist(self, path):
        if not os.path.exists(path):
            return False
        else:
            return True

    def GetFilePath(self, path):
        return os.path.dirname(path)

    def GetFileName(self, path):
        return os.path.basename(path)

    def DeleteFile(self, path):
        if not self.IsDirExist(path):
            return

        if self.isDir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    def ReadLineFile(self, path):
        f = open(path, 'r')
        lines = f.readlines()

        count = 0
        for line in lines:
            count = count + 1
            print("번호:{0}, 내용:{1}".format(count, line))
        f.close()

    def FindFileList(self, path):
        fileList = []
        for root, subFolders, files in os.walk(path):
            for f in files:
                if self.isFile(root + os.sep + f):
                    fileList.append(root + os.sep + f)
                    # fileList.append(print("{0}\\{1}".format(root, f)))
        return fileList

    def FindDirList(self, path):
        dirList = []
        for root, subFolders, files in os.walk(path):
            dirList.append(root)
        return dirList


if __name__ == '__main__':

    clsobj = clsfiledutil()
    #print(clsobj.isDir('E:\\test'))
    #print(clsobj.isFile('E:\\DaeseongPython\\main.py'))
    #print(clsobj.IsDirExist('E:\\test'))
    #print(clsobj.IsDirExist('E:\\DaeseongPython\\main.py'))
    #print(clsobj.GetFilePath('E:\\DaeseongPython\\afdasdf\\main.py'))
    #print(clsobj.GetFileName('E:\\DaeseongPython\\afdasdf\\main.py'))
    #clsobj.DeleteFile('E:\\liteidex30.3.windows-qt5.zip')
    #clsobj.DeleteFile('E:\\a')
    #clsobj.ReadLineFile('E:\\a.txt')

    """
    FileList = clsobj.FindFileList('E:\\a')
    # print(len(FileList))
    for i in range(len(FileList)):
        print(FileList[i])
    """

    dirList = clsobj.FindDirList('E:\\a')
    for dir in dirList:
        print(dir)
    pass
