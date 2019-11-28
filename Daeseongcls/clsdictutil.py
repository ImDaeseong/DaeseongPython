class clsdictutil(object):

    def __init__(self):
        self.dic = {}

    def GetWordsList(self):
        # print(list(self.dic.keys()))
        # print(list(self.dic.values()))
        for key in self.dic:
            val = self.dic[key]
            print("%s : %s" % (key, val))

    def IsDictionary(self, key):
        return self.dic.get(key)

    def RemoveWords(self, key):
        if self.IsDictionary(key):
            del self.dic[key]

    def AddWords(self, key, val):
        self.dic[key] = val

    def UpdateWords(self, key, val):
        self.dic[key] = val


if __name__ == '__main__':
    clsobj = clsdictutil()
    clsobj.AddWords('lipas', '바퀴벌레')
    clsobj.AddWords('muram', '우울한우울한')
    clsobj.AddWords('persaingan', '경쟁')
    clsobj.AddWords('rawit', '작은')
    # clsobj.GetWordsList()
    clsobj.RemoveWords('lipas')
    clsobj.AddWords('tikung', '커브길')
    clsobj.UpdateWords('muram', '우울한')
    clsobj.GetWordsList()
    pass
