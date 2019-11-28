from Daeseongdef.defStringutil import GetExt, GetFileName, GetOnlyFileName
from Daeseongcls.clsStringutil import clsStringutil
from Daeseongdef.defjsonutil import GetJson, WriteString, WriteJsonString
from Daeseongcls.clsjsonutil import clsjsonutil
from Daeseongdef.defdownloadutil import GetWebPage, GetDownloadFile
from Daeseongcls.clsdownloadutil import clsdownloadutil
from Daeseongdef.defdictutil import AddWords, GetWordsList, RemoveWords, UpdateWords
from Daeseongcls.clsdictutil import clsdictutil
from Daeseongdef.deffileutil import isDir, isFile, IsDirExist, GetFilePath, GetFileName, FindFileList, FindDirList, \
    DeleteFile, ReadLineFile
from Daeseongcls.clsfileutil import clsfiledutil
from Daeseongdef.defziputil import Zipfile, UnZipfile
from Daeseongcls.clsziputil import clsziputil
from Daeseongdef.defregistryutil import SetregistryString, GetregistryString, SetregistryDWord, GetregistryDWord, \
    DeleteKeyregistry, DeleteValueregistry, SetregistryStringWOW64, GetregistryStringWOW64, SetregistryDWordWOW64, \
    GetregistryDWordWOW64, DeleteValueregistryWOW64, SetregistryString32, GetregistryString32, SetregistryDWord32, \
    GetregistryDWord32, DeleteKeyregistry32, DeleteValueregistry32
from Daeseongcls.clsregistryutil import clsregistryutil


def func1():
    print("GetExt: " + GetExt('E:\\Util\\python\\python.png'))
    print("GetFileName: " + GetFileName('E:\\Util\\python\\python-3.8.0.png'))
    print("GetOnlyFileName: " + GetOnlyFileName('E:\\Util\\python\\python-3.8.0.png'))


def func2():
    strobj = clsStringutil('E:\\Util\\python\\python.png')
    print("Get_Ext: " + strobj.Get_Ext())
    print("Get_FileName: " + strobj.Get_FileName())
    print("Get_OnlyFileName: " + strobj.Get_OnlyFileName())


def func3():
    testdata = [
        {'id': '1', 'packagename': 'com.pearlabyss.blackdesertm', 'gametitle': '검은사막 모바일',
         'gamedesc': {'details1': '당신이 진짜로 원했던 모험의 시작', 'details2': '월드클래스 MMORPG “검은사막 모바일”'}},
        {'id': '2', 'packagename': 'com.kakaogames.moonlight', 'gametitle': '달빛조각사',
         'gamedesc': {'details1': "500만 구독자의 게임 판타지 대작 '달빛조각사'", 'details2': '- 5레벨만 달성해도 달빛조각사 이모티콘 100% 지급!'}},
        {'id': '3', 'packagename': 'com.ncsoft.lineagem19', 'gametitle': "리니지M",
         'gamedesc': {'details1': 'PC의 향수! 리니지 본질 그대로 리니지M', 'details2': 'PC리니지와 동일한 아덴월드의 오픈 필드'}},
        {'id': '4', 'packagename': 'com.netmarble.bnsmkr', 'gametitle': '블레이드&소울 레볼루션',
         'gamedesc': {'details1': '원작 감성의 방대한 세계관과 복수 중심의 흥미진진한 스토리', 'details2': 'MMORPG의 필드를 제대로 즐길 수 있는 경공'}},
        {'id': '5', 'packagename': 'com.cjenm.sknights', 'gametitle': '세븐나이츠',
         'gamedesc': {'details1': 'Netmarble롤플레잉', 'details2': '세나의 재탄생, 세븐나이츠: 리부트'}},
        {'id': '6', 'packagename': 'com.google.android.youtube', 'gametitle': 'YouTube',
         'gamedesc': {'details1': 'Google LLC동영상 플레이어/편집기', 'details2': '좋아하는 동영상 빠르게 검색하기'}},
    ]

    WriteString('C:\\game.json', '[')
    i = 0
    for row in testdata:
        WriteJsonString('C:\\game.json', row)
        if i < 5:
            WriteString('C:\\game.json', ',')
        i = i + 1
    WriteString('C:\\game.json', ']')

    game = GetJson('C:\\game.json')
    for i in game:
        print(i['id'], i['packagename'], i['gametitle'], i['gamedesc']['details1'], i['gamedesc']['details2'])
    pass


