class clsStringutil(object):

    def __init__(self, filename):
        self.filename = filename

    def Get_Ext(self):
        if self.filename.rfind('.') != -1:
            return self.filename[self.filename.rfind('.') + 1:]
        else:
            return self.filename

    def Get_FileName(self):
        if self.filename.rfind('\\') != -1:
            return self.filename[self.filename.rfind('\\') + 1:]
        else:
            return self.filename

    def Get_OnlyFileName(self):
        index1 = self.filename.rfind('\\')
        if index1 == -1:
            return ""

        index2 = self.filename.rfind('.')
        if index2 == -1:
            return ""

        return self.filename[index1 + 1:index2]


if __name__ == '__main__':
    clsobj = clsStringutil('E:\\Util\\python\\python.png')
    print("Get_Ext: " + clsobj.Get_Ext())
    print("Get_FileName: " + clsobj.Get_FileName())
    print("Get_OnlyFileName: " + clsobj.Get_OnlyFileName())
    pass
