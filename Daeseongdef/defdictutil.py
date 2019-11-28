dic = {}


def GetWordsList():
    # print(list(dic.keys()))
    # print(list(dic.values()))
    for key in dic:
        val = dic[key]
        print("%s : %s" % (key, val))


def IsDictionary(key):
    return dic.get(key)


def RemoveWords(key):
    if IsDictionary(key):
        del dic[key]


def AddWords(key, val):
    if not IsDictionary(key):
        dic[key] = val


def UpdateWords(key, val):
    dic[key] = val


if __name__ == '__main__':
    AddWords('lipas', '바퀴벌레')
    AddWords('muram', '우울한우울한')
    AddWords('persaingan', '경쟁')
    AddWords('rawit', '작은')
    # GetWordsList()
    RemoveWords('lipas')
    AddWords('tikung', '커브길')
    UpdateWords('muram', '우울한')
    GetWordsList()
    pass