def func4():
    testdata = [
        {'id': '1', 'packagename': 'com.pearlabyss.blackdesertm', 'gametitle': '검은사막 모바일',
         'gamedesc': {'details1': '당신이 진짜로 원했던 모험의 시작', 'details2': '월드클래스 MMORPG “검은사막 모바일”'}},
        {'id': '2', 'packagename': 'com.kakaogames.moonlight', 'gametitle': '달빛조각사',
         'gamedesc': {'details1': "500만 구독자의 게임 판타지 대작 '달빛조각사'", 'details2': '- 5레벨만 달성해도 달빛조각사 이모티콘 100% 지급!'}},
        {'id': '3', 'packagename': 'com.ncsoft.lineagem19', 'gametitle': "리니지M",
         'gamedesc': {'details1': 'PC의 향수! 리니지 본질 그대로 리니지M', 'details2': 'PC리니지와 동일한 아덴월드의 오픈 필드'}},
        {'id': '4', 'packagename': 'com.netmarble.bnsmkr', 'gametitle': '블레이드&소울 레볼루션',
         'gamedesc': {'details1': '원작 감성의 방대한 세계관과 복수 중심의 흥미진진한 스토리', 'details2': 'MMORPG의 필드를 제대로 즐길 수 있는 경공'}},
        {'id': '5', 'packagename': 'com.cjenm.sknights', 'gametitle': '세븐나이츠',
         'gamedesc': {'details1': 'Netmarble롤플레잉', 'details2': '세나의 재탄생, 세븐나이츠: 리부트'}},
        {'id': '6', 'packagename': 'com.google.android.youtube', 'gametitle': 'YouTube',
         'gamedesc': {'details1': 'Google LLC동영상 플레이어/편집기', 'details2': '좋아하는 동영상 빠르게 검색하기'}},
    ]

    jsonobj = clsjsonutil('C:\\game.json')

    jsonobj.WriteString('[')
    i = 0
    for row in testdata:
        jsonobj.WriteJsonString(row)
        if i < 5:
            jsonobj.WriteString(',')
        i = i + 1
    jsonobj.WriteString(']')

    game = jsonobj.GetJson()
    for i in game:
        print(i['id'], i['packagename'], i['gametitle'], i['gamedesc']['details1'], i['gamedesc']['details2'])


def func5():
    req = GetWebPage('https://github.com/ImDaeseong')
    print(req)
    GetDownloadFile(
        'http://content.screencast.com/users/JamesMontemagno/folders/Jing/media/23c1dd13-333a-459e-9e23-c3784e7cb434/2016-06-02_1049.png')


def func6():
    obj = clsdownloadutil()
    req = obj.Get_WebPage('https://github.com/ImDaeseong')
    print(req)
    obj.Get_DownloadFile(
        'http://content.screencast.com/users/JamesMontemagno/folders/Jing/media/23c1dd13-333a-459e-9e23-c3784e7cb434/2016-06-02_1049.png')


def func7():
    AddWords('lipas', '바퀴벌레')
    AddWords('muram', '우울한우울한')
    AddWords('persaingan', '경쟁')
    AddWords('rawit', '작은')
    # GetWordsList()
    RemoveWords('lipas')
    AddWords('tikung', '커브길')
    UpdateWords('muram', '우울한')
    GetWordsList()


def func8():
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


def func9():
    print(isDir('E:\\test'))
    print(isFile('E:\\DaeseongPython\\main.py'))
    print(IsDirExist('E:\\test'))
    print(IsDirExist('E:\\DaeseongPython\\main.py'))
    print(GetFilePath('E:\\DaeseongPython\\afdasdf\\main.py'))
    print(GetFileName('E:\\DaeseongPython\\afdasdf\\main.py'))
    DeleteFile('E:\\liteidex30.3.windows-qt5.zip')
    DeleteFile('E:\\a')
    if IsDirExist('E:\\a.txt'):
        ReadLineFile('E:\\a.txt')

    FileList = FindFileList('E:\\a')
    # print(len(FileList))
    for i in range(len(FileList)):
        print(FileList[i])

    dirList = FindDirList('E:\\a')
    for dir in dirList:
        print(dir)


def func10():
    clsobj = clsfiledutil()
    print(clsobj.isDir('E:\\test'))
    print(clsobj.isFile('E:\\DaeseongPython\\main.py'))
    print(clsobj.IsDirExist('E:\\test'))
    print(clsobj.IsDirExist('E:\\DaeseongPython\\main.py'))
    print(clsobj.GetFilePath('E:\\DaeseongPython\\afdasdf\\main.py'))
    print(clsobj.GetFileName('E:\\DaeseongPython\\afdasdf\\main.py'))
    clsobj.DeleteFile('E:\\liteidex30.3.windows-qt5.zip')
    clsobj.DeleteFile('E:\\a')
    if clsobj.IsDirExist('E:\\a.txt'):
        clsobj.ReadLineFile('E:\\a.txt')

    FileList = clsobj.FindFileList('E:\\a')
    # print(len(FileList))
    for i in range(len(FileList)):
        print(FileList[i])

    dirList = clsobj.FindDirList('E:\\a')
    for dir in dirList:
        print(dir)


def func11():
    Zipfile('E:\\a', 'C:\\a.zip')
    UnZipfile('C:\\a.zip', 'C:\\')


def func12():
    clsobj = clsziputil()
    clsobj.Zipfile('E:\\a', 'C:\\a.zip')
    clsobj.UnZipfile('C:\\a.zip', 'C:\\')


def func13():
    """
    SetregistryString32("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryString32("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    DeleteValueregistry32("Software\\Daeseong\\Daeseong", "Gamekey1")
    DeleteKeyregistry32("Software\\Daeseong\\Daeseong")
    DeleteKeyregistry32("Software\\Daeseong")
    """


    """
    SetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    # DeleteValueregistryWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")

    """
    SetregistryString("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryString("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    DeleteValueregistry("Software\\Daeseong\\Daeseong", "Gamekey1")

    DeleteKeyregistry("Software\\Daeseong\\Daeseong")
    DeleteKeyregistry("Software\\Daeseong")
    """


def func14():
    clsobj = clsregistryutil()

    """
    clsobj.SetregistryString32("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryString32("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    clsobj.DeleteValueregistry32("Software\\Daeseong\\Daeseong", "Gamekey1")

    clsobj.DeleteKeyregistry32("Software\\Daeseong\\Daeseong")
    clsobj.DeleteKeyregistry32("Software\\Daeseong")
    """

    """
    clsobj.SetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    # clsobj.DeleteValueregistryWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")

    """
    clsobj.SetregistryString("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryString("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    clsobj.DeleteValueregistry("Software\\Daeseong\\Daeseong", "Gamekey1")
    clsobj.DeleteKeyregistry("Software\\Daeseong\\Daeseong")
    clsobj.DeleteKeyregistry("Software\\Daeseong")
    """


if __name__ == '__main__':
    """
    func1()
    func2()
    func3()
    func4()
    func5()
    func6()
    func7()
    func8()
    func9()
    func10()
    func11()
    func12()
    func13()
    func14()
    """
